import subprocess


subprocess.call("ifconfig" , shell=True)


netad = input('what is the network adapter you want to use: ')

subprocess.call(f"ifconfig {netad} down" , shell=True)

while True:
    macaddr = input('what is the MAC addr you want? ')
    try:
        colons = macaddr.split(':')
        num = [float(colon) for colon in colons]
        break
    except ValueError:
        print("enter a valid number")

while True:
    macaddrconfirm = input(macaddr + ' Is this the MAC addr you want? ')
    if macaddrconfirm in ['yes', "y"]:
        print(f'changed old MAC to {macaddr} interface {netad} ')
        break
    elif macaddrconfirm in ['no','n']:
        print('try agine')
        continue
    else:
        print("invaild input")

subprocess.call(f"ifconfig {netad} hw ether {macaddr}" , shell=True)
subprocess.call(f"ifconfig {netad} up" , shell=True)


