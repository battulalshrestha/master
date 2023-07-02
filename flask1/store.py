from tkinter import *
import random
from PIL import Image,ImageTk
main = Tk()
main.title("card deck")
main.geometry("900x500")
main.configure(background=" green")
def resize_cards(card):
  card_img = Image.open(card)
  card_resize_img = card_img.resize(150,218)
  global card_image
  card_image = ImageTk.PhotoImage()