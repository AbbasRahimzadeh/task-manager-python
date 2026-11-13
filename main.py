 def load_tasks(self):
        if os.path.exists(FILENAME):
            with open(FILENAME, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=4)

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            status_icon = "✅" if task["completed"] else "⏳"
            display_text = f" {task['title']}  {status_icon} "
            self.task_listbox.insert(tk.END, display_text)
            if task["completed"]:
                self.task_listbox.itemconfig(idx, fg=self.muted_color)

    def add_task(self):
        title = self.task_entry.get().strip()
        if not title:
            messagebox.showwarning("هشدار", "لطفاً عنوان وظیفه را وارد کنید.")
            return
        self.tasks.append({"title": title, "completed": False})
        self.save_tasks()
        self.task_entry.delete(0, tk.END)
        self.refresh_listbox()

    def toggle_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("راهنما", "لطفاً یک وظیفه را از لیست انتخاب کنید.")
            return
        idx = selected[0]
        self.tasks[idx]["completed"] = not self.tasks[idx]["completed"]
        self.save_tasks()
        self.refresh_listbox()

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("راهنما", "لطفاً وظیفه‌ای که می‌خواهید حذف شود را انتخاب کنید.")
            return
        idx = selected[0]
        del self.tasks[idx]
        self.save_tasks()
        self.refresh_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
