import tkinter
import customtkinter as CTk

from FileManager import FileManager as fm
from card import Card
from PIL import Image

class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.FM = fm()

        self.geometry("800x600")
        self.title("БЕРСЕРК")
        self.resizable(False, False)

        self.Main()


    def Main(self):
        def button_event():
            self.Change_Menu('tech')
            Kill()

        button = CTk.CTkButton(master=self,
                                         text="База",
                                         command=button_event,
                                         width=120,
                                         height=32,
                                         border_width=0,
                                         corner_radius=8)
        button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        def Kill():
            button.destroy()

    def Change_Menu(self, set):
        def button_event():
            print(set)
            self.Space_card(set)
            Kill()

        button = CTk.CTkButton(master=self,
                                         text="Механизмы",
                                         command=button_event,
                                         width=120,
                                         height=32,
                                         border_width=0,
                                         corner_radius=8)
        button.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

        def Kill():
            button.destroy()

    def Space_card(self, set):
        labels = []
        x = 1
        y = 1
        s = 2
        for card in self.FM.Cards[set]:
            cardImage = CTk.CTkImage(dark_image = card['image'], size = (89*s,63*s))
            label = CTk.CTkLabel(master = self, text = '', image = cardImage)
            label.grid(row = 0+y, column = 0+x, padx = (0, 20), pady = (0, 20))
            if x == 4:
                x = 1
                y+=1
            else:
                x += 1

        def button_event():
            print(set)
            self.Main()
            Kill()

        button = CTk.CTkButton(master=self,
                                         text="выйти",
                                         command=button_event,
                                         width=120,
                                         height=32,
                                         border_width=0,
                                         corner_radius=8)
        button.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

        def Kill():
            button.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
