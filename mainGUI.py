from Tkinter import *

import rockpaperscissors
import hangman
import pokerdice

root = Tk()
root.title("Linux User & Developer's Mega Microgames Collector")

mainframe = Frame(root, height = 200, width = 500)
mainframe.pack_propagate(0)
mainframe.pack(padx = 5, pady = 5)

intro = Label(mainframe, text="""Welcome to Linux User & Developers Mega Microgames Collection.
Please select one of the following games to play:
""")
intro.pack(side = TOP)

rsp_button = Button(mainframe, text = "Rock, Paper Scissors", command = rockpaperscissors.gui)
rsp_button.pack()

hm_button = Button(mainframe, text = "Hangman", command = hangman.gui)
hm_button.pack()

pd_button = Button(mainframe, text = "Poker Dice", command = pokerdice.gui)
pd_button.pack()

exit_button = Button(mainframe, text = "Quit", command = root.destroy)
exit_button.pack(side = BOTTOM)

root.mainloop()

