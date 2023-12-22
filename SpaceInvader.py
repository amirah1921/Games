import tkinter as tk
import random

class SpaceInvaders:
    def __init__(self, master):
        self.master = master
        self.master.title("Space Invaders")
        self.master.geometry("600x450")

        self.canvas = tk.Canvas(self.master, width=600, height=400, bg='black')
        self.canvas.pack()

        self.score_label = tk.Label(self.master, text="Score: 0", font=("Helvetica", 16), fg='black')
        self.score_label.pack(pady=10)

        self.player = self.canvas.create_rectangle(250, 350, 350, 370, fill='blue')
        self.enemies = []
        self.score = 0

        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<space>", self.shoot)

        self.spawn_enemies()
        self.animate()

    def update_score_label(self):
        self.score_label.config(text=f"Score: {self.score}")

    def spawn_enemies(self):
        for _ in range(5):
            x = random.randint(50, 550)
            y = random.randint(50, 150)
            enemy = self.canvas.create_rectangle(x, y, x + 20, y + 20, fill='red')
            self.enemies.append(enemy)

    def move_left(self, event):
        if self.canvas.coords(self.player)[0] > 0:
            self.canvas.move(self.player, -20, 0)

    def move_right(self, event):
        if self.canvas.coords(self.player)[2] < 600:
            self.canvas.move(self.player, 20, 0)

    def shoot(self, event):
        x, y, _, _ = self.canvas.coords(self.player)
        bullet = self.canvas.create_rectangle(x + 7, y - 10, x + 13, y, fill='yellow')
        self.move_bullet(bullet)

    def move_bullet(self, bullet):
        if self.canvas.coords(bullet)[1] > 0:
            self.canvas.move(bullet, 0, -10)
            self.check_collision(bullet)
            self.master.after(50, lambda: self.move_bullet(bullet))
        else:
            self.canvas.delete(bullet)

    def check_collision(self, bullet):
        bullet_coords = self.canvas.coords(bullet)
        for enemy in self.enemies:
            enemy_coords = self.canvas.coords(enemy)
            if (enemy_coords[0] < bullet_coords[2] < enemy_coords[2] and
                    enemy_coords[1] < bullet_coords[1] < enemy_coords[3]):
                self.score += 10
                self.canvas.delete(enemy)
                self.enemies.remove(enemy)
                self.canvas.delete(bullet)
                self.spawn_enemies()
                self.update_score_label()
                break

    def animate(self):
        for enemy in self.enemies:
            self.canvas.move(enemy, random.choice([-5, 5]), 0)
            enemy_coords = self.canvas.coords(enemy)
            if enemy_coords[0] < 0 or enemy_coords[2] > 600:
                self.canvas.move(enemy, -enemy_coords[0] + 5, 0)

        self.master.after(100, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    game = SpaceInvaders(root)
    root.mainloop()
