from random import randint
from os import system
from time import sleep
from tkinter import *
from tkinter import messagebox


window = Tk()
window.geometry("800x526")

class Card:
    
    def __init__(self):

        self.confirm_button = None
        self.entry = None
        self.card_background = None
        self.result = None
        self.can = Canvas(width=800, height=526)
        self.card_front_img= PhotoImage(file="images/card_front.png")
        self.card_back_img = PhotoImage(file="images/card_back.png")
        self.can.config(highlightthickness=0, bg="#2767EC")
        self.can.grid(column=0, row=0, padx=10, pady=10)



    



    def new_card(self):

        self.can.delete("all")


        first_number = randint(0, 10)
        second_number = randint(0, 10)
        self.result = first_number * second_number
        exercise = f"{first_number} x {second_number}"
        self.entry = Entry(font=("Ethnocentric", 25, "bold"), width=3, name="entry")
        self.entry.focus_set()
        self.confirm_button = Button(self.can, width=17, text="submit", font=("Alien Encounters", 20, "bold"), bg="#11ff0e", command=self.confirm, name="confirm_button")
        window.bind('<Return>', self.confirm)

        self.card_background = self.can.create_image(400, 263, image=self.card_back_img)
        self.can.create_text(400, 200, text=exercise, font=("Ethnocentric", 80, "bold"))
        self.can.create_window(400, 300, window=self.entry)
        self.confirm_button.place(x=250, y=400)


    def confirm(self, *kw):
        entry_int = None
        right = None
        try:
            entry_int = int(self.entry.get())
        except ValueError:
            messagebox.showwarning("numero", "scrivi un numero, non delle lettere")
        finally:
            if entry_int == self.result:
                right = True
            else:
                right = False
            self.flip_slide(right)


    def flip_slide (self, is_correct):

        if is_correct:
            reponse = "giusto"
        else:
            reponse = "sbagliato"

        print(reponse)

        self.can.delete("all")
        self.confirm_button.place_forget()


        self.card_background = self.can.create_image(400, 263, image=self.card_front_img)

        
        reponse_label = Label(text=reponse, font=("Ethnocentric", 50, "bold"), fg="orange", bg="cyan")
        self.can.create_window(400, 200, window=reponse_label)

        result_labeel = Label(text=f"La risposta è {self.result}", font=("Ethnocentric", 25, "bold"), fg="red", bg="green")
        self.can.create_window(400, 350, window=result_labeel)

        self.can.update()
        sleep(3)
        self.new_card()








card = Card()
card.new_card()

window.mainloop()