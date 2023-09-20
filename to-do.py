import tkinter as tk
from tkinter import messagebox


class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_label = tk.Label(root, text="Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.add_button = tk.Button(
            root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.tasks_listbox.pack()

        self.update_button = tk.Button(
            root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.remove_button = tk.Button(
            root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.populate_listbox()

    def populate_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.populate_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task.")

    def update_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_index[0]] = new_task
                self.populate_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please enter a task.")
        else:
            messagebox.showerror("Error", "Please select a task to update.")

    def remove_task(self):
        selected_indices = self.tasks_listbox.curselection()
        if selected_indices:
            # Reverse to avoid index shifting
            selected_indices = sorted(selected_indices, reverse=True)
            for index in selected_indices:
                del self.tasks[index]
            self.populate_listbox()
        else:
            messagebox.showerror("Error", "Please select a task to remove.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()