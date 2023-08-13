import tkinter as tk
import random

# Constants
WIDTH = 400
HEIGHT = 400
UNIT_SIZE = 20
DELAY = 100  # in milliseconds

class SnakeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.food = self.generate_food()

        self.root.bind("<Key>", self.on_key_press)
        self.game_loop()

    def generate_food(self):
        x = random.randint(0, (WIDTH - UNIT_SIZE) // UNIT_SIZE) * UNIT_SIZE
        y = random.randint(0, (HEIGHT - UNIT_SIZE) // UNIT_SIZE) * UNIT_SIZE
        return x, y

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Right":
            new_head = (head_x + UNIT_SIZE, head_y)
        elif self.direction == "Left":
            new_head = (head_x - UNIT_SIZE, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - UNIT_SIZE)
        else:
            new_head = (head_x, head_y + UNIT_SIZE)

        self.snake = [new_head] + self.snake[:-1]

    def check_collision(self):
        head_x, head_y = self.snake[0]
        if (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
            or self.snake[0] in self.snake[1:]
        ):
            return True
        return False

    def on_key_press(self, event):
        new_direction = event.keysym
        if (
            new_direction == "Up" and self.direction != "Down"
            or new_direction == "Down" and self.direction != "Up"
            or new_direction == "Left" and self.direction != "Right"
            or new_direction == "Right" and self.direction != "Left"
        ):
            self.direction = new_direction

    def game_loop(self):
        if self.check_collision():
            self.canvas.create_text(
                WIDTH / 2, HEIGHT / 2, text="Game Over", font=("Helvetica", 24)
            )
            return

        self.move_snake()

        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.generate_food()

        self.canvas.delete("all")
        self.canvas.create_rectangle(
            self.food[0],
            self.food[1],
            self.food[0] + UNIT_SIZE,
            self.food[1] + UNIT_SIZE,
            fill="red",
        )

        for segment in self.snake:
            self.canvas.create_rectangle(
                segment[0],
                segment[1],
                segment[0] + UNIT_SIZE,
                segment[1] + UNIT_SIZE,
                fill="green",
            )

        self.root.after(DELAY, self.game_loop)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
