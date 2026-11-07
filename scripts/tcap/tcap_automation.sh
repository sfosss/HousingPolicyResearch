#!/bin/bash
# TCAP Housing Subsidy Reform - Automated Task Management & Reporting
# Usage: ./tcap_automation.sh [daily|weekly|monthly]
# Designed for cron scheduling

set -e

LOG_FILE="tcap_automation.log"
CSV_PATH="NYC_Housing_Subsidy_Ops_Tasks_Notion.csv"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

log() {
    echo "[${TIMESTAMP}] $1" | tee -a "$LOG_FILE"
}

generate_reports() {
    log "🔄 Generating daily reports..."

    # Run Python automation
    python3 tcap_task_automation.py report --csv "$CSV_PATH"
    log "✅ Status report generated: TCAP_Status_Report.txt"

    python3 tcap_task_automation.py risk --csv "$CSV_PATH"
    log "✅ Risk assessment complete"

    # Create timestamped backup
    BACKUP="backups/TCAP_Tasks_v$(date +%Y%m%d_%H%M%S).csv"
    mkdir -p backups
    cp "$CSV_PATH" "$BACKUP"
    log "📁 Task backup created: $BACKUP"
}

weekly_review() {
    log "📊 Running weekly review..."

    # Summarize overdue tasks
    python3 -c "
import csv
from datetime import datetime as dt
today = dt.now()
with open('$CSV_PATH') as f:
    tasks = list(csv.DictReader(f))
    overdue = [t for t in tasks if t.get('Status') != 'Complete' 
               and dt.strptime(t.get('Due Date', '2099-01-01'), '%Y-%m-%d') < today]
    print(f'\n⚠️  OVERDUE TASKS: {len(overdue)}')
    for t in overdue[:5]:
        print(f'   • {t.get("Task")[:60]}')
"

    log "✅ Weekly review complete"
}

monthly_archive() {
    log "📦 Creating monthly archive..."

    MONTH=$(date '+%Y-%m')
    ARCHIVE="archives/TCAP_Tasks_${MONTH}.tar.gz"
    mkdir -p archives

    tar -czf "$ARCHIVE" *.csv *.txt tcap_*.py 2>/dev/null || true
    log "✅ Monthly archive: $ARCHIVE"
}

main() {
    case "$1" in
        daily)
            generate_reports
            ;;
        weekly)
            generate_reports
            weekly_review
            ;;
        monthly)
            generate_reports
            weekly_review
            monthly_archive
            ;;
        *)
            echo "Usage: $0 [daily|weekly|monthly]"
            exit 1
            ;;
    esac

    log "✅ Automation cycle complete"
}

main "$@"
