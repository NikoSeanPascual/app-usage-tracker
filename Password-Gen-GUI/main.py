import customtkinter as ctk
import string
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class PasswordGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Niko's Password Generator")
        self.geometry("420x420")
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        title = ctk.CTkLabel(
            self,
            text="PASSWORD GENERATOR",
            font=("Verdana", 22, "bold")
        )
        title.pack(pady=15)

        length_frame = ctk.CTkFrame(self)
        length_frame.pack(pady=10, padx=20, fill="x")

        self.length_label = ctk.CTkLabel(
            length_frame,
            text="Length: 12"
        )
        self.length_label.pack(pady=(10, 0))

        self.length_slider = ctk.CTkSlider(
            length_frame,
            from_=8,
            to=32,
            number_of_steps=24,
            command=self.update_length_label
        )
        self.length_slider.set(12)
        self.length_slider.pack(pady=10, padx=15)

        options_frame = ctk.CTkFrame(self)
        options_frame.pack(pady=10, padx=20, fill="x")

        self.var_upper = ctk.BooleanVar(value=True)
        self.var_lower = ctk.BooleanVar(value=True)
        self.var_numbers = ctk.BooleanVar(value=True)
        self.var_symbols = ctk.BooleanVar(value=False)

        ctk.CTkCheckBox(options_frame, text="Uppercase Letters (A-Z)", variable=self.var_upper).pack(anchor="w", padx=15, pady=2)
        ctk.CTkCheckBox(options_frame, text="Lowercase Letters (a-z)", variable=self.var_lower).pack(anchor="w", padx=15, pady=2)
        ctk.CTkCheckBox(options_frame, text="Numbers (0-9)", variable=self.var_numbers).pack(anchor="w", padx=15, pady=2)
        ctk.CTkCheckBox(options_frame, text="Symbols (!@#)", variable=self.var_symbols).pack(anchor="w", padx=15, pady=2)

        output_frame = ctk.CTkFrame(self)
        output_frame.pack(pady=10, padx=20, fill="x")

        self.password_entry = ctk.CTkEntry(
            output_frame,
            font=("Lucida Console", 14),
            justify="center"
        )

        self.password_entry.pack(pady=12, padx=15, fill="x")


        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=10)

        ctk.CTkButton(
            button_frame,
            text="GENERATE",
            width=140,
            command=self.generate_password
        ).grid(row=0, column=0, padx=10)

        ctk.CTkButton(
            button_frame,
            text="COPY",
            width=140,
            command=self.copy_password
        ).grid(row=0, column=1, padx=10)

        self.error_label = ctk.CTkLabel(self, text="", text_color="red")
        self.error_label.pack(pady=(5, 0))

    def update_length_label(self, value):
        self.length_label.configure(text=f"Length: {int(value)}")

    def generate_password(self):
        self.error_label.configure(text="")
        self.password_entry.delete(0, "end")

        char_pool = ""

        if self.var_upper.get():
            char_pool += string.ascii_uppercase
        if self.var_lower.get():
            char_pool += string.ascii_lowercase
        if self.var_numbers.get():
            char_pool += string.digits
        if self.var_symbols.get():
            char_pool += string.punctuation

        if not char_pool:
            self.error_label.configure(text="MUST SELECT AT LEAST ONE OF THE OPTION.")
            return

        length = int(self.length_slider.get())
        password = "".join(random.choice(char_pool) for _ in range(length))

        self.password_entry.insert(0, password)


    def copy_password(self):
        password = self.password_entry.get()
        if password:
            self.clipboard_clear()
            self.clipboard_append(password)

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()