from pysnmp.hlapi import *

def get(ip,oid):

    iterator = getCmd(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        print("Host:", ip, "OID:", oid)

        for varBind in varBinds:

            y=[x.prettyPrint() for x in varBind]
            print(y[-1])
    pass

print("kupa")
get("192.168.88.25",".1.3.6.1.4.1.39165.1.1.0")
