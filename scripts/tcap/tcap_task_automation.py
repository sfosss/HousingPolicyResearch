#!/usr/bin/env python3
"""
TCAP Housing Subsidy Reform - Automated Task Management & Risk Monitoring
Fixed version - preserves exact CSV structure
"""

import csv
from datetime import datetime
from collections import defaultdict
import argparse


class TCAPTaskManager:
    """Main task automation engine with risk radar & version control"""

    def __init__(self, csv_path="NYC_Housing_Subsidy_Ops_Tasks_Notion.csv"):
        self.csv_path = csv_path
        self.tasks = []
        self.fieldnames = []
        self.dependencies = defaultdict(list)

    def load_tasks(self):
        """Load tasks from CSV"""
        try:
            with open(self.csv_path, "r") as f:
                reader = csv.DictReader(f)
                self.fieldnames = reader.fieldnames
                self.tasks = list(reader)
            print(f"✅ Loaded {len(self.tasks)} tasks from {self.csv_path}")
            return True
        except FileNotFoundError:
            print(f"❌ Error: {self.csv_path} not found")
            return False

    def infer_dependencies(self):
        """Map task dependencies by section order"""
        section_order = {
            "Intake/Triage": 0,
            "Research": 1,
            "Drafting": 2,
            "Decision": 3,
            "QA": 4,
            "Automation": 5,
            "Version Control": 6,
            "Deliverables": 7,
        }

        for i, task_i in enumerate(self.tasks):
            section_i = task_i.get("Section", "").strip()
            order_i = section_order.get(section_i, 999)

            blockers = []
            for j, task_j in enumerate(self.tasks):
                if i == j:
                    continue
                section_j = task_j.get("Section", "").strip()
                order_j = section_order.get(section_j, 999)

                if order_j < order_i:
                    blockers.append(j)

            if blockers:
                self.dependencies[i] = blockers

    def generate_risk_report(self):
        """Generate risk assessment by category"""
        risk_scores = {
            "legal": 0,
            "fiscal": 0,
            "operational": 0,
        }

        for task in self.tasks:
            task_text = (task.get("Task", "") + " " + task.get("Notes", "")).lower()
            status = task.get("Status", "Not Started")
            status_map = {
                "Not Started": 3,
                "In Progress": 2,
                "Complete": 0,
            }
            multiplier = status_map.get(status, 2)

            legal_kws = ["legal", "title", "aida", "504", "procurement"]
            if any(kw in task_text for kw in legal_kws):
                risk_scores["legal"] += multiplier
            fiscal_kws = ["budget", "mou", "cfo", "funding", "roi"]
            if any(kw in task_text for kw in fiscal_kws):
                risk_scores["fiscal"] += multiplier
            ops_kws = ["automation", "version", "process"]
            if any(kw in task_text for kw in ops_kws):
                risk_scores["operational"] += multiplier

        return risk_scores

    def export_status_report(self, output_file="TCAP_Status_Report.txt"):
        """Export comprehensive status report"""
        with open(output_file, "w") as f:
            f.write("=" * 80 + "\n")
            f.write("TCAP HOUSING SUBSIDY REFORM - TASK STATUS REPORT\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write("=" * 80 + "\n\n")

            # Status breakdown
            status_counts = defaultdict(int)
            for task in self.tasks:
                status = task.get("Status", "Not Started")
                status_counts[status] += 1

            f.write("STATUS BREAKDOWN:\n")
            for status, count in sorted(status_counts.items()):
                pct = round(count / len(self.tasks) * 100, 1)
                f.write(f"  {status:<20} {count:>3} ({pct:>5.1f}%)\n")

            # Risk assessment
            f.write("\nRISK ASSESSMENT:\n")
            risk = self.generate_risk_report()
            for risk_type, score in risk.items():
                f.write(f"  {risk_type.upper():<20} {score:>3} / 60\n")

            # Overdue tasks
            from datetime import datetime as dt

            today = dt.now()
            overdue = []
            for task in self.tasks:
                due_str = task.get("Due Date", "")
                status = task.get("Status", "Not Started")
                if due_str and status != "Complete":
                    try:
                        due = dt.strptime(due_str, "%Y-%m-%d")
                        if due < today:
                            overdue.append(
                                (task.get("Task", ""), due_str, (today - due).days)
                            )
                    except ValueError:
                        pass

            if overdue:
                f.write(f"\nOVERDUE TASKS ({len(overdue)}):\n")
                for task_name, due_date, days_over in sorted(
                    overdue, key=lambda x: x[2], reverse=True
                ):
                    f.write(f"  [{days_over:>2}d] {task_name[:60]}\n")

        print(f"✅ Status report exported to {output_file}")
        return output_file

    def update_task_status(self, task_index, new_status):
        """Update a task status and save to CSV (preserves exact structure)"""
        if 0 <= task_index < len(self.tasks):
            old_status = self.tasks[task_index].get("Status", "")
            self.tasks[task_index]["Status"] = new_status

            # Save with EXACT original fieldnames
            with open(self.csv_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(self.tasks)

            print(f"✅ Updated TASK_{task_index:03d}: {old_status} → {new_status}")
            return True
        return False


def main():
    parser = argparse.ArgumentParser(description="TCAP Task Automation Manager")
    parser.add_argument(
        "action",
        choices=["update", "report", "risk", "dependencies"],
        help="Action to perform",
    )
    parser.add_argument(
        "--csv",
        default="NYC_Housing_Subsidy_Ops_Tasks_Notion.csv",
        help="Path to task CSV",
    )
    parser.add_argument("--task-id", type=int, help="Task index for update")
    parser.add_argument("--status", help="New status for task")

    args = parser.parse_args()

    manager = TCAPTaskManager(args.csv)
    if not manager.load_tasks():
        return

    manager.infer_dependencies()

    if args.action == "report":
        manager.export_status_report()
    elif args.action == "risk":
        risk = manager.generate_risk_report()
        print("\nRISK ASSESSMENT:")
        for risk_type, score in risk.items():
            print(f"  {risk_type.upper():<20} {score:>3} / 60")
    elif args.action == "dependencies":
        with_blockers = len([d for d in manager.dependencies.values() if d])
        print(f"\nDEPENDENCY GRAPH: {with_blockers} tasks with blockers")
    elif args.action == "update":
        if args.task_id is not None and args.status:
            manager.update_task_status(args.task_id, args.status)
        else:
            print("Error: --task-id and --status required for update action")


if __name__ == "__main__":
    main()
