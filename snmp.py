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

get("172.16.0.2")
