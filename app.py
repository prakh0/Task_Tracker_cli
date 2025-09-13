import json
import sys
from taskmanager import TaskManager
from entity import TaskStatus


def valid_commands():
    print("Commands that could be used:")
    print("  python.py add <description>")
    print("  python.py update <id> <new_description>")
    print("  python.py delete <id>")
    print("  python.py in_progress <id>")
    print("  python.py completed <id>")
    print("  python.py list [status]")
    print("  status must be one of: TODO, IN_PROGRESS, DONE")


def error_exit(message):
    print(f"Error: {message}")
    valid_commands()
    sys.exit(1)


def get_task_id():
    try:
        return int(sys.argv[2])
    except (ValueError, IndexError):
        error_exit("Please provide a valid task ID")


def main():
    print("Script started")

    if len(sys.argv) < 2:
        error_exit("Missing command")

    command = sys.argv[1].lower()
    tm = TaskManager()

    if command == "add":
        if len(sys.argv) < 3:
            error_exit("Please provide a description")
        description = " ".join(sys.argv[2:])
        task_id = tm.add_task(description)
        print(f"Task is successfully added (ID '{task_id}')")

    elif command == "update":
        task_id = get_task_id()
        if len(sys.argv) < 4:
            error_exit("Please provide a new description")
        new_description = " ".join(sys.argv[3:])
        tm.update_task(task_id, new_description)
        print(f"Task '{task_id}' is successfully updated")

    elif command == "delete":
        task_id = get_task_id()
        tm.delete_task(task_id)
        print(f"Task '{task_id}' is successfully deleted")

    elif command == "in_progress":
        task_id = get_task_id()
        tm.mark_in_process(task_id)
        print(f"Task '{task_id}' is marked as IN_PROGRESS")

    elif command == "completed":
        task_id = get_task_id()
        tm.mark_completed(task_id)
        print(f"Task '{task_id}' is marked as DONE")

    elif command == "list":
        if len(sys.argv) == 2:
            tm.list_tasks()
        else:
            status = sys.argv[2].upper()
            if status in TaskStatus.__members__:
                tm.list_tasks(TaskStatus[status].value)
            else:
                error_exit("Please provide a valid status (TODO, IN_PROGRESS, DONE)")

    else:
        error_exit(f"Unknown command '{command}'")


if __name__ == "__main__":
    main()
