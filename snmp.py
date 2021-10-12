from pysnmp.hlapi import *

def get(fname):

    iterator = getCmd(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget((fname, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(".1.3.6.1.2.1.1.1.0"))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        print(varBinds)

        for varBind in varBinds:

            y=[x.prettyPrint() for x in varBind]
            print(y[-1])
    pass

def walk(host, oid):

    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData('public'),
                              UdpTransportTarget((host, 161)),
                              ContextData(),
                              ObjectType(ObjectIdentity(oid)),
                              lookupMib=False,
                              lexicographicMode=False):

        if errorIndication:
            print(errorIndication, file=sys.stderr)
            break

        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), file=sys.stderr)
            break

        else:
            for varBind in varBinds:
                 print('%s = %s' % varBind)

walk('192.168.88.25', '1.3.6.1.2.1.1.9.1.2')
get("192.168.88.25")
