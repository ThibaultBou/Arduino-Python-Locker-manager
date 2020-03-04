from tkinter import *
from tkinter.ttk import *
import tkinter.ttk as ttk
import tkinter as tk
from tkinter.filedialog import*
from tkinter.messagebox import *
import serial
import time
from datetime import datetime
import sqlite3
import threading
from threading import Thread
from tkinter import messagebox


# ######################################################## #
                    # PARAMETRES  #
# ######################################################## #

Motdepasse = ""
RFIDLogin = "D47C1B2B98"
ONOFF = "1"
New = "Yes"
EtatCasier = "0"
ArduinoUnoSerial = serial.Serial("com4",9600)
delay = "3"

# ######################################################## #
                    # LOGIN  #
# ######################################################## #

def LoginFen():
    if Motdepasse != "":
        global EntryMDP,ConnexionFen
        ConnexionFen = Tk()
        ConnexionFen.geometry("314x120")
        EntryMDP= StringVar()
        ConnexionFen.title('Connexion')
        ConnexionFen.Label1 = Label(ConnexionFen)
        ConnexionFen.Label1.place(relx=0.38, rely=0.00, height=21, width=61)
        ConnexionFen.Label1.configure(text='''Bienvenue''')
        ConnexionFen.Label2 = Label(ConnexionFen)
        ConnexionFen.Label2.place(relx=0.06, rely=0.17, height=21, width=218)
        ConnexionFen.Label2.configure(text='''Pour continuer merci de vous connecter''')
        ConnexionFen.Entry1 = Entry(ConnexionFen, textvariable= EntryMDP, show='●')
        ConnexionFen.Entry1.place(relx=0.06, rely=0.38,height=20, relwidth=0.87)
        ConnexionFen.Entry1.configure(width=274)
        ConnexionFen.Button1 = Button(ConnexionFen)
        ConnexionFen.Button1.place(relx=0.19, rely=0.65, height=34, width=197)
        ConnexionFen.Button1.configure(pady="0")
        ConnexionFen.Button1.configure(text='''Se connecter''', command = Verification)
        ConnexionFen.Button1.configure(width=197)
        ConnexionFen.bind("<Return>", Verif)
        ConnexionFen.resizable(False, False)
        ConnexionFen.mainloop()
    else:
        Pass()

def Pass():
    process1 = threading.Thread(target=MainFen)
    process1.start()

def Verif(self):
    Verification()

def Verification():
    global EntryMDP
    if EntryMDP.get() == Motdepasse:
        ConnexionFen.destroy()
        Pass()
    else:
        showwarning('Erreur','Mot de passe incorrect')
        EntryMDP.set('')

# ######################################################## #
                       # FENETRE  #
# ######################################################## #

def MainFen():
    global NOM,PRENOM,RFIDEntry,treeview1,Fenetre,treeview2
    Fenetre = tk.Tk()
    Fenetre.geometry("686x363")
    Fenetre.title("Python Arduino")
    Fenetre.resizable(False, False)
    Fenetre.TNotebook1 = ttk.Notebook(Fenetre)
    Fenetre.TNotebook1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
    Fenetre.TNotebook1.configure(width=684)
    Fenetre.TNotebook1.configure(takefocus="")
    Fenetre.TNotebook1_t0 = Frame(Fenetre.TNotebook1)
    Fenetre.TNotebook1.add(Fenetre.TNotebook1_t0, padding=3)
    Fenetre.TNotebook1.tab(0, text="Utilisateurs", compound="left")
    Fenetre.TNotebook1_t0.configure(width=710)
    Fenetre.TNotebook1_t1 = Frame(Fenetre.TNotebook1)
    Fenetre.TNotebook1.add(Fenetre.TNotebook1_t1, padding=3)
    Fenetre.TNotebook1.tab(1, text="Logs",compound="left")
    Fenetre.TNotebook1_t1.configure(width=680)
    Fenetre.Labelframe1 = LabelFrame(Fenetre.TNotebook1_t0)
    Fenetre.Labelframe1.place(relx=0.01, rely=0.03, relheight=0.46, relwidth=0.35)
    Fenetre.Labelframe1.configure(text='''Profil''')
    Fenetre.Labelframe1.configure(width=240)
    Fenetre.Label1 = Label(Fenetre.Labelframe1)
    Fenetre.Label1.place(relx=0.04, rely=0.0)
    Fenetre.Label1.configure(text='''Nom''')
    Fenetre.Label2 = Label(Fenetre.Labelframe1)
    Fenetre.Label2.place(relx=0.04, rely=0.2)
    Fenetre.Label2.configure(text='''Prenom''')
    Fenetre.Label3 = Label(Fenetre.Labelframe1)
    Fenetre.Label3.place(relx=0.04, rely=0.4)
    Fenetre.Label3.configure(text='''RFID''')
    NOM = StringVar()
    PRENOM = StringVar()
    RFIDEntry = StringVar()
    Fenetre.Entry1 = Entry(Fenetre.Labelframe1,textvariable= NOM)
    Fenetre.Entry1.place(relx=0.25, rely=0.0, relwidth=0.68)
    Fenetre.Entry2 = Entry(Fenetre.Labelframe1,textvariable= PRENOM)
    Fenetre.Entry2.place(relx=0.25, rely=0.2, relwidth=0.68)
    Fenetre.Entry3 = Entry(Fenetre.Labelframe1,textvariable= RFIDEntry)
    Fenetre.Entry3.place(relx=0.25, rely=0.4, relwidth=0.68)
    Radio2 = IntVar()
    Radio2.set("1")
    Fenetre.Button2 = Button(Fenetre.Labelframe1)
    Fenetre.Button2.place(relx=0.15, rely=0.65, height=34, width=155)
    Fenetre.Button2.configure(text='''Sauvegarder''',command = Sauvegarder)
    Fenetre.Labelframe2 = LabelFrame(Fenetre.TNotebook1_t0)
    Fenetre.Labelframe2.place(relx=0.01, rely=0.5, relheight=0.34, relwidth=0.35)
    Fenetre.Labelframe2.configure(text='''Paramètres casier''')
    Fenetre.Label5 = Label(Fenetre.Labelframe2)
    Fenetre.Label5.place(relx=0.04, rely=0.19)
    Fenetre.Label5.configure(text='''Etat''')
    Fenetre.Radiobutton3 = Radiobutton(Fenetre.Labelframe2)
    Fenetre.Radiobutton3.place(relx=0.21, rely=0.19)
    Fenetre.Radiobutton3.configure(text='''Activé''',variable = Radio2,value="1",command = CasierActivé)
    Fenetre.Radiobutton4 = Radiobutton(Fenetre.Labelframe2)
    Fenetre.Radiobutton4.place(relx=0.54, rely=0.19,)
    Fenetre.Radiobutton4.configure(text='''Desactivé''',variable = Radio2,value="2",command = CasierDesactivé)
    Fenetre.Button3 = Button(Fenetre.Labelframe2)
    Fenetre.Button3.place(relx=0.04, rely=0.55, height=34, width=97)
    Fenetre.Button3.configure(text='''Ouvrir''')
    Fenetre.Button4 = Button(Fenetre.Labelframe2)
    Fenetre.Button4.place(relx=0.54, rely=0.55, height=34, width=97)
    Fenetre.Button4.configure(text='''Fermer''')
    Fenetre.Label6 = Label(Fenetre.TNotebook1_t0)
    Fenetre.Label6.place(relx=0.01, rely=0.885)
    Fenetre.Label6.configure(text='''Base de données''')
    Fenetre.Button5 = Button(Fenetre.TNotebook1_t0)
    Fenetre.Button5.place(relx=0.16, rely=0.86, height=34, width=127)
    Fenetre.Button5.configure(text='''Selectionner''',command = Browse)
    Fenetre.Button1 = Button(Fenetre.TNotebook1_t0)
    Fenetre.Button1.place(relx=0.38, rely=0.86, height=34, width=127)
    Fenetre.Button1.configure(text='''Supprimer l'utilisateur''',command = Delete)
    Fenetre.Button6 = Button(Fenetre.TNotebook1_t0)
    Fenetre.Button6.place(relx=0.585, rely=0.86, height=34, width=127)
    Fenetre.Button6.configure(text='''Charger l'utilisateur''',command = selectItem)
    Fenetre.Button6 = Button(Fenetre.TNotebook1_t0)
    Fenetre.Button6.place(relx=0.79, rely=0.86, height=34, width=127)
    Fenetre.Button6.configure(text='''Modifier RFID''',command = ModifRFID)
    Fenetre.treeview1 = Treeview(Fenetre.TNotebook1_t0)
    Fenetre.treeview1.place(relx=0.38, rely=0.06, relheight=0.76, relwidth=0.6)
    Fenetre.treeview1.configure(columns = ("Col1","Col2","Col3"), show='headings')
    Fenetre.treeview1.heading("#1",text="ID")
    Fenetre.treeview1.heading("#1",anchor="center")
    Fenetre.treeview1.column("#1",width="50")
    Fenetre.treeview1.column("#1",minwidth="20")
    Fenetre.treeview1.column("#1",stretch="1")
    Fenetre.treeview1.column("#1",anchor="w")
    Fenetre.treeview1.heading("#2",text="Nom")
    Fenetre.treeview1.heading("#2",anchor="center")
    Fenetre.treeview1.column("#2",width="125")
    Fenetre.treeview1.column("#2",minwidth="20")
    Fenetre.treeview1.column("#2",stretch="1")
    Fenetre.treeview1.column("#2",anchor="w")
    Fenetre.treeview1.heading("#3",text="Prenom")
    Fenetre.treeview1.heading("#3",anchor="center")
    Fenetre.treeview1.column("#3",width="125")
    Fenetre.treeview1.column("#3",minwidth="20")
    Fenetre.treeview1.column("#3",stretch="1")
    Fenetre.treeview1.column("#3",anchor="w")
    Fenetre.treeview2 = Treeview(Fenetre.TNotebook1_t1)
    Fenetre.treeview2.place(relx=0.01, rely=0.03, relheight=0.94, relwidth=0.97)
    Fenetre.treeview2.configure(columns = ("column0","column1","column2","column3","column4"), show='headings')
    Fenetre.treeview2.heading("#1",text="ID")
    Fenetre.treeview2.heading("#1",anchor="center")
    Fenetre.treeview2.column("#1",width="50")
    Fenetre.treeview2.column("#1",minwidth="20")
    Fenetre.treeview2.column("#1",stretch="1")
    Fenetre.treeview2.column("#1",anchor="w")
    Fenetre.treeview2.heading("#2",text="Nom")
    Fenetre.treeview2.heading("#2",anchor="center")
    Fenetre.treeview2.column("#2",width="160")
    Fenetre.treeview2.column("#2",minwidth="20")
    Fenetre.treeview2.column("#2",stretch="1")
    Fenetre.treeview2.column("#2",anchor="w")
    Fenetre.treeview2.heading("#3",text="Prenom")
    Fenetre.treeview2.heading("#3",anchor="center")
    Fenetre.treeview2.column("#3",width="160")
    Fenetre.treeview2.column("#3",minwidth="20")
    Fenetre.treeview2.column("#3",stretch="1")
    Fenetre.treeview2.column("#3",anchor="w")
    Fenetre.treeview2.heading("#4",text="Heure")
    Fenetre.treeview2.heading("#4",anchor="center")
    Fenetre.treeview2.column("#4",width="160")
    Fenetre.treeview2.column("#4",minwidth="20")
    Fenetre.treeview2.column("#4",stretch="1")
    Fenetre.treeview2.column("#4",anchor="w")
    Fenetre.treeview2.heading("#5",text="RFID")
    Fenetre.treeview2.heading("#5",anchor="center")
    Fenetre.treeview2.column("#5",width="115")
    Fenetre.treeview2.column("#5",minwidth="20")
    Fenetre.treeview2.column("#5",stretch="1")
    Fenetre.treeview2.column("#5",anchor="w")
    showwarning('Message','Commencez par selectionner une base de données')
    Fenetre.mainloop()

# ######################################################## #
                    # LOGIN  #
# ######################################################## #

    # ################ #
        # Edit User #
    # ################ #

def ItemData():
    global TreeData
    curItem = Fenetre.treeview1.focus()
    TreeData = Fenetre.treeview1.item(curItem)
    TreeData = str(TreeData)
    TreeData = TreeData.replace("'",'').replace(" ",'').replace("}",'').replace("{",'').replace("[",'').replace("]",'').replace(":",'').replace("image",'').replace("values",'').replace("open0",'').replace("tags",'').replace("text",'').replace(",,",'').replace(",",' ')
    TreeData = TreeData.split()

def selectItem():
    global New,RFIDEntry , NOM ,PRENOM,ID
    ItemData()
    RFIDEntry.set('')
    NOM.set('')
    PRENOM.set('')
    RFIDEntry.set(TreeData[3])
    NOM.set(TreeData[1])
    PRENOM.set(TreeData[2])
    ID = TreeData[0]
    New = "No"

def Delete() :
    global RFIDEntry, PRENOM, NOM,New
    ItemData()
    conn = sqlite3.connect(adresse)
    cur = conn.cursor()
    cur.execute('DELETE FROM utilisateurs WHERE id = (?)', (TreeData[0],))
    conn.commit()
    conn.close()
    RFIDEntry.set('')
    NOM.set('')
    PRENOM.set('')
    New = "Yes"
    LoadTree()

def Sauvegarder():
    global RFIDEntry, PRENOM, NOM, New,ID
    Nom = NOM.get()
    Prenom = PRENOM.get()
    RFID = RFIDEntry.get()
    if New == "Yes":
        conn = sqlite3.connect(adresse)
        cur = conn.cursor()
        cur.execute('''INSERT INTO utilisateurs(Nom, Prenom, RFID)VALUES(?,?,?)''', (Nom, Prenom, RFID,))
        conn.commit()
        conn.close()
        RFIDEntry.set('')
        NOM.set('')
        PRENOM.set('')
        LoadTree()
    else:
        conn = sqlite3.connect(adresse)
        cur = conn.cursor()
        cur.execute("UPDATE utilisateurs SET Nom = ?, Prenom = ? , RFID = ? WHERE ID = ?", (Nom, Prenom, RFID, ID,))
        conn.commit()
        conn.close()
        RFIDEntry.set('')
        NOM.set('')
        PRENOM.set('')
        LoadTree()
        showwarning('Avertissement','Modification effectué avec succés')
        New = "Yes"

    # ################ #
       # Read RFID #
    # ################ #

def RFIDSysteme():
    global Reader,EtatCasier,DataFinal
    Reader = "1"
    RFIDRead2 = ""
    RFIDOLD = ""
    while True:
        if Reader == "1":
            if ONOFF == "1":
                while ArduinoUnoSerial.inWaiting() > 0:
                        RFIDRead2 = ArduinoUnoSerial.readline().decode('UTF-8')
                        RFIDRead2 = RFIDRead2.replace('\r\n','')

                        conn = sqlite3.connect(adresse)
                        cur = conn.cursor()
                        cur.execute("SELECT * FROM utilisateurs")
                        rows = cur.fetchall()
                        for row in rows:
                            if RFIDRead2 in row:
                                cur.execute("SELECT * FROM utilisateurs WHERE RFID = ?", [RFIDRead2,])
                                DataFinal = cur.fetchall()
                                DataFinal = str(DataFinal).replace(' ','').replace("'",'').replace(","," ").replace("[(","").replace(")]","").split()
                                cur = conn.cursor()
                                date = time.strftime("%d/%m/%Y %H:%M:%S")
                                cur.execute('''INSERT INTO logs(Nom, Prenom, Heure, RFID)VALUES(?,?,?,?)''', (DataFinal[1], DataFinal[2], date, RFIDRead2))
                                conn.commit()
                                NomPrenom = (DataFinal[1].upper() + " " + DataFinal[2])
                                LoadTree()
                                ArduinoUnoSerial.write(NomPrenom.encode())
            else:
                showwarning('Erreur','Casier désactivé')


   # ################ #
     # Charger les datas #
    # ################ #

def LoadTree():
    global treeview1, treeview2
    for item in Fenetre.treeview1.get_children():
        Fenetre.treeview1.delete(item)
    for item in Fenetre.treeview2.get_children():
        Fenetre.treeview2.delete(item)
    conn = sqlite3.connect(adresse)
    cur = conn.cursor()
    cur.execute("SELECT * FROM utilisateurs")
    rows = cur.fetchall()
    for row in rows:
        Fenetre.treeview1.insert("", tk.END, values=row)
    conn.close()
    conn = sqlite3.connect(adresse)
    cur = conn.cursor()
    cur.execute("SELECT * FROM logs")
    rows = cur.fetchall()
    for row in reversed(rows):
        Fenetre.treeview2.insert("", tk.END, values= row)
    conn.close()

    # ################ #
    #  Ouverture Auto  #
    # ################ #

def ModifRFID():
    global RFIDEntry,Reader
    Reader = "0"
    messagebox.showinfo("Message", "Passez votre carte puis cliquez sur OK")
    while ArduinoUnoSerial.inWaiting() > 0:
        RFIDRead = ArduinoUnoSerial.readline().decode('UTF-8')
        RFIDRead = RFIDRead.replace('\r\n','')
    RFIDEntry.set(RFIDRead)
    Reader = "1"

##    # ################ #
##        # Arduino #
##    # ################ #
##
##def ArduOpen():
##    ArduinoUnoSerial.write('1'.encode())
##    print("Arduino : Ouvert")
##
##def ArduLock():
##    ArduinoUnoSerial.write('0'.encode())
##    print("Arduino : Fermé")
##
##    # ################ #
##        # Casier #
##    # ################ #
##
##def Open():
##    global EtatCasier
##    if ONOFF == "1":
##        if EtatCasier =="0":
##            EtatCasier = "1"
##            ArduOpen()
##        else:
##            showwarning('Erreur','Casier déja ouvert')
##    else:
##        showwarning('Erreur','Casier désactivé')
##
##def Close():
##    global EtatCasier
##    if EtatCasier =="1":
##        EtatCasier = "0"
##        ArduLock()
##    else:
##        showwarning('Erreur','Casier déja fermé')

    # ################ #
        # Etat #
    # ################ #

def CasierActivé():
    global ONOFF
    ONOFF = "1"

def CasierDesactivé():
    global ONOFF
    ONOFF = "0"

    # ################ #
        # Browse #
    # ################ #

def Browse():
    global adresse,conn
    Tk().withdraw()
    adresse = askopenfilename(title="Ouvrir un fichier Texte",filetypes=[('db files','.db'),('all files','.*')])
    conn = sqlite3.connect(adresse)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         Nom TEXT,
         Prenom TEXT,
         Heure TEXT,
         RFID TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS utilisateurs(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         Nom TEXT,
         Prenom TEXT,
         RFID TEXT
    )
    """)
    conn.commit()
    LoadTree()
    process2 = threading.Thread(target=RFIDSysteme)
    process2.start()

LoginFen()