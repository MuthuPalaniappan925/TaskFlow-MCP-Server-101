# resources/task_resources.py
from server import mcp
from database import tasks_db, users_db
import json
from datetime import datetime

@mcp.resource("task://{task_id}")
def get_task_resource(task_id: str) -> str:
    """Get task as a JSON resource"""
    if task_id not in tasks_db:
        return f"Task '{task_id}' not found."
    
    task_data = tasks_db[task_id].copy()
    task_data["task_id"] = task_id
    return json.dumps(task_data, indent=2)

@mcp.resource("user://{user_id}/tasks")
def get_user_tasks_resource(user_id: str) -> str:
    """Get all tasks for a user as JSON resource"""
    if user_id not in users_db:
        return f"User '{user_id}' not found."
    
    user_tasks = {
        tid: task for tid, task in tasks_db.items() 
        if task["assigned_to"] == user_id
    }
    
    return json.dumps({
        "user": users_db[user_id],
        "tasks": user_tasks
    }, indent=2)

@mcp.resource("dashboard://summary")
def get_dashboard_summary() -> str:
    """Get task dashboard summary"""
    total_tasks = len(tasks_db)
    status_counts = {}
    priority_counts = {}
    
    for task in tasks_db.values():
        status_counts[task["status"]] = status_counts.get(task["status"], 0) + 1
        priority_counts[task["priority"]] = priority_counts.get(task["priority"], 0) + 1
    
    summary = {
        "total_tasks": total_tasks,
        "status_breakdown": status_counts,
        "priority_breakdown": priority_counts,
        "total_users": len(users_db),
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return json.dumps(summary, indent=2)