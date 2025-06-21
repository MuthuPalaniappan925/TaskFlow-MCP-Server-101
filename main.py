##main.py
from server import mcp

##Import modules so they get registered via decorators
import tools.task_tools
import resources.task_resources
import prompts.task_prompts

##Entry point to run the server
if __name__ == "__main__":
    mcp.run()