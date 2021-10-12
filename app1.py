from tkinter import *
from tkinter import ttk
from pysnmp.hlapi import *

def calculate(*args):
    try:
        value = float(feet.get())
        z.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

def ip(*args):
    fname = feet.get()
    iterator = getCmd(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget((fname, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(".1.3.6.1.2.1.2.2.1.1.1"))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            y=[x.prettyPrint() for x in varBind]
            z.set(y[-1])

            print(y[-1])
    pass

#ip("172.16.0.2")

root = Tk()
root.title("oid pooler")

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
ttk.Button(mainframe, text="GET OID", command=ip).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="adres ip").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Stan otwarcia").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="to wynik").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", ip)

root.mainloop()
