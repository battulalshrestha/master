from tkinter import *
import random
from PIL import Image, ImageTk

main = Tk()
main.title("card deck")
main.geometry("900x500")
main.configure(background="green")

def resize_cards(card):
    card_img = Image.open(card)
    card_resize_img = card_img.resize((150, 218))  # Specify the desired width and height
    card_image = ImageTk.PhotoImage(card_resize_img)
    # Additional code goes here

# Example usage of the resize_cards() function
card_path = "https://www.google.com/imgres?imgurl=http://t2.gstatic.com/images?q%3Dtbn:ANd9GcQfc71DZSZyWHVcwb3fK3U5menXyMIhh26kVF6hTKytPLUgm0X6&imgrefurl=https://th.m.wikipedia.org/wiki/%E0%B9%84%E0%B8%9F%E0%B8%A5%E0%B9%8C:Playing_card_diamond_A.svg&h=150.jpg"

resize_cards(card_path)

main.mainloop()


