import tkinter as tk
import random
user_score = 0
computer_score = 0
def play(user_choice):
    global user_score, computer_score
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    user_choice_label.config(text="Your Choice: " + user_choice)
    computer_choice_label.config(text="Computer Choice: " + computer_choice)
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(
        text=f"Score → You: {user_score}  Computer: {computer_score}"
    )
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")
root.resizable(False, False)
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
title.pack(pady=10)
instruction = tk.Label(
    root,
    text="Choose one option to play",
    font=("Arial", 11)
)
instruction.pack()
button_frame = tk.Frame(root)
button_frame.pack(pady=15)
rock_btn = tk.Button(button_frame, text="Rock", width=10,
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)
paper_btn = tk.Button(button_frame, text="Paper", width=10,
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn = tk.Button(button_frame, text="Scissors", width=10,
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)
user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 11))
user_choice_label.pack(pady=5)
computer_choice_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 11))
computer_choice_label.pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)
score_label = tk.Label(
    root,
    text="Score → You: 0  Computer: 0",
    font=("Arial", 11)
)
score_label.pack(pady=5)
root.mainloop()

