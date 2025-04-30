import tkinter as tk
from tkinter import ttk, colorchooser
from datetime import datetime, timedelta


class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Managment App")
        self.root.configure(bg="#000000")

        self.lists = []
        self.tasks = {}

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.add_list_button = tk.Button(
            self.root, text="+", command=self.add_list, bg="#000000", fg="#FFFFFF")
        self.add_list_button.pack()

    def add_list(self):
        list_frame = tk.Frame(self.notebook, bg="#000000")
        self.notebook.add(
            list_frame, text="Lista {}".format(len(self.lists) + 1))

        self.lists.append(list_frame)

        task_frame = tk.Frame(list_frame, bg="#000000")
        task_frame.pack(fill="both", expand=True)

        task_list = tk.Frame(task_frame, bg="#000000")
        task_list.pack(fill="both", expand=True)

        add_task_button = tk.Button(
            task_frame, text="+", command=lambda: self.add_task(task_list), bg="#000000", fg="#FFFFFF")
        add_task_button.pack()

        self.tasks[list_frame] = []

    def add_task(self, task_list):
        task_frame = tk.Frame(task_list, bg="#000000")
        task_frame.pack(fill="x")

        task_label = tk.Label(task_frame, text="⭕", bg="#000000", fg="#FFFFFF")
        task_label.pack(side="left")

        task_entry = tk.Entry(task_frame, bg="#333333", fg="#FFFFFF")
        task_entry.pack(side="left", fill="x", expand=True)

        task_color_button = tk.Button(task_frame, text="", command=lambda: self.change_task_color(
            task_entry), bg="#000000", fg="#FFFFFF", width=2)
        task_color_button.pack(side="left")

        task_checkbox = tk.BooleanVar()
        task_checkbox_button = tk.Checkbutton(task_frame, variable=task_checkbox, command=lambda: self.task_checkbox_clicked(
            task_checkbox, task_frame), bg="#000000", fg="#FFFFFF", selectcolor="#000000")
        task_checkbox_button.pack(side="left")

        task_deadline_label = tk.Label(
            task_frame, text="Deadline:", bg="#000000", fg="#FFFFFF")
        task_deadline_label.pack(side="left")

        task_deadline_entry = tk.Entry(
            task_frame, bg="#333333", fg="#FFFFFF", width=10)
        task_deadline_entry.pack(side="left")

        task_repeat_label = tk.Label(
            task_frame, text="Repeat:", bg="#000000", fg="#FFFFFF")
        task_repeat_label.pack(side="left")

        task_repeat_var = tk.StringVar()
        task_repeat_var.set("None")
        task_repeat_option = tk.OptionMenu(
            task_frame, task_repeat_var, "None", "Daily", "Weekly")
        task_repeat_option.pack(side="left")

        self.tasks[task_list.master].append(
            (task_entry, task_checkbox, task_deadline_entry, task_repeat_var))

    def change_task_color(self, task_entry):
        color = colorchooser.askcolor()[1]
        if color:
            task_entry.config(bg=color)

    def task_checkbox_clicked(self, task_checkbox, task_frame):
        if task_checkbox.get():
            for widget in task_frame.winfo_children():
                widget.config(state="disabled")
            task_frame.config(bg="#FFFFFF")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    app.run()
