import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageOps, ImageEnhance

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Imagens")

        self.image = None
        self.modified_image = None
        self.original_image = None

        # Canvas
        self.canvas = tk.Canvas(root, width=1000, height=500, bg="#ddd")
        self.canvas.pack(pady=10)

        # Controle carregar/salvar
        control_frame = tk.Frame(root)
        control_frame.pack()
        tk.Button(control_frame, text="Carregar Imagem", command=self.load_image).grid(row=0, column=0, padx=5)
        tk.Button(control_frame, text="Salvar Imagem", command=self.save_image).grid(row=0, column=1, padx=5)

        # Filtros
        filter_frame = tk.LabelFrame(root, text="Filtros", padx=10, pady=10)
        filter_frame.pack(pady=10)

        self.filters = {
            "Escala de Cinza": tk.BooleanVar(),
            "Inverter Cores": tk.BooleanVar(),
            "Aumento de Contraste": tk.BooleanVar(),
            "Blur": tk.BooleanVar(),
            "Nitidez": tk.BooleanVar(),
            "Detecção de Bordas": tk.BooleanVar(),
        }

        for i, (label, var) in enumerate(self.filters.items()):
            tk.Checkbutton(filter_frame, text=label, variable=var).grid(row=i//2, column=i%2, sticky='w')

        # Transformações
        transform_frame = tk.LabelFrame(root, text="Transformações", padx=10, pady=10)
        transform_frame.pack(pady=10)

        tk.Label(transform_frame, text="Rotacionar (graus):").grid(row=0, column=0, sticky='e')
        self.rotate_entry = tk.Entry(transform_frame, width=5)
        self.rotate_entry.grid(row=0, column=1)

        tk.Label(transform_frame, text="Redimensionar Largura:").grid(row=1, column=0, sticky='e')
        self.resize_width_entry = tk.Entry(transform_frame, width=5)
        self.resize_width_entry.grid(row=1, column=1)

        tk.Label(transform_frame, text="Altura:").grid(row=1, column=2, sticky='e')
        self.resize_height_entry = tk.Entry(transform_frame, width=5)
        self.resize_height_entry.grid(row=1, column=3)

        # Botão aplicar tudo
        tk.Button(root, text="Aplicar Filtros e Transformações", command=self.apply_all).pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.jpeg *.png")])
        if file_path:
            self.image = Image.open(file_path)
            self.original_image = self.image.copy()
            self.modified_image = self.image.copy()
            self.show_images(self.original_image, self.modified_image)

    def save_image(self):
        if self.modified_image:
            path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
            if path:
                self.modified_image.save(path)
        else:
            messagebox.showerror("Erro", "Nenhuma imagem para salvar.")

    def resize_image(self, image):
        max_w, max_h = 500, 500
        scale = min(max_w / image.width, max_h / image.height)
        return image.resize((int(image.width * scale), int(image.height * scale)), Image.Resampling.LANCZOS)

    def show_images(self, img1, img2):
        self.canvas.delete("all")
        img1_resized = ImageTk.PhotoImage(self.resize_image(img1))
        img2_resized = ImageTk.PhotoImage(self.resize_image(img2))
        self.tk_img1 = img1_resized
        self.tk_img2 = img2_resized
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img1_resized)
        self.canvas.create_image(500, 0, anchor=tk.NW, image=img2_resized)

    def apply_all(self):
        if not self.image:
            messagebox.showerror("Erro", "Carregue uma imagem primeiro.")
            return

        img = self.image.copy()

        # Aplica rotação
        try:
            angle = float(self.rotate_entry.get())
            if angle != 0:
                img = img.rotate(angle, expand=True)
        except ValueError:
            pass  # Se o campo estiver vazio ou inválido, ignora

        # Aplica redimensionamento
        try:
            width = int(self.resize_width_entry.get())
            height = int(self.resize_height_entry.get())
            if width > 0 and height > 0:
                img = img.resize((width, height), Image.Resampling.LANCZOS)
        except ValueError:
            pass

        # Filtros
        if self.filters["Escala de Cinza"].get():
            img = img.convert("L")

        if self.filters["Inverter Cores"].get():
            img = ImageOps.invert(img.convert("RGB"))

        if self.filters["Aumento de Contraste"].get():
            img = ImageEnhance.Contrast(img).enhance(2)

        if self.filters["Blur"].get():
            img = img.filter(ImageFilter.GaussianBlur(5))

        if self.filters["Nitidez"].get():
            img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

        if self.filters["Detecção de Bordas"].get():
            img = img.filter(ImageFilter.FIND_EDGES)

        self.modified_image = img
        self.show_images(self.original_image, self.modified_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
