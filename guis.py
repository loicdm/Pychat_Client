#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from functions import *

def gui_login():

    def registerbutton():
        gui_register()

    def loginbutton():
        username = str(entree_username.get())
        password = str(entree_password.get())
        log = login(username, password)
        if log == True:
            fenetre.destroy()
            gui_menu(username, password)
        elif log == "err1":
            showwarning('ERR1', 'SERVEUR INACESSIBLE')
        elif log == "err3":
            showwarning('ERR3', 'BASE DE DONNÉE INACESSIBLE')
        else:
            showwarning("ERR2", "NOM D'UTILISATEUR OU MOT DE PASSE INVALIDE")
            username_entry.set('')
            password_entry.set('')

    fenetre = Tk()
    fenetre.resizable(width=FALSE, height=FALSE)
    fenetre.title("Connexion")
    fenetre.geometry("300x150")

    username_entry = StringVar()
    password_entry = StringVar()

    username_text = Label(fenetre, text="Nom d'utilisateur:")
    entree_username = Entry(fenetre, textvariable=username_entry, width=30)

    password_text = Label(fenetre, text="Mot de passe:")
    entree_password = Entry(fenetre, textvariable=password_entry, show="*", width=30)

    bouton = Button(fenetre, text="Se connecter", command=loginbutton)

    link = Label(fenetre, text="S'inscrire", fg="blue", cursor="hand2")

    username_text.pack()
    entree_username.pack()
    password_text.pack()
    entree_password.pack()
    bouton.pack()
    link.pack()

    link.bind("<Button-1>", registerbutton)

    fenetre.mainloop()

def gui_register():

    def resgisterbutton():
        username = str(entree_username.get())
        password = str(entree_password.get())
        first_name = str(entree_first_name.get())
        last_name = str(entree_last_name.get())
        email = str(entree_email.get())
        if len(password) <= 16 and len(password) >= 8:
            password_test = True
        else:
            password_test = False
        email_regex = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
        if email_regex is not None and password_test == True:
            log = register(username, password, first_name, last_name, email)
            if log == True:
                registerwindow.destroy()
            elif log == "err1":
                showwarning('ERR1', 'SERVEUR INACESSIBLE')
            elif log == "err3":
                showwarning('ERR3', 'BASE DE DONNÉE INACESSIBLE')
            elif log == "err4":
                showwarning('ERR4', "NOM D'UTILISATEUR OU EMAIL NON DISPONIBLE")
        else:
            showwarning('ERREUR', 'EMAIL OU MOT DE PASSE INVALIDE')
    registerwindow = Tk()
    registerwindow.title("Inscription")

    username_entry = StringVar()
    password_entry = StringVar()
    first_name_entry = StringVar()
    last_name_entry = StringVar()
    email_entry = StringVar()

    username_text = Label(registerwindow, text="Nom d'utilisateur:")
    entree_username = Entry(registerwindow, textvariable=username_entry, width=50)

    password_text = Label(registerwindow, text="Mot de passe:")
    entree_password = Entry(registerwindow, textvariable=password_entry, show="*", width=50)

    first_name_text = Label(registerwindow, text="Prénom:")
    entree_first_name = Entry(registerwindow, textvariable=first_name_entry, show="", width=50)

    last_name_text = Label(registerwindow, text="Nom de famille:")
    entree_last_name = Entry(registerwindow, textvariable=last_name_entry, show="", width=50)

    email_text = Label(registerwindow, text="email:")
    entree_email = Entry(registerwindow, textvariable=email_entry, show="", width=50)

    bouton = Button(registerwindow, text="S'inscrire", command=resgisterbutton)

    username_text.pack()
    entree_username.pack()
    password_text.pack()
    entree_password.pack()
    first_name_text.pack()
    entree_first_name.pack()
    last_name_text.pack()
    entree_last_name.pack()
    email_text.pack()
    entree_email.pack()
    bouton.pack()
    registerwindow.mainloop()

def gui_join(a, b):
    def join_chan():
        guimenu.destroy()
        gui_join(username, userpassword)

    def create_chan():
        guimenu.destroy()
        gui_create(username, userpassword)

    global username, userpassword, guimenu
    username = a
    userpassword = b
    def join_chan():
        channel = str(entree_utilisateur_join_channel_id.get())
        password = str(entree_utilisateur_join_channel_password.get())
        id_regex = re.match(r"[#]*\d+", channel)
        id_regex2 = re.match(r"[#]+\d+", channel)
        if id_regex is not None:
            if id_regex2 is not None:
                channel = channel[1:]
            if connexion_channel(channel, password) is True:
                from gui_chat import gui_chat
                guimenu.destroy()
                gui_chat(username, userpassword, channel, password)

    guimenu = Tk()
    guimenu.title("Menu")
    guimenu.geometry("300x150")
    guimenu.resizable(width=FALSE, height=FALSE)
    menubar = Menu(guimenu)
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Créer", command=create_chan)
    menu1.add_command(label="Rejoindre", command=join_chan)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=guimenu.quit)
    menubar.add_cascade(label="Canal", menu=menu1)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="A propos")
    menubar.add_cascade(label="Aide", menu=menu3)

    guimenu.config(menu=menubar)


    join_channel_user_entry_id = StringVar()
    join_channel_text_id = Label(guimenu, text="ID du canal à rejoindre:")
    entree_utilisateur_join_channel_id = Entry(guimenu, textvariable=join_channel_user_entry_id, width=30)

    join_channel_user_entry_password = StringVar()
    join_channel_text_password = Label(guimenu, text="Mot de passe du canal à rejoindre:")
    entree_utilisateur_join_channel_password = Entry(guimenu, textvariable=join_channel_user_entry_password, width=30)

    bouton1 = Button(guimenu, text="Rejoindre le canal", command=join_chan)

    join_channel_text_id.pack()
    entree_utilisateur_join_channel_id.pack()
    join_channel_text_password.pack()
    entree_utilisateur_join_channel_password.pack()
    bouton1.pack()

    guimenu.mainloop()
    
def gui_create(a, b):
    def join_chan():
        guimenu.destroy()
        gui_join(username, userpassword)

    def create_chan():
        guimenu.destroy()
        gui_create(username, userpassword)
    global username, userpassword, guimenu
    username = a
    userpassword = b
    def create_channel():
        channel = str(entree_utilisateur_create_channel_id.get())
        password = str(entree_utilisateur_create_channel_password.get())
        if used_channel(channel, password) is False:
            state = new_channel(a, channel, password)
            if state[0] is True:
                guimenu.destroy()
                gui_chat(a, b, state[1], password)


    guimenu = Tk()
    guimenu.title("Menu")
    guimenu.geometry("300x150")
    guimenu.resizable(width=FALSE, height=FALSE)
    menubar = Menu(guimenu)
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Créer", command=create_chan)
    menu1.add_command(label="Rejoindre", command=join_chan)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=guimenu.quit)
    menubar.add_cascade(label="Canal", menu=menu1)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="A propos")
    menubar.add_cascade(label="Aide", menu=menu3)

    guimenu.config(menu=menubar)

    create_channel_user_entry_id = StringVar()
    create_channel_text_id = Label(guimenu, text="Nom du canal à créer:")
    entree_utilisateur_create_channel_id = Entry(guimenu, textvariable=create_channel_user_entry_id, width=30)

    create_channel_user_entry_password = StringVar()
    create_channel_text_password = Label(guimenu, text="PASSWORD du canal à créer:")
    entree_utilisateur_create_channel_password = Entry(guimenu, textvariable=create_channel_user_entry_password, width=30)

    bouton2 = Button(guimenu, text="Créer le canal", command=create_channel)

    create_channel_text_id.pack()
    entree_utilisateur_create_channel_id.pack()

    create_channel_text_password.pack()
    entree_utilisateur_create_channel_password.pack()

    bouton2.pack()

    guimenu.mainloop()
    
def gui_menu(a, b):
    def join_chan():
        guimenu.destroy()
        gui_join(username, password)

    def create_chan():
        guimenu.destroy()
        gui_create(username, password)

    global username, password, guimenu
    username = a
    password = b
    guimenu = Tk()
    guimenu.title("Menu")
    guimenu.geometry("320x90")
    guimenu.resizable(width=FALSE, height=FALSE)

    bouton1 = Button(guimenu, text="Rejoindre un canal", width="120", height="30", command=join_chan)
    bouton2 = Button(guimenu, text="Créer un canal", width="120", height="30", command=create_chan)

    bouton1.place(x=100, y=10, height=30, width=120)
    bouton2.place(x=100, y=50, height=30, width=120)


    guimenu.mainloop()
    
def gui_chat(a, b, c, d):
    def send():
        msg = str(Entry1.get())
        sendmsg(username, channel, password, msg)
        Message.set('')

    class RefreshMessages(Thread):
        def __init__(self):
            Thread.__init__(self)

        def run(self):
            localidlist = []
            while Running == True:
                try:
                    time.sleep(1)
                    global guichat
                    idlist = loadidslist(channel, password)
                    for item in idlist:
                        item = str(item)[1:-2]
                        if (item not in localidlist) is True:
                            data = get_msg(item, channel, password)
                            localidlist.append(item)
                            text = "[" + str(data[3]) + "] " + "<" + str(data[1]) + "> " + str(data[2]) + "\n"
                            chat.config(state=NORMAL)
                            chat.insert(END, text)
                            chat.config(state=DISABLED)
                except:
                    pass

    def join_chan():
        guichat.destroy()
        gui_join(username, password)

    def create_chan():
        guichat.destroy()
        gui_create(username, password)

    def del_chan():
        if chan_delete(username, userpassword, channel, password) is True:
            guichat.destroy()
            gui_menu(username, userpassword)
        else:
            showwarning('ERR1', 'PAS LES DROITS')

    def close():
        global Running
        Running = False

    global username, userpassword, launch, Running, guichat, chat, Entry1, Message, channel, password, thread_1
    username = a
    userpassword = b
    channel = c
    password = d
    channel_name = get_chan_name(channel)
    launch = 1
    Running = True
    guichat = Tk()
    guichat.title('PYCHAT #' + str(channel) + " - " + channel_name)
    guichat.geometry("800x450")
    guichat.resizable(width=FALSE, height=FALSE)
    menubar = Menu(guichat)
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Créer", command=create_chan)
    menu1.add_command(label="Rejoindre", command=join_chan)
    menu1.add_command(label="Supprimer le canal", command=del_chan)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=guichat.quit)
    menubar.add_cascade(label="Canal", menu=menu1)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="A propos")
    menubar.add_cascade(label="Aide", menu=menu3)

    guichat.config(menu=menubar)
    chat = Text(guichat, bd=0, bg="white", height="7", width="770", font="Arial")
    chat.config(state=DISABLED)
    scrollbar = Scrollbar(guichat, command=chat.yview)
    chat['yscrollcommand'] = scrollbar.set
    Button1 = Button(guichat, text="Envoyer", command=send)
    Message = StringVar()
    Entry1 = Entry(guichat, textvariable=Message, bg='bisque', fg='maroon')
    scrollbar.place(x=780, y=0, height=390)
    chat.place(x=5, y=5, height=390, width=770)
    Entry1.place(x=5, y=410, height=30, width=650)
    Button1.place(x=680, y=410, height=30, width=100)
    thread_1 = RefreshMessages()
    thread_1.start()
    guichat.mainloop()
    close()