from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import json


class TaskStatus(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class Task:
    def __init__(
        self,
        id: int,
        description: str,
        status: TaskStatus,
        createdAt=None,
        updatedAt=None,
    ):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt or datetime.now().isoformat()
        self.updatedAt = updatedAt

    def __str__(self):
        return f"ID {self.id}, Description {self.description}, Status {self.status}, Created_At {self.createdAt}, Updated_At {self.updatedAt}"
