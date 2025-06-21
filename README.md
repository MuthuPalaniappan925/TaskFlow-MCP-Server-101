# TaskFlow MCP Server 101 [Learning]

Model Context Protocol (MCP) server for task management, built with FastMCP. Integrate task management capabilities into Claude Desktop.

## Components

### Task Management Tools
- **Create Tasks**: Generate new tasks with detailed specifications
- **Update Status**: Track progress through pending, in-progress, completed, cancelled
- **Task Details**: Get comprehensive information about any task
- **User Tasks**: List all tasks for specific team members
- **Overdue Tracking**: Identify and manage overdue tasks
- **Smart Search**: Find tasks by title, description, or tags

### Resources
- **Task Resource**: JSON representation of individual tasks
- **User Task Lists**: Complete task portfolios for team members  
- **Dashboard Summary**: Real-time project statistics and metrics

### Model Prompts
- **Task Creation Assistant**: Guided task creation with SMART criteria
- **Daily Standup**: Automated standup report generation
- **Project Planning**: Break down complex projects into manageable tasks

## Architecture

```
taskflow-mcp/
├── server.py              # Shared MCP server instance
├── database.py           # In-memory data storage
├── main.py              # Application entry point
├── tools/
│   └── task_tools.py    # Task management tools
├── resources/
│   └── task_resources.py # Task data resources
└── prompts/
    └── task_prompts.py   # assistant prompts
```

## Quick Start

### Prerequisites
- Python 3.10+
- conda or pip (conda pref)
- Claude Desktop (for integration)

### Installation

1. **Create and activate conda environment:**
```bash
conda create -n mcp-project python=3.10
conda activate mcp-project
```

2. **Install dependencies:**
```bash
pip install mcp requests
pip install --upgrade typer
```

3. **Initialize project with uv:**
```bash
uv init taskflow-mcp
cd taskflow-mcp
```

4. **Add the modular code** to your project structure (see files above)

5. **Install MCP CLI support:**
```bash
uv add "mcp[cli]"
```

6. **Install the MCP server:**
```bash
uv run mcp install main.py
```

### Claude Desktop Integration

1. **Open Claude Desktop config file:**
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. **Add TaskFlow MCP configuration:**
```json
{
  "mcpServers": {
    "TaskFlow": {
      "command": "/path/to/your/project/.venv/Scripts/python.exe",
      "args": [
        "/path/to/your/project/main.py"
      ]
    }
  }
}
```

3. **Restart Claude Desktop** and you'll see TaskFlow tools available!

## Usage [Examples]

### Creating a Task
```
Create a high-priority task for "Implement user authentication" assigned to muthu.pal with due date 2025-07-15
```

### Checking Team Status  
```
Show me all tasks for ankitha.pal that are currently in progress
```

### Daily Standup
```
Generate a daily standup report showing today's focus items and any blockers
```

### Project Planning
```
Help me break down a "Mobile App Development" project into manageable tasks
```

## Available Tools

| Tool | Description |
|------|-------------|
| `create_task` | Create new tasks with full specifications |
| `update_task_status` | Update task status and track completion |
| `get_task_details` | Retrieve comprehensive task information |
| `list_tasks_by_user` | Filter tasks by assignee and status |
| `get_overdue_tasks` | Identify overdue items needing attention |
| `search_tasks` | Search across titles, descriptions, and tags |
