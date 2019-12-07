import tkinter
import sqlite3

db = sqlite3.connect('local.db')

# Detail Window
window = tkinter.Tk()

window.title("Viewer DB Regelmäßige Verben")

tkinter.Label(window, text = 'Infinitiv:').grid(row = 0, column = 0)
Infinitiv = tkinter.Entry(window)
Infinitiv.grid(row = 0, column = 1)
tkinter.Label(window, text = 'Praesens1PersonSingular:').grid(row = 1, column = 0)
Praesens1PersonSingular = tkinter.Entry(window)
Praesens1PersonSingular.grid(row = 1, column = 1)
tkinter.Label(window, text = 'Praesens2PersonSingular:').grid(row = 2, column = 0)
Praesens2PersonSingular = tkinter.Entry(window)
Praesens2PersonSingular.grid(row = 2, column = 1)
tkinter.Label(window, text = 'Praesens3PersonSingular:').grid(row = 3, column = 0)
Praesens3PersonSingular = tkinter.Entry(window)
Praesens3PersonSingular.grid(row = 3, column = 1)
tkinter.Label(window, text = 'Praeteritum1PersonSingular:').grid(row = 4, column = 0)
Praeteritum1PersonSingular = tkinter.Entry(window)
Praeteritum1PersonSingular.grid(row = 4, column = 1)
tkinter.Label(window, text = 'Praeteritum2PersonSingular:').grid(row = 5, column = 0)
Praeteritum2PersonSingular = tkinter.Entry(window)
Praeteritum2PersonSingular.grid(row = 5, column = 1)
tkinter.Label(window, text = 'Praeteritum3PersonSingular:').grid(row = 6, column = 0)
Praeteritum3PersonSingular = tkinter.Entry(window)
Praeteritum3PersonSingular.grid(row = 6, column = 1)
tkinter.Label(window, text = 'KonjunktivII1PersonSingular:').grid(row = 7, column = 0)
KonjunktivII1PersonSingular = tkinter.Entry(window)
KonjunktivII1PersonSingular.grid(row = 7, column = 1)
tkinter.Label(window, text = 'KonjunktivII2PersonSingular:').grid(row = 8, column = 0)
KonjunktivII2PersonSingular = tkinter.Entry(window)
KonjunktivII2PersonSingular.grid(row = 8, column = 1)
tkinter.Label(window, text = 'KonjunktivII3PersonSingular:').grid(row = 9, column = 0)
KonjunktivII3PersonSingular = tkinter.Entry(window)
KonjunktivII3PersonSingular.grid(row = 9, column = 1)
tkinter.Label(window, text = 'ImperativSingular:').grid(row = 10, column = 0)
ImperativSingular = tkinter.Entry(window)
ImperativSingular.grid(row = 10, column = 1)
tkinter.Label(window, text = 'ImperativPlural:').grid(row = 11, column = 0)
ImperativPlural = tkinter.Entry(window)
ImperativPlural.grid(row = 11, column = 1)
tkinter.Label(window, text = 'PerfektPartizip2:').grid(row = 12, column = 0)
PerfektPartizip2 = tkinter.Entry(window)
PerfektPartizip2.grid(row = 12, column = 1)
tkinter.Label(window, text = 'PerfektHilfsverb:').grid(row = 13, column = 0)
PerfektHilfsverb = tkinter.Entry(window)
PerfektHilfsverb.grid(row = 13, column = 1)

def LeseEintragVonDB(InfinitivName):
    Infinitiv.delete(0,tkinter.END)
    Praesens1PersonSingular.delete(0,tkinter.END)
    Praesens2PersonSingular.delete(0,tkinter.END)
    Praesens3PersonSingular.delete(0,tkinter.END)
    Praeteritum1PersonSingular.delete(0,tkinter.END)
    Praeteritum2PersonSingular.delete(0,tkinter.END)
    Praeteritum3PersonSingular.delete(0,tkinter.END)
    KonjunktivII1PersonSingular.delete(0,tkinter.END)
    KonjunktivII2PersonSingular.delete(0,tkinter.END)
    KonjunktivII3PersonSingular.delete(0,tkinter.END)
    ImperativSingular.delete(0,tkinter.END)
    ImperativPlural.delete(0,tkinter.END)
    PerfektPartizip2.delete(0,tkinter.END)
    PerfektHilfsverb.delete(0,tkinter.END)

    Infinitiv.insert(0,InfinitivName)
    db_result = db.execute('''SELECT Wortform
                          FROM RegelmäßigeVerben
                          WHERE Infinitiv='{}' AND Typ='{}' '''.format(InfinitivName, 'Praesens1PersonSingular')).fetchone()
    Praesens1PersonSingular.insert(0,db_result[0] if db_result is not None and len(db_result)>0 else "")
    db_result = db.execute('''SELECT Wortform
                          FROM RegelmäßigeVerben
                          WHERE Infinitiv='{}' AND Typ='{}' '''.format(InfinitivName, 'Praesens2PersonSingular')).fetchone()
    Praesens2PersonSingular.insert(0,db_result[0] if db_result is not None and len(db_result)>0 else "")
    db_result = db.execute('''SELECT Wortform
                          FROM RegelmäßigeVerben
                          WHERE Infinitiv='{}' AND Typ='{}' '''.format(InfinitivName, 'Praesens3PersonSingular')).fetchone()
    Praesens3PersonSingular.insert(0,db_result[0] if db_result is not None and len(db_result)>0 else "")
    db_result = db.execute('''SELECT Wortform
                          FROM RegelmäßigeVerben
                          WHERE Infinitiv='{}' AND Typ='{}' '''.format(InfinitivName, 'Praeteritum1PersonSingular')).fetchone()
    Praeteritum1PersonSingular.insert(0,db_result[0] if db_result is not None and len(db_result)>0 else "")
    db_result = db.execute('''SELECT Wortform
                          FROM RegelmäßigeVerben
                          WHERE Infinitiv='{}' AND Typ='{}' '''.format(InfinitivName, 'Praeteritum2PersonSingular')).fetchone()
    Praeteritum2PersonSingular.insert(0,db_result[0] if db_result is not None and len(db_result)>0 else "")
    db_result = db.execute('''SELECT Wortform
                          FROM RegelmäßigeVerben
                          WHERE Infinitiv='{}' AND Typ='{}' '''.format(InfinitivName, 'Praeteritum3PersonSingular')).fetchone()
    Praeteritum3PersonSingular.insert(0,db_result[0] if db_result is not None and len(db_result)>0 else "")
    db_result = db.execute('''SELECT Wortform
                          FROM RegelmäßigeVerben
                          WHERE Infinitiv='{}' AND Typ='{}' '''.format(InfinitivName, 'KonjunktivII1PersonSingular')).fetchone()
    KonjunktivII1PersonSingular.insert(0,db_result[0] if db_result is not None and len(db_result)>0 else "")
    db_result = db.execute('''SELECT Wortform
                          FROM RegelmäßigeVerben
                          WHERE Infinitiv='{}' AND Typ='{}' '''.format(InfinitivName, 'KonjunktivII2PersonSingular')).fetchone()
    KonjunktivII2PersonSingular.insert(0,db_result[0] if db_result is not None and len(db_result)>0 else "")
    db_result = db.execute('''SELECT Wortform
                          FROM RegelmäßigeVerben
                          WHERE Infinitiv='{}' AND Typ='{}' '''.format(InfinitivName, 'KonjunktivII3PersonSingular')).fetchone()
    KonjunktivII3PersonSingular.insert(0,db_result[0] if db_result is not None and len(db_result)>0 else "")
    db_result = db.execute('''SELECT Wortform
                          FROM RegelmäßigeVerben
                          WHERE Infinitiv='{}' AND Typ='{}' '''.format(InfinitivName, 'ImperativSingular')).fetchone()
    ImperativSingular.insert(0,db_result[0] if db_result is not None and len(db_result)>0 else "")
    db_result = db.execute('''SELECT Wortform
                          FROM RegelmäßigeVerben
                          WHERE Infinitiv='{}' AND Typ='{}' '''.format(InfinitivName, 'ImperativPlural')).fetchone()
    ImperativPlural.insert(0,db_result[0] if db_result is not None and len(db_result)>0 else "")
    db_result = db.execute('''SELECT Wortform
                          FROM RegelmäßigeVerben
                          WHERE Infinitiv='{}' AND Typ='{}' '''.format(InfinitivName, 'PerfektPartizip2')).fetchone()
    PerfektPartizip2.insert(0,db_result[0] if db_result is not None and len(db_result)>0 else "")
    db_result = db.execute('''SELECT Wortform
                          FROM RegelmäßigeVerben
                          WHERE Infinitiv='{}' AND Typ='{}' '''.format(InfinitivName, 'PerfektHilfsverb')).fetchone()
    PerfektHilfsverb.insert(0,db_result[0] if db_result is not None and len(db_result)>0 else "")

def UpdateOrInsertIntoDB(valInfinitiv, valTyp, valWortform):
    if valWortform is not None and valWortform.isspace() is False:
        db_result = db.execute('''SELECT id
                            FROM RegelmäßigeVerben
                            WHERE Infinitiv='{}' AND Typ='{}' '''.format(valInfinitiv, valTyp)).fetchone()
        if db_result is not None and len(db_result)>0:
            print('UPDATE RegelmäßigeVerben SET Infinitiv=\'{}\', Typ=\'{}\', Wortform=\'{}\' WHERE id={}'.format(valInfinitiv, valTyp, valWortform, db_result[0]))
            db.execute('UPDATE RegelmäßigeVerben SET Infinitiv=\'{}\', Typ=\'{}\', Wortform=\'{}\' WHERE id={}'.format(valInfinitiv, valTyp, valWortform, db_result[0]))
        else:
            print('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(valInfinitiv, valTyp, valWortform))
            db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(valInfinitiv, valTyp, valWortform))
        db.commit()

def SchreibeEintragNachDB():
    valInfinitiv = str(Infinitiv.get())
    if valInfinitiv is None or valInfinitiv.isspace():
        return

    UpdateOrInsertIntoDB(valInfinitiv, 'Infinitiv', valInfinitiv)
    UpdateOrInsertIntoDB(valInfinitiv, 'Praesens1PersonSingular', str(Praesens1PersonSingular.get()))  
    UpdateOrInsertIntoDB(valInfinitiv, 'Praesens2PersonSingular', str(Praesens2PersonSingular.get()))
    UpdateOrInsertIntoDB(valInfinitiv, 'Praesens3PersonSingular', str(Praesens3PersonSingular.get()))
    UpdateOrInsertIntoDB(valInfinitiv, 'Praeteritum1PersonSingular', str(Praeteritum1PersonSingular.get()))
    UpdateOrInsertIntoDB(valInfinitiv, 'Praeteritum2PersonSingular', str(Praeteritum2PersonSingular.get()))
    UpdateOrInsertIntoDB(valInfinitiv, 'Praeteritum3PersonSingular', str(Praeteritum3PersonSingular.get()))
    UpdateOrInsertIntoDB(valInfinitiv, 'KonjunktivII1PersonSingular', str(KonjunktivII1PersonSingular.get()))
    UpdateOrInsertIntoDB(valInfinitiv, 'KonjunktivII2PersonSingular', str(KonjunktivII2PersonSingular.get()))
    UpdateOrInsertIntoDB(valInfinitiv, 'KonjunktivII3PersonSingular', str(KonjunktivII3PersonSingular.get()))
    UpdateOrInsertIntoDB(valInfinitiv, 'ImperativSingular', str(ImperativSingular.get()))
    UpdateOrInsertIntoDB(valInfinitiv, 'ImperativPlural', str(ImperativPlural.get()))
    UpdateOrInsertIntoDB(valInfinitiv, 'PerfektPartizip2', str(PerfektPartizip2.get()))
    UpdateOrInsertIntoDB(valInfinitiv, 'PerfektHilfsverb', str(PerfektHilfsverb.get()))
    db.commit()

def ReadValuesFromDBButton_onClick():
    LeseEintragVonDB(str(Infinitiv.get()))

ReadValuesFromDBButton = tkinter.Button(window, text = "Lese Eintrag von DB", command = ReadValuesFromDBButton_onClick)
ReadValuesFromDBButton.grid(row = 14, column = 0)

def WriteValuesToDBButton_onClick():
    SchreibeEintragNachDB()

WriteValuesToDBButton = tkinter.Button(window, text = "Schreibe Eintrag in DB", command = WriteValuesToDBButton_onClick)
WriteValuesToDBButton.grid(row = 14, column = 1)

# Main Window
MainMenuWindow = tkinter.Tk()

MainMenuWindow.title("Wähle Eintrag aus")

def onLBselect(evt):
    try:
        # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print('You selected item {}: "{}"'.format(index, value))
        LeseEintragVonDB(value)
    except:
        pass

listboxNamen = tkinter.Listbox(master=MainMenuWindow, selectmode='browse')
db_result = db.execute('''SELECT Infinitiv
                          FROM RegelmäßigeVerben
                          GROUP BY Infinitiv''').fetchall()

for singleEntry in db_result:
    listboxNamen.insert('end', str(singleEntry[0]))

listboxNamen.pack(fill='both', expand=True)
listboxNamen.bind('<<ListboxSelect>>', onLBselect)

def on_closing():
    window.destroy()
    MainMenuWindow.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)
MainMenuWindow.protocol("WM_DELETE_WINDOW", on_closing)

MainMenuWindow.mainloop()