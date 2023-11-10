class Task:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
        self.is_done = False

    def __str__(self):
        return f"--------------------\nTitle: {self.title}\nDescription: {self.desc}\nIs Done: {self.is_done}\n--------------------\n"


class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        if task not in self.task_list:
            self.task_list.append(task)
            return "Task added successfully!\n"
        else:
            return "Task is already in the list...\n"

    def display_tasks(self):
        for idx, task in enumerate(self.task_list, start=1):
            print(f"Task {idx}")
            print(task)

    def mark_as_done(self, index):
        if 0 <= index < len(self.task_list):
            task = self.task_list[index]
            if not task.is_done:
                confirmation = input(f"Mark '{task.title}' as done? (yes/no): ").lower()
                if confirmation == 'yes':
                    task.is_done = True
                    print("Task Completed!\n")
                else:
                    print("Task not marked as done.\n")
            else:
                print("Task is already marked as done.\n")
        else:
            print("Invalid index. Please try again.\n")


def display_menu():
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Done")
    print("4. Exit Task Manager\n")


def main():
    task_manager = TaskManager()

    while True:
        try:
            display_menu()
            choice = int(input("Enter Choice: "))

            if choice == 1:
                task_title = input("Enter Task Title: ").lower()
                task_desc = input("Enter Task Description: ").lower()
                print()
                task = Task(task_title, task_desc)
                result = task_manager.add_task(task)
                print(result)

            elif choice == 2:
                print("\nDisplaying Tasks...\n")
                task_manager.display_tasks()

            elif choice == 3:
                print("Indexes: [", end=" ")
                for idx, _ in enumerate(task_manager.task_list):
                    print(idx, end=" ")
                print("]\n")
                index = int(input("Enter Task Index Number: "))
                task_manager.mark_as_done(index)

            elif choice == 4:
                print("Closing Task Manager...\n")
                break

            else:
                print("Invalid Input. Please try again.\n")

        except ValueError:
            print("Input must be an integer...\n")


if __name__ == "__main__":
    main()
