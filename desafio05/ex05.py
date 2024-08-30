from time import sleep

string = str(input('Digite uma string a qual deseja inverter: '))

pInv = ""

#iterando do ultimo carectere ao primeiro
for i in range(len(string) - 1, -1, -1):
    pInv += string[i]
print('INVERTENDO...')
sleep(2)

print("String invertida: {}".format(pInv))