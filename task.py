import uuid
import datetime


class Task:
    def __init__(self, title, description):
        """Αρχικοποίηση στοιχείων του task κατά τη δημιουργία του αντικειμένου"""

        self.id = str(uuid.uuid4())  # Μοναδικό ID
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """Μέθοδος που επιστρέφει ένα λεξικό"""

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        """Δημιουργεί ένα αντικείμενο (Task) απο λεξικό (data)"""

        task = Task(data["title"], data["description"])
        task.id = data["id"]
        task.completed = data["completed"]
        task.created_at = data["created_at"]
