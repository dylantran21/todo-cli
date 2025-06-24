#!/usr/bin/env python3
import argparse, json, os   

FILE_NAME = "tasks.json"    #constant variable for ease of change of file 

def load_tasks(): 
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:    #checks if the file exits 
        return []                               #returns an empty list
    with open(FILE_NAME, "r") as opened_file:   #opens the file to be read
        return json.load(opened_file)           #returns the contents of the file

def save_tasks(tasks): 
    with open(FILE_NAME, "w") as opened_file:   #opens the file to be edited
        json.dump(tasks, opened_file, indent=2) #formats and saves the contents of the file

def list_tasks():
    tasks = load_tasks()  
    if not tasks:                               #checks if the file is empty or doesn't exist
        print("There are no tasks.")   
        return
    for i, task in enumerate(tasks, 1):         #iterates through the tasks while assigning 1 as the base index     
        if task["done"]:                        #checks if task is done or not and assigns an icon for either
            status = "✅"
        else:
            status = "❌"
        print(f"{i}. {task['task']} {status}")  #prints formated task

def add_task(description):
    tasks = load_tasks() 
    tasks.append({"task": description, "done": False})  #appends the task list with the new task
    save_tasks(tasks)                                   #saves the newly appended list
    print(f"New task successfully added!")

def mark_done(index):
    tasks = load_tasks() 
    if 0 <= index-1 < len(tasks):               #checks if the index exists
        tasks[index-1]["done"] = True           #changes the value of the key "done" from False to True
        save_tasks(tasks)                       #save changes to the file
        print(f"{tasks[index-1]['task']} ✅")
    else:
        print("Invalid task number")
    
def delete_task(index):
    tasks = load_tasks() 
    if 0 <= index-1 < len(tasks):                   #checks if the index exists
        deleted_task = tasks.pop(index-1)           #stores the entry then deletes it
        save_tasks(tasks)                           #save changes to the file
        print(f"Deleted: {deleted_task['task']}")
    else:
        print("Invalid task number")

def main():
    parser = argparse.ArgumentParser(description="ToDo CLI")    #object to enable cli
    sub = parser.add_subparsers(dest="command")                 #object to enable the creation of commands

    sub.add_parser("list", help="list tasks")                                                                               #adds command for showing the list of tasks
    sub.add_parser("add", help="Add a task").add_argument("description", help="Task description")                           #adds command for adding a task 
    sub.add_parser("done", help="Mark a task as finished").add_argument("index", type=int, help="Task number to be marked") #adds command for marking a task as finished 
    sub.add_parser("delete", help="Delete a task").add_argument("index", type=int, help="Task number to be deleted")        #adds command for deleting a task

    args = parser.parse_args()

    #defines the affect of the commands
    if args.command == "list":
        list_tasks()
    elif args.command == "add":
        add_task(args.description)
    elif args.command == "done":
        mark_done(args.index)
    elif args.command == "delete":
        delete_task(args.index)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
