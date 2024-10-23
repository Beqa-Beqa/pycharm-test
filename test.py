# # Task list
# task_list = []
#
# while True:
#     # Constants
#     ADD_TASK = 1
#     REMOVE_TASK = 2
#     UPDATE_TASK = 3
#     VIEW_ALL_TASKS = 4
#     VIEW_COMPLETED_TASKS = 5
#     MARK_AS_COMPLETED = 6
#     EXIT = 7
#
#     FIRST_CHOICE = ADD_TASK
#     LAST_CHOICE = EXIT
#
#     FIRST_TASK_INDEX = 0
#
#     menu_choice = input("""1. Add a task
# 2. Remove a task
# 3. Update a task
# 4. View all tasks
# 5. View completed tasks
# 6. Mark a task as completed
# 7. Exit
#
# >>> """)
#
#     # Get the value which can be cast into an integer
#     try:
#         menu_choice = int(menu_choice)
#     except ValueError:
#         print('Enter a proper digit value!')
#         continue
#
#     # If choice is out of range
#     if menu_choice < FIRST_CHOICE or menu_choice > LAST_CHOICE:
#         print('Action out of range!')
#         continue
#
#     # If choice is to exit program
#     if menu_choice == EXIT:
#         print('Quitting the program!')
#         break
#
#     # If choice is to add task
#     if menu_choice == ADD_TASK:
#         task_description = input('Enter task description: ')
#
#         task = {
#             'description': task_description,
#             'completed': False
#         }
#
#         task_list.append(task)
#
#         continue
#
#
#     # Utility function
#     def get_task_index():
#         # While task_index is not type of integer
#         while True:
#             try:
#                 task_index = int(input('Enter task index: '))
#                 break
#
#             except ValueError:
#                 print('Enter proper index!')
#
#         return task_index
#
#
#     # If choice is to remove task
#     if menu_choice == REMOVE_TASK:
#         task_index = get_task_index()
#
#         if FIRST_TASK_INDEX <= task_index < len(task_list):
#             task_list.pop(task_index)
#             print('Task removed successfully!')
#         else:
#             print(f'Task with index {task_index} does not exist!')
#
#         continue
#
#     # If choice is to update task description
#     if menu_choice == UPDATE_TASK:
#         task_index = get_task_index()
#
#         if FIRST_TASK_INDEX <= task_index < len(task_list):
#             new_description = input('Enter new task description: ')
#             task_list[task_index]['description'] = new_description
#         else:
#             print(f'Task with index {task_index} does not exist!')
#
#         continue
#
#     # If choice is to view all tasks
#     if menu_choice == VIEW_ALL_TASKS:
#         for task_idx in range(len(task_list)):
#             current_task = task_list[task_idx]
#             print(f"({task_idx}) | Description: {current_task['description']} | is complete: {current_task['completed']}")
#
#         continue
#
#     # If choice is to view completed tasks only
#     if menu_choice == VIEW_COMPLETED_TASKS:
#         tasks_completed = list(filter(lambda task: task['completed'] == True, task_list))
#
#         for task_idx in range(len(tasks_completed)):
#             current_task = tasks_completed[task_idx]
#             print(f"({task_idx}) | Description: {current_task['description']} | is complete: {current_task['completed']}")
#
#         continue
#
#     # If choice is to mark the task as completed
#     if menu_choice == MARK_AS_COMPLETED:
#         task_index = get_task_index()
#
#         if FIRST_TASK_INDEX <= task_index < len(task_list):
#             task_list[task_index]['completed'] = True
#             print('Task marked as completed successfully!')
#         else:
#             print(f'Task with index {task_index} does not exist!')
#
#         continue

new_list = [1, 2, 3, 4, 5]
