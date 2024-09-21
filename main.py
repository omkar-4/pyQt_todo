import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox, QInputDialog

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadTasks()

    def initUI(self):
        self.setWindowTitle('ToDo App')
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.taskInput = QLineEdit(self)
        self.layout.addWidget(self.taskInput)

        self.taskList = QListWidget(self)
        self.layout.addWidget(self.taskList)

        self.buttonLayout = QHBoxLayout()

        self.addButton = QPushButton('Add Task', self)
        self.addButton.clicked.connect(self.addTask)
        self.buttonLayout.addWidget(self.addButton)

        self.updateButton = QPushButton('Update Task', self)
        self.updateButton.clicked.connect(self.updateTask)
        self.buttonLayout.addWidget(self.updateButton)

        self.deleteButton = QPushButton('Delete Task', self)
        self.deleteButton.clicked.connect(self.deleteTask)
        self.buttonLayout.addWidget(self.deleteButton)

        self.layout.addLayout(self.buttonLayout)
        self.setLayout(self.layout)

    def addTask(self):
        task = self.taskInput.text()
        if task:
            self.taskList.addItem(task)
            self.taskInput.clear()
            self.saveTasks()

    def updateTask(self):
        selectedTask = self.taskList.currentItem()
        if selectedTask:
            newTask, ok = QInputDialog.getText(self, 'Update Task', 'Edit task:', QLineEdit.Normal, selectedTask.text())
            if ok and newTask:
                selectedTask.setText(newTask)
                self.saveTasks()

    def deleteTask(self):
        selectedTask = self.taskList.currentItem()
        if selectedTask:
            self.taskList.takeItem(self.taskList.row(selectedTask))
            self.saveTasks()

    def saveTasks(self):
        tasks = []
        for index in range(self.taskList.count()):
            tasks.append(self.taskList.item(index).text())
        with open('tasks.txt', 'w') as file:
            for task in tasks:
                file.write(task + '\n')

    def loadTasks(self):
        if os.path.exists('tasks.txt'):
            with open('tasks.txt', 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    self.taskList.addItem(task.strip())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todoApp = ToDoApp()
    todoApp.show()
    sys.exit(app.exec_())
