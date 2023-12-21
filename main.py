import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import os

class EnchantmentLearningApp:
    def __init__(self, root, image_folder):
        self.root = root
        self.image_folder = image_folder
        self.score = 0
        self.image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]
        self.current_image = None

        # Setting up the GUI
        self.root.title("Minecraft Enchantment Learning")
        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_image)
        self.next_button.pack()

        # Start the game
        self.next_image()

    def next_image(self):
        if self.current_image:
            user_answer = simpledialog.askstring("Input", "What letter is this?", parent=self.root)
            correct_answer = self.current_image[:-4]  # Remove .png extension
            if correct_answer == "dot":
                correct_answer = "."
            if user_answer and user_answer.lower() == correct_answer:
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
            else:
                messagebox.showinfo("Wrong Answer", f"Wrong! The correct answer was '{correct_answer}'.")

        random_image = random.choice(self.image_files)
        self.current_image = random_image
        img_path = os.path.join(self.image_folder, random_image)
        photo = tk.PhotoImage(file=img_path)
        self.image_label.config(image=photo)
        self.image_label.image = photo  # Keep a reference

def main():
    root = tk.Tk()
    app = EnchantmentLearningApp(root, "assets")  # Replace with your image folder path
    root.mainloop()

# Run the app
if __name__ == "__main__":
    main()
