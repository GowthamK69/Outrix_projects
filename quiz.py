import tkinter as tk
from tkinter import messagebox
import random

# ----------------------------
# GOATED QUIZ DATA
# ----------------------------
questions = [
    {
        "q": "Which data structure uses FIFO?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue"
    },
    {
        "q": "Which language runs in the browser?",
        "options": ["Python", "C++", "JavaScript", "Java"],
        "answer": "JavaScript"
    },
    {
        "q": "What does CPU stand for?",
        "options": [
            "Central Process Unit",
            "Control Processing Unit",
            "Central Processing Unit",
            "Compute Process Utility"
        ],
        "answer": "Central Processing Unit"
    },
    {
        "q": "Which is a Python web framework?",
        "options": ["Django", "Laravel", "Spring", "Rails"],
        "answer": "Django"
    },
    {
        "q": "Who founded Microsoft?",
        "options": ["Steve Jobs", "Bill Gates", "Jeff Bezos", "Elon Musk"],
        "answer": "Bill Gates"
    }
]

random.shuffle(questions)

# ----------------------------
# MAIN QUIZ CLASS
# ----------------------------
class QuizGUI:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.index = 0

        root.title("GOATED NEON QUIZ")
        root.geometry("600x500")
        root.configure(bg="black")

        # Title
        self.title = tk.Label(
            root,
            text="🧠 GOATED QUIZ APP",
            font=("Arial", 22, "bold"),
            fg="#00E1FF",
            bg="black"
        )
        self.title.pack(pady=20)

        # Question Box
        self.question_label = tk.Label(
            root,
            text="",
            font=("Arial", 16),
            wraplength=500,
            fg="white",
            bg="black"
        )
        self.question_label.pack(pady=30)

        # Option Buttons
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(
                root,
                text="",
                font=("Arial", 14, "bold"),
                bg="#101820",
                fg="#00E1FF",
                activebackground="#00E1FF",
                activeforeground="black",
                width=30,
                bd=0,
                relief="flat",
                highlightthickness=2,
                highlightcolor="#00E1FF"
            )
            btn.pack(pady=8)
            self.option_buttons.append(btn)

        self.load_question()

    # Load next question
    def load_question(self):
        if self.index >= len(questions):
            self.end_quiz()
            return

        q_data = questions[self.index]
        self.question_label.config(text=f"Q{self.index+1}: {q_data['q']}")

        for i, opt in enumerate(q_data["options"]):
            self.option_buttons[i].config(
                text=opt,
                command=lambda selected=opt: self.check_answer(selected)
            )

    # Answer checking
    def check_answer(self, selected):
        correct = questions[self.index]["answer"]
        if selected == correct:
            self.score += 1

        self.index += 1
        self.load_question()

    # Quiz end screen
    def end_quiz(self):
        for btn in self.option_buttons:
            btn.pack_forget()

        self.question_label.config(
            text=f"🎉 Quiz Completed!\n\nYour Score: {self.score}/{len(questions)}",
            font=("Arial", 18, "bold")
        )

        retry = tk.Button(
            self.root,
            text="Restart Quiz",
            font=("Arial", 16, "bold"),
            bg="#00E1FF",
            fg="black",
            width=20,
            command=self.restart_quiz
        )
        retry.pack(pady=30)

    # Restart quiz
    def restart_quiz(self):
        self.score = 0
        self.index = 0
        random.shuffle(questions)

        for btn in self.option_buttons:
            btn.pack(pady=8)

        self.load_question()


# ----------------------------
# RUN APP
# ----------------------------
root = tk.Tk()
app = QuizGUI(root)
root.mainloop()
