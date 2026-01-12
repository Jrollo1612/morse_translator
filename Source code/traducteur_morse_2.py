from tkinter import *
from tkinter import filedialog, messagebox

# ---------------- Morse mapping ----------------

morse = {
    'A': '🟣➖',
    'B': '➖🟣🟣🟣',
    'C': '➖🟣➖🟣',
    'D': '➖🟣🟣',
    'E': '🟣',
    'F': '🟣🟣➖🟣',
    'G': '➖➖🟣',
    'H': '🟣🟣🟣🟣',
    'I': '🟣🟣',
    'J': '🟣➖➖➖',
    'K': '➖🟣➖',
    'L': '🟣➖🟣🟣',
    'M': '➖➖',
    'N': '➖🟣',
    'O': '➖➖➖',
    'P': '🟣➖➖🟣',
    'Q': '➖➖🟣➖',
    'R': '🟣➖🟣',
    'S': '🟣🟣🟣',
    'T': '➖',
    'U': '🟣🟣➖',
    'V': '🟣🟣🟣➖',
    'W': '🟣➖➖',
    'X': '➖🟣🟣➖',
    'Y': '➖🟣➖➖',
    'Z': '➖➖🟣🟣'
}


# ---------------- Logic ----------------

class MorseTranslator:
    def __init__(self):
        self.mapping = morse
        self.inverse = {v: k for k, v in self.mapping.items()}

    def text_to_morse(self, text):
        text = text.upper()
        words = text.split()
        out = []
        for w in words:
            letters = [self.mapping[c] for c in w if c in self.mapping]
            out.append("/".join(letters))
        return "//".join(out)

    def morse_to_text(self, code):
        words = code.split("//")
        out = []
        for w in words:
            letters = [self.inverse.get(l, "") for l in w.split("/")]
            out.append("".join(letters))
        return " ".join(out)

# ---------------- GUI ----------------

class MorseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traducteur Morse")
        self.root.geometry("900x700")
        self.root.configure(bg="#1e1e1e")

        self.translator = MorseTranslator()
        self.last_output = ""

        # Colors (dark theme)
        self.root_bg = "#1e1e1e"
        self.panel_bg = "#2b2b2b"
        self.text_bg = "#121212"
        self.text_fg = "#ffffff"
        self.btn_bg = "#3a3a3a"
        self.fg = "#ffffff"

        # ---------- Top bar ----------
        top = Frame(root, bg=self.root_bg)
        top.pack(fill=X, pady=5)

        Label(top, text="Traducteur Morse", bg=self.root_bg, fg="white",
              font=("Segoe UI", 14, "bold")).pack()

        # ---------- Center panels ----------
        center = Frame(root, bg=self.root_bg)
        center.pack(fill=BOTH, expand=True, padx=10, pady=10)

        left = Frame(center, bg=self.panel_bg)
        left.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 5))

        right = Frame(center, bg=self.panel_bg)
        right.pack(side=RIGHT, fill=BOTH, expand=True, padx=(5, 0))

        Label(left, text="Texte", bg=self.panel_bg, fg=self.fg).pack(anchor="w", padx=8, pady=5)
        Label(right, text="Traduction", bg=self.panel_bg, fg=self.fg).pack(anchor="w", padx=8, pady=5)

        self.input_text = Text(left, bg=self.text_bg, fg=self.text_fg,
                               insertbackground="white", wrap="word")
        self.input_text.pack(fill=BOTH, expand=True, padx=8, pady=(0, 8))

        self.output_text = Text(right, bg=self.text_bg, fg=self.text_fg,
                                wrap="word")
        self.output_text.pack(fill=BOTH, expand=True, padx=8, pady=(0, 8))

        self.morse_bar = Frame(root, bg=self.root_bg)
        self.morse_bar.pack(pady=6)

        self.dot_btn = Button(self.morse_bar, text="🟣", font=("Segoe UI", 14),
                              width=4, command=lambda: self.insert_morse("🟣"))
        self.dot_btn.pack(side=LEFT, padx=5)
        self.dash_btn = Button(self.morse_bar, text="➖", font=("Segoe UI", 14),
                       width=4, command=lambda: self.insert_morse("➖"))
        self.dash_btn.pack(side=LEFT, padx=5)

        self.slash_btn = Button(self.morse_bar, text="/", font=("Segoe UI", 14),
                        width=4, command=lambda: self.insert_morse("/"))
        self.slash_btn.pack(side=LEFT, padx=5)
        self.clear_btn = Button(self.morse_bar, text="⌫", font=("Segoe UI", 14),
                        width=4, command=self.backspace)
        self.clear_btn.pack(side=LEFT, padx=5)

        self.morse_bar.pack_forget()   # caché au démarrage


        # ---------- Bottom buttons ----------
        bottom = Frame(root, bg=self.root_bg)
        bottom.pack(fill=X, pady=8)

        Button(bottom, text="Ouvrir fichier", bg=self.btn_bg, fg=self.fg,
               command=self.open_file).pack(side=LEFT, padx=10)

        Button(bottom, text="Enregistrer", bg=self.btn_bg, fg=self.fg,
               command=self.save_file).pack(side=LEFT)

        # ---------- Bind ----------
        self.input_text.bind("<KeyRelease>", self.auto_translate)

    # ---------------- Logic ----------------
    def insert_morse(self, char):
        self.input_text.insert(END, char)
        self.auto_translate()

    def backspace(self):
        self.input_text.delete("end-2c")
        self.auto_translate()

    def auto_translate(self, event=None):
        src = self.input_text.get("1.0", END).strip()
        if not src:
            self.output_text.delete("1.0", END)
            return

        morse_chars = set("🟣➖/ ")
        if all(c in morse_chars for c in src):
            res = self.translator.morse_to_text(src)
        else:
            res = self.translator.text_to_morse(src)

        self.output_text.delete("1.0", END)
        self.output_text.insert(END, res)
        self.last_output = res
        # afficher / cacher clavier morse
        src = self.input_text.get("1.0", END).strip()
        if src and all(c in "🟣➖/ " for c in src):
            self.morse_bar.pack()
        else:
            self.morse_bar.pack_forget()


    def swap(self):
        a = self.input_text.get("1.0", END)
        b = self.output_text.get("1.0", END)

        self.input_text.delete("1.0", END)
        self.output_text.delete("1.0", END)

        self.input_text.insert(END, b)
        self.output_text.insert(END, a)

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text", "*.txt")])
        if not path:
            return
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
        self.input_text.delete("1.0", END)
        self.input_text.insert(END, data)
        self.auto_translate()

    def save_file(self):
        if not self.last_output:
            return
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if not path:
            return
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.last_output)
        messagebox.showinfo("OK", "Fichier enregistré")

# ---------------- Run ----------------

if __name__ == "__main__":
    root = Tk()
    app = MorseApp(root)
    root.mainloop()
