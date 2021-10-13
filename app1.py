from tkinter import *
from tkinter import ttk
from pysnmp.hlapi import *


def model(*args):
    ip = feet.get()
    iterator = getCmd(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(".1.3.6.1.4.1.39165.1.1.0"))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print("ERROR")
        #print("errorIndication")

    elif errorStatus:
        print("ERROR")
        #print('%s at %s' % (errorStatus.prettyPrint(),
        #                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    elif errorIndex:
        print("ERROR")
    else:
        for varBind in varBinds:
            y=[x.prettyPrint() for x in varBind]
            z.set(y[-1])
            print(y[-1])
    pass


root = Tk()

root.title("System diagnostyczny IPTV PRO")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=10, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
z = StringVar()
ttk.Label(mainframe, textvariable=z).grid(column=2, row=2, sticky=(W, E))

#Przycisk (gdzie, jaki tekst, komenda na siatce kolumna 3 wiersz 3 )
ttk.Button(mainframe, text="Wyślij", command=model).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Wprowadź adres ip").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Model kamery").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", model)
root.mainloop()
