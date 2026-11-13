        header_label = tk.Label(
            self.root, text="مدیریت وظایف روزانه",
            font=("Tahoma", 15, "bold"), bg=self.bg_color, fg=self.text_color
        )
        header_label.pack(pady=(20, 15))

        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(pady=5, padx=20, fill=tk.X)

        self.add_btn = tk.Button(
            input_frame, text="افزودن +", command=self.add_task,
            bg=self.accent_color, fg="white", font=("Tahoma", 10, "bold"),
            relief=tk.FLAT, padx=14, pady=6, cursor="hand2"
        )
        self.add_btn.pack(side=tk.LEFT, padx=(0, 8))

        self.task_entry = tk.Entry(
            input_frame, font=("Tahoma", 11), bg=self.card_color,
            fg=self.text_color, insertbackground="white", relief=tk.FLAT,
            justify="right"
        )
        self.task_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True, ipady=6, ipadx=8)
        self.task_entry.bind("<Return>", lambda event: self.add_task())
