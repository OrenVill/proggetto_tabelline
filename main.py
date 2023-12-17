from random import randint
from os import system
from time import sleep
from tkinter import *
from tkinter import messagebox


def first_time():
    global can, card_front_img, card_background, card_back_img, entry, confirm_button, result

    can = Canvas(width=800, height=526)
    card_front_img = PhotoImage(file="images/card_front.png")
    card_back_img = PhotoImage(file="images/card_back.png")
    card_background = can.create_image(400, 263, image=card_back_img)
    entry = Entry(font=("Ethnocentric", 25, "bold"), width=3)
    confirm_button = Button(can, width=17, text="submit", font=("Alien Encounters", 20, "bold"), bg="#11ff0e", command=confirm)

    first_number = randint(0, 10)
    second_number = randint(0, 10)
    result = first_number * second_number
    calcolo = f"{first_number} x {second_number}"
    can.create_text(400, 200, text=calcolo, font=("Ethnocentric", 80, "bold"))
    can.create_window(400, 300, window=entry)
    confirm_button.place(x=250, y=400)

    can.config(highlightthickness=0, bg="#2767EC")
    can.grid(column=0, row=0, padx=10, pady=10)

    

    


def confirm():
    right = None
    try:
        entry_int = int(entry.get())
    except ValueError:
        messagebox.showwarning("numero", "scrivi un numero, non delle lettere")

    finally:
        if entry_int == result:
            right = True
        else:
            right = False
        flip_slide(right)



def flip_slide(is_correct):
    if is_correct:
        reponse = "giusto"
    else:
        reponse = "sbagliato"

    print(reponse)

    can.itemconfig(2, state = "hidden")
    can.itemconfig(3, state = "hidden") 
    confirm_button.place_forget()


    can.itemconfig(card_background, image = card_front_img) 
    
    reponse_label = Label(text=reponse, font=("Ethnocentric", 50, "bold"), fg="orange", bg="cyan")
    can.create_window(400, 200, window=reponse_label)

    result_labeel = Label(text=f"La risposta è {result}", font=("Ethnocentric", 25, "bold"), fg="red", bg="green")
    can.create_window(400, 350, window=result_labeel)

    can.update()
    sleep(3)
    new_card()



def new_card():
    global result

    can.delete("all")

    card_background = can.create_image(400, 263, image=card_back_img)


    can.itemconfig(2, state = "normal")
    can.itemconfig(3, state = "normal") 
    confirm_button.place(x=250, y=400)

    can.itemconfig(card_background, image = card_back_img) 

    first_number = randint(0, 10)
    second_number = randint(0, 10)
    result = first_number * second_number
    calcolo = f"{first_number} x {second_number}"
    can.create_text(400, 200, text=calcolo, font=("Ethnocentric", 80, "bold"))









window = Tk()
window.geometry("800x526")
first_time()

window.mainloop()