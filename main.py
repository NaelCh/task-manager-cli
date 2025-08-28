import argparse
from task_manager import TaskManager

def main():
    manager = TaskManager()

    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add", help="Προσθήκη νέου task")
    add_parser.add_argument("title", help="Τίτλος του task")
    add_parser.add_argument("description", help="Περιγραφή του Task")

    # list
    subparsers.add_parser("list", help="Εμφάνιση όλων των tasks")

    # done
    done_parser = subparsers.add_parser("done", help="Ολοκλήρωση task")
    done_parser.add_argument("id", help="ID του task")

    # remove
    remove_parser = subparsers.add_parser("remove", help="Διαγραφή task")
    remove_parser.add_argument("id", help="ID του task")

    args = parser.parse_args()

    if args.command == "add":
        task = manager.add_task(args.title, args.description)
        print(f"✅ Προστέθηκε task: {task.id} | {task.title}")

    elif args.command == "list":
        tasks = manager.list_tasks()
        if not tasks:
            print("📭 Δεν υπάρχουν tasks.")
        else:
            for t in tasks:
                status = "✔️" if t.completed else "❌"
                print(f"{t.id | {status} | {t.title} - {t.description}}")

    elif args.command == "done":
        if manager.mark_completed(args.id):
            print(f"✔️ Το task {args.id} ολοκληρώθηκε.")
        else:
            print("⚠️Δεν βρέθηκε task με αυτό το ID.")

    elif args.command == "remove":
        manager.remove_task(args.id)
        print(f"🗑 Το task {args.id} διαγράφηκε.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
