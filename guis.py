#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from functions import *
import webbrowser


def help():
    webbrowser.open('https://www.exnihil.io/pychat/help/help.pdf')


def gui_login():
    def registerbutton(event):
        gui_register()

    def loginbutton():
        username = str(username_entry.get())
        password = str(password_entry.get())
        if username and password:
            log = login(username, password)
            if log is True:
                guilogin.destroy()
                gui_menu(username, password)
            elif log is False:
                showwarning("ERR2", "NOM D'UTILISATEUR OU MOT DE PASSE INVALIDE")
                password_textvariable.set('')

    def enter(event):
        loginbutton()

    guilogin = Tk()
    set_icon(guilogin)
    guilogin.resizable(width=FALSE, height=FALSE)
    guilogin.title("PYCHAT | CONNEXION")
    guilogin.geometry("300x150")

    password_textvariable = StringVar()
    username_textvariable = StringVar()

    username_text = Label(guilogin, text="Nom d'utilisateur:")
    username_entry = Entry(guilogin, textvariable=username_textvariable, width=30)

    password_text = Label(guilogin, text="Mot de passe:")
    password_entry = Entry(guilogin, textvariable=password_textvariable, show="*", width=30)

    button = Button(guilogin, text="Se connecter", command=loginbutton)

    link = Label(guilogin, text="S'inscrire", fg="blue", cursor="hand2")

    username_text.pack()
    username_entry.pack()
    password_text.pack()
    password_entry.pack()
    button.pack()
    link.pack()
    username_entry.bind("<Return>", enter)
    password_entry.bind("<Return>", enter)
    link.bind("<Button-1>", registerbutton)

    guilogin.mainloop()


def gui_register():
    def resgisterbutton():
        username = str(username_entry.get())
        password = str(password_entry.get())
        first_name = str(first_name_entry.get())
        last_name = str(last_name_entry.get())
        email = str(email_entry.get())
        if username and password and first_name and last_name and email:
            if 16 >= len(password) >= 8:
                password_test = True
            else:
                password_test = False
            email_regex = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
            if email_regex is not None and password_test is True:
                log = register(username, password, first_name, last_name, email)
                if log is True:
                    registerwindow.destroy()
                elif log is False:
                    showwarning('ERR4', "NOM D'UTILISATEUR OU EMAIL NON DISPONIBLE")
            else:
                showwarning('ERREUR', 'EMAIL OU MOT DE PASSE INVALIDE')

    def enter(event):
        resgisterbutton()

    registerwindow = Tk()
    registerwindow.resizable(width=FALSE, height=FALSE)
    set_icon(registerwindow)
    registerwindow.title("PYCHAT | INSCRIPTION")

    username_textvariable = StringVar()
    password_textvariable = StringVar()
    first_name_textvariable = StringVar()
    last_name_textvariable = StringVar()
    email_textvariable = StringVar()

    username_text = Label(registerwindow, text="Nom d'utilisateur:")
    username_entry = Entry(registerwindow, textvariable=username_textvariable, width=50)
    username_entry.bind("<Return>", enter)

    password_text = Label(registerwindow, text="Mot de passe:")
    password_entry = Entry(registerwindow, textvariable=password_textvariable, show="*", width=50)
    password_entry.bind("<Return>", enter)

    first_name_text = Label(registerwindow, text="Prénom:")
    first_name_entry = Entry(registerwindow, textvariable=first_name_textvariable, show="", width=50)
    first_name_entry.bind("<Return>", enter)

    last_name_text = Label(registerwindow, text="Nom de famille:")
    last_name_entry = Entry(registerwindow, textvariable=last_name_textvariable, show="", width=50)
    last_name_entry.bind("<Return>", enter)

    email_text = Label(registerwindow, text="email:")
    email_entry = Entry(registerwindow, textvariable=email_textvariable, show="", width=50)
    email_entry.bind("<Return>", enter)

    button = Button(registerwindow, text="S'inscrire", command=resgisterbutton)

    username_text.pack()
    username_entry.pack()
    password_text.pack()
    password_entry.pack()
    first_name_text.pack()
    first_name_entry.pack()
    last_name_text.pack()
    last_name_entry.pack()
    email_text.pack()
    email_entry.pack()
    button.pack()
    registerwindow.mainloop()


def gui_join(a, b):
    def join_chan_call_gui():
        guimenu.destroy()
        gui_join(username, userpassword)

    def create_chan():
        guimenu.destroy()
        gui_create(username, userpassword)

    global username, userpassword, guimenu
    username = a
    userpassword = b

    def join_chan():
        channel = str(channel_id_entry.get())
        password = str(channel_password_entry.get())
        id_regex = re.match(r"^[#]*\d+$", channel)
        id_regex2 = re.match(r"^[#]+\d+$", channel)
        if channel:
            if id_regex is not None:
                if id_regex2 is not None:
                    channel = channel[1:]
                con = connexion_channel(channel, password)
                if con is True:
                    guimenu.destroy()
                    gui_chat(username, userpassword, channel, password)
                elif con is False:
                    showwarning("ERR4", "ID OU MOT DE PASSE INVALIDE")
            else:
                showwarning("ERR4", "ID OU MOT DE PASSE INVALIDE")

    def enter(event):
        join_chan()

    guimenu = Tk()
    set_icon(guimenu)
    guimenu.title("PYCHAT | REJOINDRE UN CANAL")
    guimenu.geometry("300x150")
    guimenu.resizable(width=FALSE, height=FALSE)
    menubar = Menu(guimenu)
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Créer", command=create_chan)
    menu1.add_command(label="Rejoindre", command=join_chan_call_gui)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=guimenu.quit)
    menubar.add_cascade(label="Canal", menu=menu1)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="Manuel en ligne", command=help)
    menubar.add_cascade(label="Aide", menu=menu3)

    guimenu.config(menu=menubar)

    channel_id_textvariable = StringVar()
    join_channel_text_id = Label(guimenu, text="ID du canal à rejoindre:")
    channel_id_entry = Entry(guimenu, textvariable=channel_id_textvariable, width=30)
    channel_id_entry.bind("<Return>", enter)

    channel_password_textvariable = StringVar()
    join_channel_text_password = Label(guimenu, text="Mot de passe du canal à rejoindre:")
    channel_password_entry = Entry(guimenu, textvariable=channel_password_textvariable, width=30)
    channel_password_entry.bind("<Return>", enter)

    button1 = Button(guimenu, text="Rejoindre le canal", command=join_chan)

    join_channel_text_id.pack()
    channel_id_entry.pack()
    join_channel_text_password.pack()
    channel_password_entry.pack()
    button1.pack()

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
        channel = str(channel_name_entry.get())
        password = str(channel_password_entry.get())
        if channel:
            state = new_channel(a, channel, password)
            if state[0] is True:
                guimenu.destroy()
                gui_chat(a, b, state[1], password)

    def enter(event):
        create_channel()

    guimenu = Tk()
    set_icon(guimenu)
    guimenu.title("PYCHAT | CRÉER UN CANAL")
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
    menu3.add_command(label="Manuel en ligne", command=help)
    menubar.add_cascade(label="Aide", menu=menu3)

    guimenu.config(menu=menubar)

    channel_name_textvariable = StringVar()
    create_channel_text_name = Label(guimenu, text="Nom du canal à créer:")
    channel_name_entry = Entry(guimenu, textvariable=channel_name_textvariable, width=30)
    channel_name_entry.bind("<Return>", enter)

    channel_password_textvariable = StringVar()
    create_channel_text_password = Label(guimenu, text="PASSWORD du canal à créer:")
    channel_password_entry = Entry(guimenu, textvariable=channel_password_textvariable, width=30)
    channel_password_entry.bind("<Return>", enter)

    button2 = Button(guimenu, text="Créer le canal", command=create_channel)

    create_channel_text_name.pack()
    channel_name_entry.pack()

    create_channel_text_password.pack()
    channel_password_entry.pack()

    button2.pack()

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
    set_icon(guimenu)
    guimenu.title("PYCHAT | MENU")
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
        if msg != "" and len(msg) <= 140:
            sendmsg(username, channel, password, msg)
            Message.set('')

    def enter(event):
        send()

    class RefreshMessages(Thread):
        def __init__(self):
            Thread.__init__(self)

        def run(self):
            global localidlist
            localidlist = []
            unread = 0
            while Running is True:
                try:
                    time.sleep(1)
                    global channel_name, guichat
                    channel_name = get_chan_name(channel)
                    idlist = loadidslist(channel, password)
                    if guichat.focus_get() is not None:
                        unread = 0
                    if unread == 0:
                        guichat.title('PYCHAT | #' + str(channel) + " - " + channel_name)
                    else:
                        guichat.title('(' + str(unread) + ') ' + 'PYCHAT | #' + str(channel) + " - " + channel_name)
                    if idlist == []:
                        localidlist.clear()
                        chat.config(state=NORMAL)
                        chat.delete(1.0, END)
                        chat.config(state=DISABLED)
                        unread = 0
                        guichat.title('PYCHAT | #' + str(channel) + " - " + channel_name)
                    elif idlist != "err3":
                        for item in idlist:
                            item = str(item)[1:-2]
                            if (item not in localidlist) is True:
                                data = get_msg(item, channel, password)
                                localidlist.append(item)
                                date = data[3]
                                date = "[" + str(date[2]) + "/" + date[1] + "/" + date[0] + " | " + str(date[3]) + ":" + \
                                       date[4] + ":" + date[5] + "] "
                                pseudo = "<" + str(data[1]) + "> "
                                textmessage = str(data[2]) + "\n"
                                text = date + pseudo + textmessage
                                chat.config(state=NORMAL)
                                chat.insert(END, text)
                                tag1_arg1 = str(len(localidlist)) + ".0"
                                tag1_arg2 = str(len(localidlist)) + "." + str(len(date))
                                tag2_arg1 = str(len(localidlist)) + "." + str(len(date))
                                tag2_arg2 = str(len(localidlist)) + "." + str(len(date) + len(pseudo))
                                chat.tag_add("date", tag1_arg1, tag1_arg2)
                                chat.tag_config("date", foreground="green")
                                chat.tag_add("pseudo", tag2_arg1, tag2_arg2)
                                chat.tag_config("pseudo", foreground="blue")
                                chat.config(state=DISABLED)
                                if guichat.focus_get() is None:
                                    unread += 1


                except:
                    pass

    def join_chan():
        global Running, localidlist
        close()
        Running = False
        localidlist.clear()
        gui_join(username, userpassword)

    def create_chan():
        global Running, localidlist
        close()
        Running = False
        localidlist.clear()
        gui_create(username, userpassword)

    def del_chan():
        if chan_delete(username, userpassword, channel, password) is True:
            global Running, localidlist
            close()
            Running = False
            localidlist.clear()
            gui_menu(username, userpassword)
        else:
            showwarning('ERR1', 'PAS LES DROITS')

    def clear_chan():
        if chan_clear(username, userpassword, channel, password) is True:
            global localidlist
            localidlist.clear()
            chat.config(state=NORMAL)
            chat.delete(1.0, END)
            chat.config(state=DISABLED)
        else:
            showwarning('ERR1', 'PAS LES DROITS')

    def rename_gui():

        def rename():
            new_channel_name = str(channel_rename_entry.get())
            if new_channel_name:
                if rename_chan(username, userpassword, channel, password, new_channel_name) is True:
                    guirename.destroy()
                    global channel_name
                    channel_name = new_channel_name
                    guichat.title('PYCHAT | #' + str(channel) + " - " + channel_name)

                else:
                    showwarning('ERR1', 'PAS LES DROITS')

        def enter(event):
            rename()

        guirename = Tk()
        set_icon(guirename)
        guirename.title("PYCHAT | RENOMMER LE CANAL")
        guirename.geometry("300x100")
        guirename.resizable(width=FALSE, height=FALSE)

        channel_rename_textvariable = StringVar()
        rename_channel_text_name = Label(guirename, text="Nom du canal:")
        channel_rename_entry = Entry(guirename, textvariable=channel_rename_textvariable, width=30)
        channel_rename_entry.bind("<Return>", enter)
        button2 = Button(guirename, text="Renommer le canal", command=rename)

        rename_channel_text_name.pack()
        channel_rename_entry.pack()
        button2.pack()
        guirename.mainloop()

    def close():
        global guichat
        guichat.destroy()

    global username, userpassword, launch, Running, guichat, chat, Entry1, Message, channel, channel_name, password, thread_1
    username = a
    userpassword = b
    channel = c
    password = d
    channel_name = get_chan_name(channel)
    launch = 1
    Running = True
    guichat = Tk()
    set_icon(guichat)
    guichat.title('PYCHAT | #' + str(channel) + " - " + channel_name)
    guichat.geometry("800x470")
    guichat.resizable(width=FALSE, height=FALSE)
    menubar = Menu(guichat)
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Créer", command=create_chan)
    menu1.add_command(label="Rejoindre", command=join_chan)
    menu1.add_command(label="Renommer le canal", command=rename_gui)
    menu1.add_command(label="Supprimer le canal", command=del_chan)
    menu1.add_command(label="Supprimer les messages", command=clear_chan)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=close)
    menubar.add_cascade(label="Canal", menu=menu1)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="Manuel en ligne", command=help)
    menubar.add_cascade(label="Aide", menu=menu3)

    guichat.config(menu=menubar)
    chat = Text(guichat, bd=0, bg="white", height="7", width="770", font="Arial")
    chat.config(state=DISABLED)
    scrollbar = Scrollbar(guichat, command=chat.yview)
    chat['yscrollcommand'] = scrollbar.set
    button1 = Button(guichat, text="Envoyer", command=send)
    Message = StringVar()
    Entry1 = Entry(guichat, textvariable=Message, bg='light gray', fg='black')
    Entry1.bind("<Return>", enter)
    scrollbar.place(x=780, y=0, height=390)
    chat.place(x=5, y=5, height=390, width=770)
    Entry1.place(x=5, y=410, height=30, width=650)
    button1.place(x=680, y=410, height=30, width=100)
    thread_1 = RefreshMessages()
    thread_1.start()
    guichat.mainloop()
    Running = False
