from tkinter import *
from random import *
from tkinter import messagebox
from tkinter import ttk
from TicTacToedb import *
import sqlite3
import customtkinter

# Creation de gui
window = Tk()
window.geometry('480x303')
window.minsize(480,303)
window.title('XO')

# Global valeurs
switch_value = True
win = False
clicked = True
player1_wins = 0
player2_wins = 0
count = 0
user_wins = 0
computer_wins = 0
tie = 0

def tab_0():
    # Fonctions
    def about():
        messagebox.showinfo('Tic Tac Toe',"Deux joueurs s'affrontent. Ils doivent remplir chacun à leur tour une case de la grille avec le symbole qui leur est attribué: O ou X. Le gagnant est celui qui arrive à aligner trois symboles identiques, horizontalement, verticalement ou en diagonale. Il est coutume de laisser le joueur jouant X effectuer le premier coup de la partie.")
    def close():
        drop()
        window.destroy()

    # Menu de tab_0
    my_menu = Menu(window)
    window.config(menu=my_menu)
    Exit = Menu(my_menu, tearoff=0)
    Option = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label='Exit', menu=Exit)
    my_menu.add_cascade(label='Option', menu=Option)
    Exit.add_command(label='Quitter', command=close)
    Option.add_command(label='About', command=about)

    def tab_1():
        # Fonction
        def retour():
            player1.destroy()
            player_input1.destroy()
            player2.destroy()
            player_input2.destroy()
            submit1.destroy()
            label1.destroy()
            label2.destroy()
            text.destroy()
            tab_0()

        # Creation de base de donnees
        first_connection()

        # Destroy le contenu et le menu de tab_0
        welcome.destroy()
        frame1.destroy()
        frame2.destroy()
        button_debut1.destroy()
        button_debut2.destroy()
        my_menu.delete('Exit')
        my_menu.delete('Option')
        
        # Creation de meny de tab_1
        Exit = Menu(my_menu, tearoff=0)
        Option = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Exit', menu=Exit)
        my_menu.add_cascade(label='Option', menu=Option)
        Exit.add_command(label='Quitter', command=close)
        Exit.add_separator()
        Exit.add_command(label='Retour', command=retour)
        Option.add_command(label='About', command=about)
        
        # Joueurs 1 et 2 infos
        player1 = Label(window, text='Player 1 :')
        player1.grid(row=0, column=0, padx=10)
        player_input1 = Entry(window, width=50)
        player_input1.grid(row=0, column= 1, padx= 10, pady= 10)
        
        player2 = Label(window, text='Player 2 :')
        player2.grid(row=1, column=0, padx=10)
        player_input2 = Entry(window, width=50)
        player_input2.grid(row=1, column= 1, padx= 10, pady= 10)
        
        # Compteur de lettres de joueurs 1 et 2
        str1 = StringVar(value=0)
        label1 = Label(window, textvariable=str1, width=2)
        label1.grid(row=0, column=2)
        player_input1.bind('<KeyRelease>',lambda x : str1.set(str(len(player_input1.get()))))

        str2 = StringVar(value=0)
        label2 = Label(window, textvariable=str2, width=2)
        label2.grid(row=1, column=2)
        player_input2.bind('<KeyRelease>',lambda y : str2.set(str(len(player_input2.get()))))
        
        # Required info
        text = Label(window, text="""Il faut donner deux noms de 8 lettres de plus à chacun!"""
                    ,font=("Courrier", 12), bd=1, relief=SUNKEN, bg='black', fg='white')
        text.place(relx=.5, rely=.5, anchor='center')

        # the user entered data in the mandatory entry: proceed to next step
        def next_step1():
            if player_input1.get() and player_input2.get() and(len(player_input1.get()) <= 8) and(len(player_input2.get()) <= 8):
                # Creation des donnees
                p1 = player_input1.get()
                p2 = player_input2.get()
                add(p1)
                add(p2)

                # Destroy le contenu de tab_1
                player1.destroy()
                player_input1.destroy()
                player2.destroy()
                player_input2.destroy()
                submit1.destroy()
                label1.destroy()
                label2.destroy()
                text.destroy()

                def tab_2():
                    # Destroy Menu
                    my_menu.delete('Exit')
                    my_menu.delete('Option')

                    # Fonctions
                    def retour():
                        rejouer()
                        frame3.destroy()
                        frame6.destroy()
                        finish_button.destroy()
                        pl1label.destroy()
                        pl2label.destroy()
                        score_1.destroy()
                        score_2.destroy()
                        for i in range(3):
                            for j in range(3):
                                buttons[i][j].destroy()
                        my_menu.delete('Rejouer')
                        drop()
                        tab_1()

                    def accueil():
                        player1.destroy()
                        player_input1.destroy()
                        player2.destroy()
                        player_input2.destroy()
                        frame3.destroy()
                        finish_button.destroy()
                        frame6.destroy()
                        pl1label.destroy()
                        pl2label.destroy()
                        score_1.destroy()
                        score_2.destroy()
                        text.destroy()
                        for i in range(3):
                            for j in range(3):
                                buttons[i][j].destroy()
                        drop()
                        tab_0()
                    
                    def rejouer():
                        global count, clicked, win, player1_wins, player2_wins
                        count = 0
                        clicked = True
                        win = False
                        player1_wins = 0
                        player2_wins = 0
                        score_1.config(text=player1_wins)
                        score_2.config(text=player2_wins)
                        for i in range(3):
                            for j in range(3):
                                buttons[i][j].config(text='', state=NORMAL)
                                
                    def round():
                        global count, clicked, win
                        count = 0
                        clicked = True
                        win = False
                        for i in range(3):
                            for j in range(3):
                                buttons[i][j].config(text='', state=NORMAL)
                                
                    def players(row, col):
                        global clicked, count
                        count += 1
                        if count % 2 != 0:
                            if buttons[row][col]["text"] == "" and clicked == True:
                                buttons[row][col]["text"] = "X"
                                buttons[row][col].config(state=DISABLED)
                                checkuserwinning()
                        else:
                            if buttons[row][col]["text"] == "" and clicked == True:
                                buttons[row][col]["text"] = "O"
                                buttons[row][col].config(state=DISABLED)
                                checkuserwinning()
                            
                    def checkuserwinning():
                        global count, win, player1_wins, player2_wins, tie
                        for i in range(3):
                            if count % 2 != 0 and(buttons[i][0]["text"] == 'X' and buttons[i][1]["text"] == 'X' and buttons[i][2]["text"] == 'X'):
                                player1_wins += 1
                                update1(player1_wins)
                                score_1.config(text=player1_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 != 0 and(buttons[0][i]['text'] == 'X' and buttons[1][i]['text'] == 'X' and buttons[2][i]['text'] == 'X'):
                                player1_wins += 1
                                update1(player1_wins)
                                score_1.config(text=player1_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 != 0 and(buttons[0][0]['text'] == 'X' and buttons[1][1]['text'] == 'X' and buttons[2][2]['text'] == 'X'):
                                player1_wins += 1
                                update1(player1_wins)
                                score_1.config(text=player1_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 != 0 and(buttons[0][2]['text'] == 'X' and buttons[1][1]['text'] == 'X' and buttons[2][0]['text'] == 'X'):
                                player1_wins += 1
                                update1(player1_wins)
                                score_1.config(text=player1_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 == 0 and(buttons[i][0]["text"] == 'O' and buttons[i][1]["text"] == 'O' and buttons[i][2]["text"] == 'O'):
                                player2_wins += 1
                                update2(player2_wins)
                                score_2.config(text=player2_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 == 0 and(buttons[0][i]['text'] == 'O' and buttons[1][i]['text'] == 'O' and buttons[2][i]['text'] == 'O'):
                                player2_wins += 1
                                update2(player2_wins)
                                score_2.config(text=player2_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 == 0 and(buttons[0][0]['text'] == 'O' and buttons[1][1]['text'] == 'O' and buttons[2][2]['text'] == 'O'):
                                player2_wins += 1
                                update2(player2_wins)
                                score_2.config(text=player2_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 == 0 and(buttons[0][2]['text'] == 'O' and buttons[1][1]['text'] == 'O' and buttons[2][0]['text'] == 'O'):
                                player2_wins += 1
                                update2(player2_wins)
                                score_2.config(text=player2_wins)
                                round()
                                win = True
                                return win
                            elif count == 9:
                                if (win == False):
                                    tie += 1
                                    round()
                                    return win
                                
                    winner1 = select()   
                    winner2 = select1()            
                    def terminer():
                        global player1_wins, player2_wins, tie
                        if player1_wins > player2_wins:
                            response = messagebox.showinfo('Resultat', f'{winner1[1]} won\n{winner1[1]} : {player1_wins}\n{winner2[1]} : {player2_wins}\nTie : {tie}')
                        elif player2_wins > player1_wins:
                            response = messagebox.showinfo('Resultat', f'{winner2[1]} won\n{winner2[1]} : {player1_wins}\n{winner1[1]} : {player2_wins}\nTie : {tie}')
                        else:
                            response = messagebox.showinfo('Resultat', f'Tie!\n{winner1[1]} : {player1_wins}\n{winner2[1]} : {player2_wins}\nTie : {tie}')
                        if response == 'ok':
                            retour()
                    # Creation de menu de tab_2
                    Exit = Menu(my_menu, tearoff=0)
                    Option = Menu(my_menu, tearoff=0)
                    Rejouer = Menu(my_menu, tearoff=0)
                    my_menu.add_cascade(label='Exit', menu=Exit)
                    my_menu.add_cascade(label='Option', menu=Option)
                    my_menu.add_cascade(label='Rejouer', menu=Rejouer)
                    Exit.add_command(label='Quitter', command=close)
                    Exit.add_separator()
                    Exit.add_command(label='Retour', command=retour)
                    Exit.add_command(label='Accueil', command=accueil) 
                    Option.add_command(label='About', command=about)
                    Rejouer.add_command(label='rejouer', command=rejouer)

                    # Creation de noms de joueurs 1 et 2
                    pl1label = Label(window, text=p1, font=('Arial',17), justify='left')
                    pl1label.place(x=10, y=100)
                    score_1 = Label(window, text=player1_wins, font=('Arial',17))
                    score_1.place(x=140, y=100)
                    pl2label = Label(window, text=p2, font=('Arial',17), justify='left')
                    pl2label.place(x=10, y=150)
                    score_2 = Label(window, text=player2_wins, font=('Arial',17))
                    score_2.place(x=140, y=150)
                    frame3 = Frame(window)
                    
                    # Creation de Buttons
                    frame3.pack(side=RIGHT)
                    buttons = []
                    for i in range(3):
                        row = []
                        for j in range(3):
                            button = Button(frame3, text="", height=6, width=13, command=lambda row=i, col=j: players(row, col))
                            button.grid(row=i, column=j)
                            row.append(button)
                        buttons.append(row)

                    frame6 = Frame(window)
                    frame6.place(x=36, y=250)
                    finish_button = Button(frame6,text= 'Terminer le match', width=13, height=2, command=terminer)
                    finish_button.pack()
                tab_2()
            elif (len(player_input1.get())) or(len(player_input2.get()) > 8) or (((len(player_input1.get())) and(len(player_input2.get()))) > 8):
                label1.config(fg='red')
                label2.config(fg='red')
                messagebox.showerror('Error!!',"OOPS. Vous avez saisi un(deux) nom(s) plus de lettres que nécessaires.\nRevérifier s'il vous plaît.")
            else:
                # the mandatory field is empty
                submit1.config(text='required', fg='red')
                player_input1.focus_set()
                player_input2.focus_set()
                messagebox.showerror('Error!!',"OOPS. Vous avez oublié un(deux) nom(s) que nécessaires.\nRevérifier s'il vous plaît.")

        # Button d'envoyer
        submit1 = Button(window, text='envoyer',width=10,height=2, command=next_step1)
        submit1.grid()
        
    def tab_3():
        # Fonction
        def retour():
            player1.destroy()
            player_input1.destroy()
            submit2.destroy()
            label1.destroy()
            text.destroy()
            tab_0()
            
        # Creation de base de donnees
        first_connection()
        
        # Destroy le contenu et le menu de tab_0
        welcome.destroy()
        frame1.destroy()
        frame2.destroy()
        button_debut1.destroy()
        button_debut2.destroy()
        my_menu.delete('Exit')
        my_menu.delete('Option')
        
        # Creation de menu de tab_1
        Exit = Menu(my_menu, tearoff=0)
        Option = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label='Exit', menu=Exit)
        my_menu.add_cascade(label='Option', menu=Option)
        Exit.add_command(label='Quitter', command=close)
        Exit.add_separator()
        Exit.add_command(label='Retour', command=retour)
        Option.add_command(label='About', command=about)
        
        # Joueur infos
        player1 = Label(window, text='Player 1 :')
        player1.grid(row=0, column=0, padx=10)
        player_input1 = Entry(window, width=50)
        player_input1.grid(row=0, column= 1, padx= 10, pady= 10)

        # Compteur de lettres de joueur
        str1 = StringVar(value=0)
        label1 = Label(window, textvariable=str1, width=2)
        label1.grid(row=0, column=2)
        player_input1.bind('<KeyRelease>',lambda x : str1.set(str(len(player_input1.get()))))
        
        # Required info
        text = Label(window, text='Il faut donner un nom de 8 lettres de plus!',font=("Courrier", 13), bd=1, relief=SUNKEN, bg='black', fg='white')
        text.place(relx=.5, rely=.5, anchor='center')
        
        # the user entered data in the mandatory entry: proceed to next step
        def next_step2():
            if player_input1.get() and(len(player_input1.get())) <= 8:
                #Creation des donnees
                p1 = player_input1.get()
                add(p1)
                add('boot')

                # Destroy le contenu de tab_3
                player1.destroy()
                player_input1.destroy()
                submit2.destroy()
                label1.destroy()
                text.destroy()

                def tab_4():
                    # Destroy de menu de tab_3
                    my_menu.delete('Exit')
                    my_menu.delete('Option')

                    # Fonctions
                    def retour():
                        rejouer()
                        frame4.destroy()
                        frame5.destroy()
                        finish_button.destroy()
                        pl1label.destroy()
                        pl2label.destroy()
                        score_1.destroy()
                        score_2.destroy()
                        for i in range(3):
                            for j in range(3):
                                buttons[i][j].destroy()
                        my_menu.delete('Rejouer')
                        drop()
                        tab_3()
                    
                    def accueil():
                        player1.destroy()
                        player_input1.destroy()
                        frame4.destroy()
                        frame5.destroy()
                        finish_button.destroy()
                        pl1label.destroy()
                        pl2label.destroy()
                        score_1.destroy()
                        score_2.destroy()
                        text.destroy()
                        for i in range(3):
                            for j in range(3):
                                buttons[i][j].destroy()
                        drop()
                        tab_0()
                    
                    def rejouer():
                        global count, clicked, win, user_wins, computer_wins
                        count = 0
                        clicked = True
                        win = False
                        user_wins = 0
                        computer_wins = 0
                        for i in range(3):
                            for j in range(3):
                                buttons[i][j].config(text='', state=NORMAL)
                                
                    def round():
                        global count, clicked, win
                        count = 0
                        clicked = True
                        win = False
                        for i in range(3):
                            for j in range(3):
                                buttons[i][j].config(text='', state=NORMAL)
                    
                    def click(row, col):
                        global clicked, count
                        if buttons[row][col]["text"] == "" and clicked == True:
                            buttons[row][col]["text"] = "X"
                            buttons[row][col].config(state=DISABLED)
                            count += 1
                            checkuserwinning()
                            computer_move()
                            
                    def computer_move():
                        global count
                        empty_cells = []
                        for i in range(3):
                            for j in range(3):
                                if buttons[i][j]["text"] == "":
                                    empty_cells.append((i, j))
                        if empty_cells:
                            row, col = choice(empty_cells)
                            buttons[row][col]["text"] = "O"
                            buttons[row][col].config(state=DISABLED)
                            count += 1
                            checkuserwinning()
                            
                    def checkuserwinning():
                        global count, win, user_wins, computer_wins, tie
                        for i in range(3):
                            if count % 2 != 0 and(buttons[i][0]["text"] == 'X' and buttons[i][1]["text"] == 'X' and buttons[i][2]["text"] == 'X'):
                                user_wins += 1
                                update1(user_wins)
                                score_1.config(text=user_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 != 0 and(buttons[0][i]['text'] == 'X' and buttons[1][i]['text'] == 'X' and buttons[2][i]['text'] == 'X'):
                                user_wins += 1
                                update1(user_wins)
                                score_1.config(text=user_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 != 0 and(buttons[0][0]['text'] == 'X' and buttons[1][1]['text'] == 'X' and buttons[2][2]['text'] == 'X'):
                                user_wins += 1
                                update1(user_wins)
                                score_1.config(text=user_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 != 0 and(buttons[0][2]['text'] == 'X' and buttons[1][1]['text'] == 'X' and buttons[2][0]['text'] == 'X'):
                                user_wins += 1
                                update1(user_wins)
                                score_1.config(text=user_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 == 0 and(buttons[i][0]["text"] == 'X' and buttons[i][1]["text"] == 'X' and buttons[i][2]["text"] == 'X'):
                                user_wins += 1
                                update1(user_wins)
                                score_1.config(text=user_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 == 0 and(buttons[0][i]['text'] == 'X' and buttons[1][i]['text'] == 'X' and buttons[2][i]['text'] == 'X'):
                                user_wins += 1
                                update1(user_wins)
                                score_1.config(text=user_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 == 0 and(buttons[0][0]['text'] == 'X' and buttons[1][1]['text'] == 'X' and buttons[2][2]['text'] == 'X'):
                                user_wins += 1
                                update1(user_wins)
                                score_1.config(text=user_wins)
                                round()
                                win = True
                                return win 
                            elif count % 2 == 0 and(buttons[0][2]['text'] == 'X' and buttons[1][1]['text'] == 'X' and buttons[2][0]['text'] == 'X'):
                                user_wins += 1
                                update1(user_wins)
                                score_1.config(text=user_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 == 0 and(buttons[i][0]["text"] == 'O' and buttons[i][1]["text"] == 'O' and buttons[i][2]["text"] == 'O'):
                                computer_wins += 1
                                update2(computer_wins)
                                score_2.config(text=computer_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 == 0 and(buttons[0][i]['text'] == 'O' and buttons[1][i]['text'] == 'O' and buttons[2][i]['text'] == 'O'):
                                computer_wins += 1
                                update2(computer_wins)
                                score_2.config(text=computer_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 == 0 and(buttons[0][0]['text'] == 'O' and buttons[1][1]['text'] == 'O' and buttons[2][2]['text'] == 'O'):
                                computer_wins += 1
                                update2(computer_wins)
                                score_2.config(text=computer_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 == 0 and(buttons[0][2]['text'] == 'O' and buttons[1][1]['text'] == 'O' and buttons[2][0]['text'] == 'O'):
                                computer_wins += 1
                                update2(computer_wins)
                                score_2.config(text=computer_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 != 0 and(buttons[i][0]["text"] == 'O' and buttons[i][1]["text"] == 'O' and buttons[i][2]["text"] == 'O'):
                                computer_wins += 1
                                update2(computer_wins)
                                score_2.config(text=computer_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 != 0 and(buttons[0][i]['text'] == 'O' and buttons[1][i]['text'] == 'O' and buttons[2][i]['text'] == 'O'):
                                computer_wins += 1
                                update2(computer_wins)
                                score_2.config(text=computer_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 != 0 and(buttons[0][0]['text'] == 'O' and buttons[1][1]['text'] == 'O' and buttons[2][2]['text'] == 'O'):
                                computer_wins += 1
                                update2(computer_wins)
                                score_2.config(text=computer_wins)
                                round()
                                win = True
                                return win
                            elif count % 2 != 0 and(buttons[0][2]['text'] == 'O' and buttons[1][1]['text'] == 'O' and buttons[2][0]['text'] == 'O'):
                                computer_wins += 1
                                update2(computer_wins)
                                score_2.config(text=computer_wins)
                                round()
                                win = True
                                return win
                            elif count == 9:
                                if (win == False):
                                    tie += 1
                                    round()
                                    return win
                    
                    winner = select()
                    def terminer():
                        global user_wins, computer_wins, tie
                        if user_wins > computer_wins:
                            response = messagebox.showinfo('Resultat', f'You are the winner\n{winner[1]} : {user_wins}\nThe boot : {computer_wins}\nTie : {tie}')
                        elif computer_wins > user_wins:
                            response = messagebox.showinfo('Resultat', f'You are lose this time try again!\n{winner[1]} : {user_wins}\nThe boot : {computer_wins}\nTie : {tie}')
                        else:
                            response = messagebox.showinfo('Resultat', f'Tie!\n{winner[1]} : {user_wins}\n The boot : {computer_wins}\nTie : {tie}')
                        if response == 'ok':
                                retour()
                                
                    # Creation de manu de tab_4
                    Exit = Menu(my_menu, tearoff=0)
                    Option = Menu(my_menu, tearoff=0)
                    Rejouer = Menu(my_menu, tearoff=0)
                    my_menu.add_cascade(label='Exit', menu=Exit)
                    my_menu.add_cascade(label='Option', menu=Option)
                    my_menu.add_cascade(label='Rejouer', menu=Rejouer)
                    Exit.add_command(label='Quitter', command=close)
                    Exit.add_separator()
                    Exit.add_command(label='Retour', command=retour)
                    Exit.add_command(label='Accueil', command=accueil)
                    Option.add_command(label='About', command=about)
                    Rejouer.add_command(label='rejouer', command=rejouer)

                    # Creation de noms de joueurs 1 et 2
                    pl1label = Label(window, text=p1, font=('Arial',17), justify='left')
                    pl1label.place(x=10, y=100)
                    score_1 = Label(window, text=user_wins, font=('Arial',17))
                    score_1.place(x=140, y=100)
                    pl2label = Label(window, text='boot', font=('Arial',17), justify='left')
                    pl2label.place(x=10, y=150)
                    score_2 = Label(window, text=computer_wins, font=('Arial',17))
                    score_2.place(x=140, y=150)
                    
                    # Creation de Buttons
                    frame4 = Frame(window)
                    frame4.pack(side=RIGHT)
                    buttons = []
                    for i in range(3):
                        row = []
                        for j in range(3):
                            button = Button(frame4, text="", height=6, width=13, command=lambda row=i, col=j: click(row, col))
                            button.grid(row=i, column=j)
                            row.append(button)
                        buttons.append(row)
                        
                    frame5 = Frame(window)
                    frame5.place(x=36, y=250)
                    finish_button = Button(frame5,text= 'Terminer le match', width=13, height=2, command=terminer)
                    finish_button.pack()
                tab_4()
            elif (len(player_input1.get()) > 8):
                label1.config(fg='red')
                messagebox.showerror('Error!!',"OOPS. Vous avez saisi le nom plus de lettres que nécessaires.\nRevérifier s'il vous plaît.")
            else:
                # the mandatory field is empty
                submit2.config(text='required', fg='red')
                player_input1.focus_set()
                messagebox.showerror('Error!!',"OOPS. Vous avez oublié le nom que nécessaires.\nRevérifier s'il vous plaît.")

        # Creation de Button d'envoyer
        submit2 = Button(window, text='envoyer',width=10,height=2, command=next_step2)
        submit2.grid()

    # Contenu de tab_0
    frame1 = Frame(window)
    frame1.pack(expand=True)
    welcome = Label(frame1, text='Bienvenue dans le jeux de Tic Tac Toe', font=('Arial',13))
    welcome.pack(expand=True)
    frame2 = Frame(window)
    frame2.pack(expand=True)
    button_debut1 = Button(frame2, text='VS Boot', font='20',width=10, height=2,command=tab_3)
    button_debut1.pack(side=LEFT)
    button_debut2 = Button(frame2, text='VS Ami', font='20',width=10, height=2, command=tab_1)
    button_debut2.pack(side=TOP)
tab_0()
window.mainloop()