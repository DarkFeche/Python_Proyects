import tkinter as tk
from tkinter import scrolledtext, messagebox
import re
import pyperclip
import sys


class PdfTextFormatter:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Text Formatter")
        self.root.geometry("600x450")

        # --- Ventana 1: Entrada ---
        # Etiqueta de instrucción
        label = tk.Label(root, text="Pega aquí el texto del PDF:",
                         font=("Arial", 10, "bold"))
        label.pack(pady=5)

        # Área de texto principal
        self.input_text = scrolledtext.ScrolledText(
            root, width=70, height=15, font=("Arial", 10))
        self.input_text.pack(padx=10, pady=5)

        # Botón de Procesar
        process_btn = tk.Button(root, text="Procesar Texto", command=self.process_text,
                                bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), height=2)
        process_btn.pack(pady=10, fill=tk.X, padx=20)

    def process_text(self):
        """Lógica principal de limpieza de texto."""
        raw_text = self.input_text.get("1.0", tk.END).strip()

        if not raw_text:
            messagebox.showwarning("Aviso", "El campo de texto está vacío.")
            return

        # PASO 1: Proteger los párrafos reales (doble salto de línea)
        # Usamos un marcador temporal único que no suele existir en textos normales.
        temp_text = raw_text.replace('\n\n', '<<PARAGRAPH_MARKER>>')

        # PASO 2: Eliminar saltos de línea erróneos (Regex)
        # Buscamos \n que NO estén precedidos por punto, interrogación o exclamación.
        # Reemplazamos por un ESPACIO para evitar que las palabras se peguen (ej: "hola\nmundo" -> "hola mundo")
        pattern = r'(?<![\.\?!])\n'
        cleaned_text = re.sub(pattern, ' ', temp_text)

        # PASO 3: Restaurar los párrafos reales
        final_text = cleaned_text.replace('<<PARAGRAPH_MARKER>>', '\n\n')

        # Eliminar dobles espacios accidentales generados por el reemplazo
        final_text = re.sub(r' +', ' ', final_text)

        self.show_result_window(final_text)

    def show_result_window(self, text):
        """Ventana 2: Muestra resultado y copia al portapapeles."""

        # Copiar automáticamente al portapapeles
        try:
            pyperclip.copy(text)
            clipboard_status = " (Copiado al portapapeles)"
        except Exception as e:
            clipboard_status = " (Error al copiar: Instala xclip en Linux si falla)"

        # Crear ventana emergente (Toplevel)
        popup = tk.Toplevel(self.root)
        popup.title("Texto Procesado")
        popup.geometry("600x450")

        lbl_info = tk.Label(
            popup, text=f"Texto limpio{clipboard_status}:", fg="blue")
        lbl_info.pack(pady=5)

        output_box = scrolledtext.ScrolledText(
            popup, width=70, height=15, font=("Arial", 10))
        output_box.insert(tk.INSERT, text)
        output_box.pack(padx=10, pady=5)

        # Botón Cerrar (Cierra toda la aplicación como se pidió)
        close_btn = tk.Button(popup, text="Cerrar / Finalizar", command=self.close_app,
                              bg="#f44336", fg="white", font=("Arial", 11, "bold"))
        close_btn.pack(pady=10, fill=tk.X, padx=20)

    def close_app(self):
        self.root.destroy()
        sys.exit()


if __name__ == "__main__":
    root = tk.Tk()
    app = PdfTextFormatter(root)
    root.mainloop()
