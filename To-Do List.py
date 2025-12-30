import tkinter as tk
from tkinter import messagebox
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
        self.tasks = []
        title = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"))
        title.pack(pady=10)
        self.task_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.task_entry.pack(pady=10)
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)
        add_btn = tk.Button(button_frame, text="Add Task", width=12, command=self.add_task)
        add_btn.grid(row=0, column=0, padx=5)
        done_btn = tk.Button(button_frame, text="Mark Done", width=12, command=self.mark_done)
        done_btn.grid(row=0, column=1, padx=5)
        delete_btn = tk.Button(button_frame, text="Delete Task", width=12, command=self.delete_task)
        delete_btn.grid(row=1, column=0, columnspan=2, pady=5)
        self.task_listbox = tk.Listbox(
            root,
            width=45,
            height=15,
            font=("Arial", 11),
            selectbackground="lightblue"
        )
        self.task_listbox.pack(pady=10)
    def add_task(self):
        task = self.task_entry.get().strip()
        if task == "":
            messagebox.showwarning("Warning", "Task cannot be empty!")
            return
        self.tasks.append(task)
        self.task_listbox.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)
    def mark_done(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(index)
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, f"✔ {task}")
        except IndexError:
            messagebox.showinfo("Info", "Please select a task first.")
    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
        except IndexError:
            messagebox.showinfo("Info", "Please select a task to delete.")
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

