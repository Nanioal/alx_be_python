# Prompt the user to enter a task description
task = input("Enter a task description: ")

# Prompt the user to enter the task's priority
priority = input("Enter the task's priority (high, medium, low): ").lower()

# Prompt the user to enter if the task is time-bound
time_bound = input("Is the task time-bound (yes or no)? ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"Task: {task} - Priority: High"
    case "medium":
        reminder = f"Task: {task} - Priority: Medium"
    case "low":
        reminder = f"Task: {task} - Priority: Low"
    case _:
        reminder = f"Task: {task} - Priority: Unknown"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the customized reminder
print(reminder)
