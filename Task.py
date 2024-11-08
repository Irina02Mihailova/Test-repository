class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"{self.description} (Срок выполнения задачи: {self.due_date}) - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Задача с таким индексом не найдена.")

    def list_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if not current_tasks:
            print("Нет текущих задач.")
        else:
            for index, task in enumerate(current_tasks):
                print(f"{index}. {task}")


task_manager = TaskManager()
task_manager.add_task("Посмотреть видеоурок", "08.11.2024")
task_manager.add_task("Выполнить домашнее задание", "20.11.2024")
task_manager.add_task("Отправить домашнее задание на проверку", "20.11.2024")
task_manager.add_task("Потренироваться решать задачи по предыдущим темам", "07.11.2024")

print("Список текущих задач:")
task_manager.list_current_tasks()

task_manager.mark_task_completed(0)
task_manager.mark_task_completed(3)

print("\nОбновленный список текущих задач:")
task_manager.list_current_tasks()
