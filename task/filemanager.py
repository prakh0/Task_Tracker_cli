import json
import os
from task.entity import Task

TASK_FILE = "task.json"


class FileManager:
    def __init__(self):
        pass

    @staticmethod
    def load_task():
        if not os.path.exists(TASK_FILE) or os.path.getsize(TASK_FILE) == 0:
            FileManager.save_task([])
            return []
        try:
            with open(TASK_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error reading {TASK_FILE}: {e}. Resetting task list...")
            FileManager.save_task([])
            return []

    @staticmethod
    def save_task(tasks: list[Task]):
        tasks_dict = [task.__dict__ for task in tasks]
        try:
            with open(TASK_FILE, "w", encoding="utf-8") as file:
                json.dump(tasks_dict, file, indent=4, ensure_ascii=False)
            print(f"Tasks saved to {TASK_FILE}")
        except IOError as e:
            print(f"An error occurred while saving tasks: {e}")
