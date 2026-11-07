#!/usr/bin/env python3
"""
Sync TCAP tasks to GitHub automatically
"""
import subprocess
from datetime import datetime


def sync():
    try:
        # Add the CSV file
        subprocess.run(
            ["git", "add", "NYC_Housing_Subsidy_Ops_Tasks_Notion.csv"], check=True
        )

        # Commit with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = subprocess.run(
            ["git", "commit", "-m", f"[Auto-sync] TCAP task update - {timestamp}"],
            capture_output=True,
            text=True,
        )

        # If there are changes, push
        if result.returncode == 0:
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print("✅ Synced to GitHub successfully")
        else:
            print("ℹ️  No changes to sync")

    except subprocess.CalledProcessError as e:
        print(f"⚠️  Sync skipped: {e}")


if __name__ == "__main__":
    sync()
