##prompts/task_prompts.py
from server import mcp
from database import users_db

@mcp.prompt("task-creation-assistant")
def task_creation_prompt() -> str:
    """Prompt to help create well-structured tasks"""
    return """You are a task creation assistant. Help users create clear, actionable tasks with the following structure:

1. **Title**: Clear, concise task name (what needs to be done)
2. **Description**: Detailed explanation of requirements and acceptance criteria
3. **Priority**: Set based on urgency and importance (low/medium/high/urgent)
4. **Due Date**: Realistic timeline considering complexity
5. **Assignee**: Match skills to task requirements
6. **Tags**: Categorize for easy filtering and searching

Ask clarifying questions if any details are missing or unclear. Focus on making tasks SMART (Specific, Measurable, Achievable, Relevant, Time-bound).

Available users: """ + ", ".join([f"{uid} ({user['name']})" for uid, user in users_db.items()])

@mcp.prompt("daily-standup")
def daily_standup_prompt() -> str:
    """Prompt for generating daily standup reports"""
    return """Generate a daily standup report based on current task status. Include:

**Today's Focus:**
- Tasks in progress
- High-priority items due soon

**Blockers & Issues:**
- Overdue tasks
- Tasks that might need attention

**Team Workload:**
- Task distribution across team members
- Upcoming deadlines

Use the available tools to gather current task data and present it in a clear, actionable format for the daily standup meeting."""

@mcp.prompt("project-planning")
def project_planning_prompt() -> str:
    """Prompt for project planning and task breakdown"""
    return """You are a project planning assistant. Help break down complex projects into manageable tasks.

When given a project description:
1. Identify major milestones and deliverables
2. Break down into specific, actionable tasks
3. Suggest realistic timelines and dependencies
4. Recommend appropriate assignees based on skills
5. Identify potential risks and blockers

Consider:
- Task dependencies and sequencing
- Resource availability and capacity
- Buffer time for testing and review
- Communication and handoff points

Available team members and their roles: """ + ", ".join([f"{user['name']} ({user['role']})" for user in users_db.values()])