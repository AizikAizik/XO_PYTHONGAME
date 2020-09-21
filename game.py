import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
#set window Title
root.title("Tic-Tac-Toe")

#value holder variable for player 1
playera = tk.StringVar()

#value holder variable for player 2
playerb = tk.StringVar()

p1 = tk.StringVar()
p2 = tk.StringVar()

#widget for player 1 to enter player name
player1_name = tk.Entry(root,textvariable=p1, bd=5)
#place the player1 widget on the window
player1_name.grid(row=1, column=1, columnspan=8)

#widget for player 2 to enter player name
player2_name = tk.Entry(root,textvariable=p2, bd=5)
#place the player2 widget on the window
player2_name.grid(row=2, column=1, columnspan=8)

#intialize button click to true
bclick = True

#initialize flag to zero
flag = 0

buttons = tk.StringVar()
#button = ["button1","button2","button3","button4","button5","button6","button7","button8","button9"]

#function for disabling the buttons
def disableButton():
    button1.configure(state="disabled")
    button2.configure(state="disabled")
    button3.configure(state="disabled")
    button4.configure(state="disabled")
    button5.configure(state="disabled")
    button6.configure(state="disabled")
    button7.configure(state="disabled")
    button8.configure(state="disabled")
    button9.configure(state="disabled")

#functionality for clicking a button
def btnClick(buttons):
    #get instances to global variables
    global bclick, flag, player1_name, player2_name, playera, playerb
    
    if buttons["text"] == "" and bclick == True:
        buttons["text"] = "X"
        bclick = False # set to false to make it O turn
        playerb = p2.get() + " Wins!!"
        playera = p1.get() + " Wins!!"
        checkForWin() # keep checking if anybody has won
        flag += 1
    elif buttons["text"] == "" and bclick == False:
        buttons["text"] = "O"
        bclick = True # set to true to make it X turn
        checkForWin() # keep checking if anybody wins
        flag += 1    
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already clicked!!")

#function for checking for winner or draw
def checkForWin():
    #check cases where X wins
    if(
        button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or
        button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or
        button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
        button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" or
        button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or
        button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or
        button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" or
        button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"
    ):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playera)
       
    # Game ended in tie if flag's count gets to 8 
    elif flag == 8:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Game ended in a Tie!!")
        disableButton() #disable all the buttons
      
    #check for cases where O wins  
    elif(
        button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
        button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
        button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
        button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or
        button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
        button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or
        button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" or
        button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"
    ):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)

    
# design labels and buttons
label = tk.Label(root, text="player 1:", font="Input 17 bold", bg="white", fg="black", height=1,width=8)
label.grid(row=1, column=0)

label = tk.Label(root, text="player 2:", font="Input 17 bold", bg="white", fg="black", height=1,width=8)
label.grid(row=2, column=0)

# for i in range(1,10):
#     col1=0
#     col2=0
#     col3=0
#     globals()["button" + str(i)] = tk.Button(root,
#                               text="",
#                               font="Input 20 bold",
#                               bg="grey",
#                               fg="white",
#                               height=4,
#                               width=8,
#                               command=lambda : btnClick(globals()["button" + str(i)]))
    
#     if(i < 4):
#         globals()["button" + str(i)].grid(row=3, column=col1)
#         col1 += 1
#     elif(i>=4 and i<7):
#         globals()["button" + str(i)].grid(row=4, column=col2)
#         col2 += 1
#     else:
#         globals()["button" + str(i)].grid(row=5, column=col3)
#         col3 += 1
button1 = tk.Button(root,
                       text="",
                       font="Input 20 bold",
                       bg="grey",
                       fg="white",
                       height=4,
                       width=8,
                       command=lambda : btnClick(button1) )

button1.grid(row=3, column=0)

button2 = tk.Button(root,
                       text="",
                       font="Input 20 bold",
                       bg="grey",
                       fg="white",
                       height=4,
                       width=8,
                       command=lambda : btnClick(button2) )

button2.grid(row=3, column=1)

button3 = tk.Button(root,
                       text="",
                       font="Input 20 bold",
                       bg="grey",
                       fg="white",
                       height=4,
                       width=8,
                       command=lambda : btnClick(button3) )

button3.grid(row=3, column=2)

button4 = tk.Button(root,
                       text="",
                       font="Input 20 bold",
                       bg="grey",
                       fg="white",
                       height=4,
                       width=8,
                       command=lambda : btnClick(button4) )

button4.grid(row=4, column=0)

button5 = tk.Button(root,
                       text="",
                       font="Input 20 bold",
                       bg="grey",
                       fg="white",
                       height=4,
                       width=8,
                       command=lambda : btnClick(button5) )

button5.grid(row=4, column=1)

button6 = tk.Button(root,
                       text="",
                       font="Input 20 bold",
                       bg="grey",
                       fg="white",
                       height=4,
                       width=8,
                       command=lambda : btnClick(button6) )

button6.grid(row=4, column=2)

button7 = tk.Button(root,
                       text="",
                       font="Input 20 bold",
                       bg="grey",
                       fg="white",
                       height=4,
                       width=8,
                       command=lambda : btnClick(button7) )

button7.grid(row=5, column=0)

button8 = tk.Button(root,
                       text="",
                       font="Input 20 bold",
                       bg="grey",
                       fg="white",
                       height=4,
                       width=8,
                       command=lambda : btnClick(button8) )

button8.grid(row=5, column=1)

button9 = tk.Button(root,
                       text="",
                       font="Input 20 bold",
                       bg="grey",
                       fg="white",
                       height=4,
                       width=8,
                       command=lambda : btnClick(button9) )

button9.grid(row=5, column=2)

root.mainloop()