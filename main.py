        list_frame = tk.Frame(self.root, bg=self.bg_color)
        list_frame.pack(pady=15, padx=20, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.task_listbox = tk.Listbox(
            list_frame, font=("Tahoma", 11), bg=self.card_color,
            fg=self.text_color, selectbackground="#334155",
            selectforeground="white", relief=tk.FLAT, bd=0,
            highlightthickness=0, yscrollcommand=scrollbar.set,
            justify="right"
        )
        self.task_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_listbox.yview)
