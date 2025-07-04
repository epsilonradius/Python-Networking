import winreg as wrg


def hexconv(val):
    addr=""
    for ch in val:
        addr += ("%02x "% ord(ch))
    addr = addr.strip(" ").replace(" ",":")[0:17]
    return addr

def PrintNet():
    net = input(r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged")
    key = wrg.OpenKey(wrg.HKEY_LOCAL_MACHINE, net)
    print("net:" + net)
    #print("key:"  {key})
    print ('\n[*] Networks joined')
    for i in range(100):
        try:
            guid = wrg.EnumKey(key, i)
            print("guid: " + guid)
            netKey = wrg.OpenKey(key, str(guid))
            print("netkey: " + netKey)
            (n,addr,t) = wrg.EnumValue(netKey,5)
            (n,name,t) = wrg.EnumValue(netKey,4)
            macAddr = hexconv(addr)
            netName = str(name)
            print('[+] ' + netName + ' ' + macAddr)
            wrg.CloseKey(netKey)
        except:
            print("[-] Error")
            break
def main():
    PrintNet()
if __name__== "__main__":
    main()
