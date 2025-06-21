# tools/task_tools.py
from server import mcp
from database import tasks_db, users_db
from typing import List, Optional
from datetime import datetime

@mcp.tool()
def create_task(title: str, description: str, assigned_to: str, priority: str = "medium", due_date: Optional[str] = None, tags: Optional[List[str]] = None) -> str:
    """
    Create a new task with the specified details.
    Priority can be: low, medium, high, urgent
    """
    ##Generate new task ID
    task_ids = [int(tid[3:]) for tid in tasks_db.keys()]
    new_id = f"TSK{max(task_ids) + 1:03d}" if task_ids else "TSK001"
    
    ##Validate user
    if assigned_to not in users_db:
        return f"Error: User '{assigned_to}' not found in system."
    
    ##Create task
    new_task = {
        "title": title,
        "description": description,
        "status": "pending",
        "priority": priority.lower(),
        "assigned_to": assigned_to,
        "due_date": due_date,
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "tags": tags or [],
        "completed_at": None
    }
    
    tasks_db[new_id] = new_task
    return f"Task '{new_id}' created successfully and assigned to {users_db[assigned_to]['name']}."

@mcp.tool()
def update_task_status(task_id: str, status: str) -> str:
    """
    Update task status. Valid statuses: pending, in_progress, completed, cancelled
    """
    if task_id not in tasks_db:
        return f"Error: Task '{task_id}' not found."
    
    valid_statuses = ["pending", "in_progress", "completed", "cancelled"]
    if status.lower() not in valid_statuses:
        return f"Error: Invalid status. Valid options: {', '.join(valid_statuses)}"
    
    old_status = tasks_db[task_id]["status"]
    tasks_db[task_id]["status"] = status.lower()
    
    ##Set completion date if completed
    if status.lower() == "completed":
        tasks_db[task_id]["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return f"Task '{task_id}' status updated from '{old_status}' to '{status.lower()}'."

@mcp.tool()
def get_task_details(task_id: str) -> str:
    """Get detailed information about a specific task"""
    if task_id not in tasks_db:
        return f"Error: Task '{task_id}' not found."
    
    task = tasks_db[task_id]
    user_name = users_db.get(task["assigned_to"], {}).get("name", task["assigned_to"])
    
    details = f"""
Task ID: {task_id}
Title: {task["title"]}
Description: {task["description"]}
Status: {task["status"].title()}
Priority: {task["priority"].title()}
Assigned to: {user_name}
Due Date: {task["due_date"] or "Not set"}
Created: {task["created_at"]}
Tags: {', '.join(task["tags"]) if task["tags"] else "None"}
Completed: {task["completed_at"] or "Not completed"}
"""
    return details.strip()

@mcp.tool()
def list_tasks_by_user(user_id: str, status_filter: Optional[str] = None) -> str:
    """
    List all tasks assigned to a specific user, optionally filtered by status
    """
    if user_id not in users_db:
        return f"Error: User '{user_id}' not found."
    
    user_tasks = [
        (tid, task) for tid, task in tasks_db.items() 
        if task["assigned_to"] == user_id
    ]
    
    if status_filter:
        user_tasks = [
            (tid, task) for tid, task in user_tasks 
            if task["status"] == status_filter.lower()
        ]
    
    if not user_tasks:
        filter_text = f" with status '{status_filter}'" if status_filter else ""
        return f"No tasks found for {users_db[user_id]['name']}{filter_text}."
    
    result = f"Tasks for {users_db[user_id]['name']}:\n"
    for tid, task in user_tasks:
        result += f"- {tid}: {task['title']} ({task['status']}, {task['priority']} priority)\n"
    
    return result.strip()

@mcp.tool()
def get_overdue_tasks() -> str:
    """Get all tasks that are past their due date and not completed"""
    today = datetime.now().strftime("%Y-%m-%d")
    overdue_tasks = []
    
    for tid, task in tasks_db.items():
        if (task["due_date"] and 
            task["due_date"] < today and 
            task["status"] not in ["completed", "cancelled"]):
            overdue_tasks.append((tid, task))
    
    if not overdue_tasks:
        return "No overdue tasks found."
    
    result = "Overdue Tasks:\n"
    for tid, task in overdue_tasks:
        user_name = users_db.get(task["assigned_to"], {}).get("name", task["assigned_to"])
        days_overdue = (datetime.now() - datetime.strptime(task["due_date"], "%Y-%m-%d")).days
        result += f"- {tid}: {task['title']} (Due: {task['due_date']}, {days_overdue} days overdue, Assigned to: {user_name})\n"
    
    return result.strip()

@mcp.tool()
def search_tasks(query: str) -> str:
    """Search tasks by title, description, or tags"""
    query = query.lower()
    matching_tasks = []
    
    for tid, task in tasks_db.items():
        if (query in task["title"].lower() or 
            query in task["description"].lower() or 
            any(query in tag.lower() for tag in task["tags"])):
            matching_tasks.append((tid, task))
    
    if not matching_tasks:
        return f"No tasks found matching '{query}'."
    
    result = f"Tasks matching '{query}':\n"
    for tid, task in matching_tasks:
        result += f"- {tid}: {task['title']} ({task['status']})\n"
    
    return result.strip()