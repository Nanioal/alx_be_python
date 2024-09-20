# Prompt the user to enter a task description
task = input("Enter a task description: ")

# Prompt the user to enter the task's priority
priority = input("Enter the task's priority (high, medium, low): ").lower()

# Prompt the user to enter if the task is time-bound
time_bound = input("Is the task time-bound (yes or no)? ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"{task} is a high priority task"
    case "medium":
        reminder = f"{task} is a medium priority task. Consider completing it when you have space to do so"
    case "low":
        reminder = f"{task} is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"{task} Priority is Unknown"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the customized reminder
print(reminder)
