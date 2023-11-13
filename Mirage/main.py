import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
# from tkinter import *
# window = Tk()
# window.title("Mirage")
# window.geometry("400х500+600+300")
# window.resizable(False, False)
# icon = PhotoImage(file='MirageLogo.ico')
# window.iconphoto(True,icon)
# window.iconbitmap("MirageLogo.ico")
# window.mainloop()

class MirageEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Mirage")

        # Устанавливаем иконку приложения
        self.root.iconbitmap("MirageLogo.ico")

        # Создаем меню
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Меню "Файл"
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Сохранить", command=self.save_image)

        # Меню "Справка"
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="О программе", command=self.show_about_dialog)

        # Меню "Параметры"
        options_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Параметры", menu=options_menu)
        options_menu.add_command(label="Размер холста", command=self.change_canvas_size)

        # Создаем холст
        self.canvas = tk.Canvas(root, width=1366, height=768, bg="white")
        self.canvas.pack()

        # Добавляем кнопки для выбора цвета, кисти и масштаба

        # Кнопка "Цвет"
        color_button = tk.Button(root, text="Цвет", command=self.choose_color)
        color_button.pack()

        # Кнопка "Кисть"
        brush_button = tk.Button(root, text="Кисть", command=self.choose_brush)
        brush_button.pack()

        # Кнопка "Масштаб"
        scale_button = tk.Button(root, text="Масштаб", command=self.change_scale)
        scale_button.pack()

        # Переменные для хранения текущих параметров
        self.current_color = "black"
        self.current_brush_size = 2
        self.current_scale = 1.0

        # Привязываем события
        self.canvas.bind("<Button-1>", self.draw)

    def draw(self, event):
        x, y = event.x, event.y
        brush_size = self.current_brush_size
        scaled_brush_size = int(brush_size * self.current_scale)
        x1, y1 = x - scaled_brush_size, y - scaled_brush_size
        x2, y2 = x + scaled_brush_size, y + scaled_brush_size
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.current_color, outline=self.current_color)

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            try:
                x = self.root.winfo_rootx() + self.canvas.winfo_x()
                y = self.root.winfo_rooty() + self.canvas.winfo_y()
                x1 = x + self.canvas.winfo_width()
                y1 = y + self.canvas.winfo_height()
                self.canvas.postscript(file=file_path, colormode='color')
                messagebox.showinfo("Mirage", "Изображение успешно сохранено.")
            except Exception as e:
                messagebox.showerror("Mirage", f"Ошибка при сохранении изображения: {str(e)}")

    def show_about_dialog(self):
        messagebox.showinfo("О программе", "Mirage - графический редактор создан на основе потраченных нервов и слёз разработчиков.\nРазработчики: Dimon & Dimentor.\nSo H!gh inc.\n2023 ")

    def change_canvas_size(self):
        # Здесь можно добавить функциональность для изменения размера холста
        pass

    def choose_color(self):
        color = colorchooser.askcolor(title="Выберите цвет")[1]
        if color:
            self.current_color = color

    def choose_brush(self):
        # Здесь можно добавить функциональность для выбора размера и формы кисти
        pass

    def change_scale(self):
        # Здесь можно добавить функциональность для изменения масштаба окна
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = MirageEditor(root)
    root.mainloop()
