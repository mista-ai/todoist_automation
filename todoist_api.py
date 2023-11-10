from datetime import datetime
from todoist_api_python.api import TodoistAPI
from pprint import pprint

# Replace with your Todoist API key
api = TodoistAPI('api_key')

try:
    projects = api.get_projects()
    pprint(projects)
except Exception as error:
    pprint(error)

# Get current date
now = datetime.now()

# Find overdue tasks and create follow-up tasks
try:
    tasks = api.get_tasks(project_id='project_id')
    for task in tasks:
        task_time = datetime.strptime(task.due.datetime, '%Y-%m-%dT%H:%M:%S')
        if task_time > now:
            pass
            # print('The datetime in the string is in the future.')
        else:
            print('The datetime in the string is in the past or present.')
            api.add_task(
                content=f"{task.content} failed",
                due_string="today",
                due_lang="en",
                priority=4,
            )
            api.close_task(task_id=task.id)
        # print()
        # if task.due.datetime is None:
        #     print(task.due.date)
        #     if task.due.date
        # if task.due.date
    # pprint(tasks)
except Exception as error:
    pprint(error)

# Commit the changes to Todoist
print()