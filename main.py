import tkinter
import customtkinter as CTk

from CardFrame import CardPlace

class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('{}x{}'.format(int(self.winfo_screenwidth()*0.9), int(self.winfo_screenheight()*0.9)))
        self.title("БЕРСЕРК")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=2)
        self.columnconfigure(2, weight=1)

        self.card_place = None

        def on_closing():
            if self.card_place is not None:
                self.card_place.work_off()
            print("Выводится при попытке закрытия окна")
            self.destroy()  # Закрыть окно
        self.protocol("WM_DELETE_WINDOW", on_closing)

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
            self.Space_card()
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

    def Space_card(self):
        self.card_place = CardPlace(master = self, set = 'tech')


if __name__ == "__main__":
    app = App()
    app.mainloop()
