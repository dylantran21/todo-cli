# To-Do CLI App

A simple, command-line to-do list application written in Python. Practice with file I/O, command-line argument parsing, and basic version control.

## 🚀 Features

- **List** tasks with status icons (✅/❌):
```bash
todo.py list
```

- **Add** task to the end of the list:
```bash
todo.py add "Buy groceries"
```

* **Delete** task by index:
```bash
todo.py delete 3
```

* **Mark** task as done:
```bash
todo.py done 2
```

## 🛠️ Setup & Installation

1. Clone the repository
    ```bash
    git clone git@github.com:dylantran21/todo-cli.git
    cd todo-cli
    ```
2. Ensure Python 3 is installed
    * On macOS/Linux: likely already installed

    * On Windows, use the py launcher or install from python.org

## ▶️ Usage

* **List** tasks
```bash
#macOS/Linux
./todo.py list

#Windows (PowerShell)
python todo.py list
```

* **Add** a new task
```bash
python todo.py add "Finish writing README"
```

* **Delete** a task
```bash
python todo.py delete 1
```

* **Mark** a task as done
```bash
python todo.py done 1
```

## 📂 Data File
All tasks are stored in `tasks.json` in the project root. It’s initialized to an empty list (`[]`) when you first run the script.

## 📖 What I Learned
* argparse for building multi-command CLIs with subparsers

* JSON file handling (`json.load` / `json.dump`) for simple persistence

* File-existence checks and basic error handling in Python

* Version control: structured commits, meaningful messages, and pushing to GitHub

## 🔮 Future Improvements
* Add due dates and priority levels for tasks

* Support editing existing task descriptions

* Implement a search/filter command (`todo.py search "keyword"`)

* Package as an installable module with `pip` and entry-point

## 📜 License
This project is licensed under the [MIT License](LICENSE). 