class ToDoList:
    def __init__(self):
        self.tasks=dict()
    def addTask(self,task):
        self.tasks[len(self.tasks) + 1]=task
        print("The task has been added successfully")
    def viewTasks(self):
        if not self.tasks:
            print('No tasks found. Add some tasks first.')
        else:        
            for i,j in self.tasks.items():
                print("{}.{}".format(i,j))
    def removeTask(self, index):
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index)
            print('Task "{}" removed successfully.'.format(removed_task))                
        else:
            print('Invalid task index.')
                
def main():
    todoList=ToDoList()
    def displayOptions():
        print("1. Add task")
        print("2. View task")
        print("3. Remove task")
        print("4. Exit")
    while True:
        displayOptions()
        choice=int(input("Enter your choice 1/2/3/4\n"))
        if choice==1:
                task=input("Enter the task\n")
                todoList.addTask(task)
        elif choice==2:
                todoList.viewTasks()
        elif choice==3:
                index=int(input("Enter the index of the task to remove\n"))
                todoList.removeTask(index)
        elif choice==4:
                print('Exiting the to-do list app. Goodbye!')
                break
        else:
            print("invalid input")
                
if __name__ == "__main__":
    main()
