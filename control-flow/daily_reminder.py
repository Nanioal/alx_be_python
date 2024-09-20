task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()

Reminder = ""
note = ""

match priority:
    case "high":
        Reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        Reminder = f"Reminder: '{task}' is a medium priority task."
        note = f"Reminder: '{task}' is a medium priority task."
    case "low":
        Reminder = f"Reminder: '{task}' is a low priority task."
        note = f"Note: '{task}' is a low priority task."
    case _:
        Reminder = f"Reminder: '{task}' Priority is Unknown."

if time_bound == "yes":
    Reminder += " that requires immediate attention today!"
    print(Reminder)
elif time_bound == "no":
    note += " Consider completing it when you have free time."
    print(note)
