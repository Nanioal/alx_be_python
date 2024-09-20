task = input("Enter a task description: ")

priority = input("Enter the task's priority (high, medium, low): ").lower()

time_bound = input("Is the task time-bound (yes or no)? ").lower()


match priority:
    case "high":
        reminder = f"{task} is a high priority task"
    case "medium":
        reminder = f"{task} is a medium priority task. Consider completing it when you have space to do so"
    case "low":
        reminder = f"{task} is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"{task} Priority is Unknown"


if time_bound == "yes":
    reminder += " that requires immediate attention today!"


print(reminder)
