        btn_frame = tk.Frame(self.root, bg=self.bg_color)
        btn_frame.pack(pady=(0, 20), padx=20, fill=tk.X)

        self.complete_btn = tk.Button(
            btn_frame, text="تغییر وضعیت (انجام شد / نشد) ✔", command=self.toggle_task,
            bg=self.success_color, fg="white", font=("Tahoma", 10, "bold"),
            relief=tk.FLAT, pady=8, cursor="hand2"
        )
        self.complete_btn.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))

        self.delete_btn = tk.Button(
            btn_frame, text="حذف وظیفه 🗑", command=self.delete_task,
            bg=self.danger_color, fg="white", font=("Tahoma", 10, "bold"),
            relief=tk.FLAT, pady=8, cursor="hand2"
        )
        self.delete_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
