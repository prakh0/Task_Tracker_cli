from datetime import datetime
from filemanager import FileManager
from entity import Task, TaskStatus


class TaskManager:
    def __init__(self):
        task_array = FileManager.load_task()
        self.tasks: list[Task] = [Task(**item) for item in task_array]

    def add_task(self, description: str) -> int:
        existing_ids = sorted({task.id for task in self.tasks})
        task_id = 1
        for existing_id in existing_ids:
            if task_id < existing_id:
                break
            task_id += 1
        task = Task(id=task_id, description=description, status=TaskStatus.TODO)
        self.tasks.append(task)
        FileManager.save_task(self.tasks)
        print(f"Task is successfully added (ID {task_id})")
        return task_id

    def update_task(self, task_id: int, new_description: str) -> None:
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            task.description = new_description
            task.updatedAt = datetime.now().isoformat()
            FileManager.save_task(self.tasks)
            print(f"Task {task_id} is successfully updated")
        else:
            print(f"Task {task_id} not found")

    def delete_task(self, task_id: int) -> None:
        self.tasks = [task for task in self.tasks if task.id != task_id]
        FileManager.save_task(self.tasks)
        print(f"Task {task_id} is successfully deleted")

    def mark_in_process(self, task_id: int) -> None:
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            task.status = TaskStatus.IN_PROGRESS
            task.updatedAt = datetime.now().isoformat()
            FileManager.save_task(self.tasks)
            print(f"Task {task_id} is marked as IN_PROGRESS")
        else:
            print(f"Task {task_id} not found")

    def mark_completed(self, task_id: int) -> None:
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            task.status = TaskStatus.DONE
            task.updatedAt = datetime.now().isoformat()
            FileManager.save_task(self.tasks)
            print(f"Task {task_id} is marked as DONE")
        else:
            print(f"Task {task_id} not found")

    def list_tasks(self, status=None) -> list[Task]:
        tasks_to_list = self.tasks
        if status:
            tasks_to_list = [task for task in self.tasks if task["status"] == status]
        for task in tasks_to_list:
            print(task)
