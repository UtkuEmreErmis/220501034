import tkinter as tk
import random


class BouncingBallsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bouncing Balls")
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        # Kullanıcı seçenekleri
        self.size_var = tk.IntVar(value=20)  # Varsayılan boyut
        self.color_var = tk.StringVar(value="red")  # Varsayılan renk

        # Kontrol paneli
        control_frame = tk.Frame(root)
        control_frame.pack()

        # Boyut Seçenekleri (Örnek görsellerle)
        tk.Label(control_frame, text="Boyut:").pack(side="left")
        for size in [20, 30, 40]:
            frame = tk.Frame(control_frame)
            frame.pack(side="left", padx=5)
            # Görseli çiz
            canvas = tk.Canvas(frame, width=50, height=50, bg="white", highlightthickness=0)
            canvas.pack()
            canvas.create_oval(25 - size // 2, 25 - size // 2, 25 + size // 2, 25 + size // 2, fill="gray")
            # Seçim düğmesi
            button = tk.Radiobutton(frame, variable=self.size_var, value=size, text=f"{size}px", command=self.update_preview)
            button.pack()

        # Renk Seçenekleri (Renk kutuları ile)
        tk.Label(control_frame, text="Renk:").pack(side="left")
        for color in ["red", "green", "blue"]:
            frame = tk.Frame(control_frame)
            frame.pack(side="left", padx=5)
            # Görseli çiz
            canvas = tk.Canvas(frame, width=50, height=50, bg="white", highlightthickness=0)
            canvas.pack()
            canvas.create_oval(10, 10, 40, 40, fill=color)
            # Seçim düğmesi
            button = tk.Radiobutton(frame, variable=self.color_var, value=color, text=color.capitalize(), command=self.update_preview)
            button.pack()

        # Şekil Ekleme ve Hareket Düğmeleri
        self.add_shape_btn = tk.Button(control_frame, text="Şekil Ekle", command=self.enable_shape_placement)
        self.add_shape_btn.pack(side="left", padx=5)

        self.start_btn = tk.Button(control_frame, text="Start", command=self.start_animation)
        self.start_btn.pack(side="left", padx=5)

        self.stop_btn = tk.Button(control_frame, text="Stop", command=self.stop_animation)
        self.stop_btn.pack(side="left", padx=5)

        self.reset_btn = tk.Button(control_frame, text="Reset", command=self.reset_canvas)
        self.reset_btn.pack(side="left", padx=5)

        self.speed_up_btn = tk.Button(control_frame, text="Speed Up", command=self.speed_up)
        self.speed_up_btn.pack(side="left", padx=5)

        # Toplar ve hareket durumu
        self.balls = []
        self.running = False
        self.speed_multiplier = 1
        self.placing_shape = False  # Şekil ekleme modu
        self.preview_id = None  # Hayalet şekil ID'si

    def enable_shape_placement(self):
        """Kullanıcının şekli yerleştirmek için Canvas'a tıklamasını sağlar."""
        self.placing_shape = True
        self.canvas.bind("<Motion>", self.show_preview)
        self.canvas.bind("<Button-1>", self.add_ball)

    def show_preview(self, event):
        """Fare hareket ederken hayalet şekli gösterir."""
        size = self.size_var.get()
        color = self.color_var.get()

        # Önizleme şekli daha önce varsa, kaldır
        if self.preview_id:
            self.canvas.delete(self.preview_id)

        # Yeni önizleme şekli oluştur
        self.preview_id = self.canvas.create_oval(
            event.x - size, event.y - size, event.x + size, event.y + size,
            outline=color, dash=(4, 4)  # Kesikli çizgi ile hayalet şekil
        )

    def add_ball(self, event):
        """Kullanıcının seçtiği konuma bir top ekler."""
        if not self.placing_shape:
            return

        size = self.size_var.get()
        color = self.color_var.get()
        x, y = event.x, event.y

        dx = random.choice([-2, 2])
        dy = random.choice([-2, 2])

        # Gerçek top ekle
        ball = {
            "id": self.canvas.create_oval(
                x - size, y - size, x + size, y + size, fill=color
            ),
            "dx": dx,
            "dy": dy,
            "size": size,
        }
        self.balls.append(ball)

        # Hayalet şekli kaldır ve fare hareketlerini takip etmeyi durdur
        if self.preview_id:
            self.canvas.delete(self.preview_id)
        self.preview_id = None
        self.placing_shape = False
        self.canvas.unbind("<Motion>")
        self.canvas.unbind("<Button-1>")

    def update_preview(self):
        """Seçilen boyut ve renk değiştikçe önizlemeyi günceller."""
        if self.preview_id:
            # Önizleme şekli varsa güncelle
            size = self.size_var.get()
            color = self.color_var.get()
            self.canvas.itemconfig(self.preview_id, outline=color)
            x1, y1, x2, y2 = self.canvas.coords(self.preview_id)
            cx, cy = (x1 + x2) / 2, (y1 + y2) / 2  # Merkez koordinatlarını hesapla
            self.canvas.coords(self.preview_id, cx - size, cy - size, cx + size, cy + size)

    def update_positions(self):
        for ball in self.balls:
            x1, y1, x2, y2 = self.canvas.coords(ball["id"])
            dx, dy = ball["dx"] * self.speed_multiplier, ball["dy"] * self.speed_multiplier

            # Kenar çarpma kontrolü
            if x1 + dx < 0 or x2 + dx > 600:
                ball["dx"] = -ball["dx"]
            if y1 + dy < 0 or y2 + dy > 400:
                ball["dy"] = -ball["dy"]

            # Topu hareket ettir
            self.canvas.move(ball["id"], ball["dx"] * self.speed_multiplier, ball["dy"] * self.speed_multiplier)

    def start_animation(self):
        if not self.running:
            self.running = True
            self.animate()

    def stop_animation(self):
        self.running = False

    def reset_canvas(self):
        self.running = False
        for ball in self.balls:
            self.canvas.delete(ball["id"])
        self.balls = []
        self.speed_multiplier = 1
        if self.preview_id:
            self.canvas.delete(self.preview_id)
        self.preview_id = None

    def speed_up(self):
        self.speed_multiplier += 1

    def animate(self):
        if self.running:
            self.update_positions()
            self.root.after(20, self.animate)  # Her 20ms'de bir güncelle


# Uygulamayı başlat
root = tk.Tk()
app = BouncingBallsApp(root)
root.mainloop()
