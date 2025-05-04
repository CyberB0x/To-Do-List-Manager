# To-Do List Manager

Это простое приложение для управления задачами с использованием Python и MySQL. Приложение позволяет добавлять, просматривать и удалять задачи.

## Требования

- Python 3.x
- MySQL
- Библиотеки:
  - `mysql-connector-python`
  - `dotenv`

## Установка

### 1. Клонируйте репозиторий

Скачайте или клонируйте репозиторий на свой компьютер:

```bash
git clone https://github.com/ваш_репозиторий/To-Do-List-Manager.git

```
# 2. Создайте и активируйте виртуальное окружение
python -m venv venv

Активируйте виртуальное окружение:
Для Windows:
venv\\Scripts\\activate

Для MacOS/Linux:
source venv/bin/activate

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Настройка MySQL
4.1 Создайте базу данных
Для начала нужно создать базу данных. Запустите MySQL и выполните следующий запрос:
CREATE DATABASE user_task_db;

# 4.2 Создайте таблицу
Запустите следующий SQL запрос для создания таблицы tasks:
```
USE user_task_db;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

# 5. Настройка окружения
Создайте файл .env в корне проекта и добавьте в него следующие строки:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=user_task_db
```

# 6. Запуск проекта
python -m app.main

# 7. Использование
После запуска приложения вы можете добавлять, удалять и просматривать задачи. Вот доступные команды:
Добавить задачу: Введите описание задачи.
Просмотр задач: Все задачи будут отображены в консоли.
Удалить задачу: Укажите ID задачи для удаления.

# Структура проекта
```
To-Do-List-Manager/
├── app/
│   ├── main.py           # Основной файл приложения
│   ├── models.py         # Логика для работы с задачами (добавление, удаление, получение)
│   └── __init__.py       # Инициализация приложения
├── db/
│   ├── connection.py     # Настройки подключения к базе данных
│   └── __init__.py       # Инициализация базы данных
├── .env                  # Конфигурация окружения
├── requirements.txt      # Список зависимостей
└── README.md             # Документация проекта
```

# Зависимости
Проект использует следующие библиотеки:

mysql-connector-python — для работы с MySQL.

python-dotenv — для загрузки переменных окружения из файла .env.

Чтобы установить все зависимости, используйте команду:
pip install -r requirements.txt

