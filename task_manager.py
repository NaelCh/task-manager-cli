import json
import os
from task import Task

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def add_task(self, title, description):
        """Προσθέτει task"""

        task = Task(title, description)
        self.tasks.append(task)
        self.save_to_file()
        return task

    def remove_task(self, task_id):
        """Αφαιρεί task"""

        new_tasks = []
        for task in self.tasks:
            if task.id != task_id:
                new_tasks.append(task)

        self.tasks = new_tasks
        self.save_to_file()

    def mark_completed(self, task_id):
        """Σημειώνει ένα task ως ολοκληρωμένο"""

        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self.save_to_file()
                return True
        return False

    def list_tasks(self):
        """Επιστρέφει τα tasks"""

        return self.tasks

    def save_to_file(self):
        """Αποθηκεύει task"""

        data = [task.to_dict() for task in self.tasks]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        """Φορτώνει task"""

        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.tasks = [Task.from_dict(item) for item in data]
