##database.py
from datetime import datetime

##In-memory task database (demonstration purposes only)
tasks_db = {
    "TSK001": {
        "title": "Complete project documentation",
        "description": "Write comprehensive documentation for the new feature",
        "status": "in_progress",
        "priority": "high",
        "assigned_to": "muthu.pal",
        "due_date": "2025-06-30",
        "created_at": "2025-06-15",
        "tags": ["documentation", "project"],
        "completed_at": None
    },
    "TSK002": {
        "title": "Code review for authentication module",
        "description": "Review the new authentication implementation",
        "status": "pending",
        "priority": "medium",
        "assigned_to": "ankitha.pal",
        "due_date": "2025-06-25",
        "created_at": "2025-06-20",
        "tags": ["code-review", "security"],
        "completed_at": None
    }
}

##User database (demonstration purposes only)
users_db = {
    "muthu.pal": {"name": "Muthu Palaniappan", "email": "muthu@pal.com", "role": "developer"},
    "ankitha.pal": {"name": "Ankitha Palaniappan", "email": "ankitha@pal.com", "role": "senior_developer"}
}