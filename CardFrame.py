import customtkinter as CTk

from FileManager import FileManager
from card import Card
from PIL import Image

class ScrollableLabelButtonFrame(CTk.CTkScrollableFrame):
    def __init__(self, master, commandP=None, commandM=None, **kwargs):
        super().__init__(master, **kwargs)
        self.commandP = commandP
        self.commandM = commandM
        self.radiobutton_variable = CTk.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item, id, image=None):
        on_list = 3
        label = CTk.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        buttonPlus = CTk.CTkButton(self, text="Plus", width=100, height=24)
        buttonMinus = CTk.CTkButton(self, text="Minus", width=100, height=24)
        if self.commandP is not None:
            buttonPlus.configure(command=lambda: self.commandP(label, id))
        if self.commandM is not None:
            buttonMinus.configure(command=lambda: self.commandM(label, id))
        shift = len(self.label_list) % on_list * 3
        label.grid(row=len(self.label_list)//on_list, column=0+shift, pady=(0, 10), sticky="w")
        buttonPlus.grid(row=len(self.button_list)//on_list, column=2+shift, pady=(0, 10), padx=5)
        buttonMinus.grid(row=len(self.button_list)//on_list, column=1+shift, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append((buttonPlus,buttonMinus))

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button[0].destroy()
                button[1].destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return

class CardPlace():
    def __init__(self, master, set, **kwargs):
        self._master = master
        self._set = set

        self.fm = FileManager(self._set)
        # create scrollable label and button frame
        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self._master, commandP=self.label_button_frame_event_plus, commandM=self.label_button_frame_event_minus, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")
        i = 0
        for card in self.fm.Cards[self._set]:  # add items with images
            self.scrollable_label_button_frame.add_item(f"Count: {card['card'].Number_in_collection} item {card['card'].Number_in_realese}", id = i, image=CTk.CTkImage(card['image'], size = (200,300)))
            i+=1

    def label_button_frame_event_plus(self, label, id):
        self.fm.Cards[self._set][id]['card'].Number_in_collection+=1
        label.configure(text = f"Count: {self.fm.Cards[self._set][id]['card'].Number_in_collection} item {self.fm.Cards['tech'][id]['card'].Number_in_realese}")

    def label_button_frame_event_minus(self, label, id):
        self.fm.Cards[self._set][id]['card'].Number_in_collection-=1
        label.configure(text = f"Count: {self.fm.Cards[self._set][id]['card'].Number_in_collection} item {self.fm.Cards['tech'][id]['card'].Number_in_realese}")

    def work_off(self):
        del self.scrollable_label_button_frame
        del self.fm

    def __del__(self):
        self.work_off()
        print("I DEAD")
