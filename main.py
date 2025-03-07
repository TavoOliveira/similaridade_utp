from book import Book
from enums.rating_age import Rating_Age

book = Book("As Aventuras de Nicolau Nicolei", "Gustei Gustai", ["Infantil", "Ação"], Rating_Age.Plus18, 10, "https://th.bing.com/th/id/OIP.uwteg2Qa3dIeY00GaeuOoQHaEK?rs=1&pid=ImgDetMain")

# import TKinterModernThemes as TKMT
# import tkinter as tk
# from PIL import Image, ImageTk
# import os

# class App(TKMT.ThemedTKinterFrame):
#         def __init__(self):
#                 super().__init__("Similaridade", "sun-valley", "dark")

#                 self.frame = self.addFrame("Container")

#                 icon_search_path = os.path.join("icons", "search.png")
#                 self.search_icon = ImageTk.PhotoImage(Image.open(icon_search_path).resize((16, 16)))

#                 search_button = self.frame.AccentButton("Search", command=self.handle_button_search, col=1)
#                 search_button.config(image=self.search_icon, compound=tk.LEFT)

#                 self.entrada = tk.StringVar()

#                 text_box = self.frame.Entry(textvariable=self.entrada, col=0)

#                 self.run()

#         def handle_button_search(self):
#                 print(self.entrada.get())


# if __name__ == "__main__":
#         App()