from app.models import add_task, get_all_tasks, delete_task

def main():
    while True:
        print("\n=== Меню ===")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Удалить задачу")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            description = input("Введите описание задачи: ")
            add_task(description)
            print("Задача добавлена!")
        elif choice == "2":
            tasks = get_all_tasks()
            if tasks:
                print("\nВаш список задач:")
                for task in tasks:
                    print(f"{task[0]}. {task[1]}")
            else:
                print("Список задач пуст.")
        elif choice == "3":
            task_id = input("Введите ID задачи для удаления: ")
            delete_task(task_id)
            print("Задача удалена.")
        elif choice == "4":
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
