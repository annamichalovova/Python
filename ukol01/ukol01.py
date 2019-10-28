kod= input("Zadejte binární kód: ")

a=0
b=8

c=((len(kod))/8)
c=int(c)
for i in range (0,c):
    print(chr(int(kod[a:b],2)),end="")
    a=a+8
    b=b+8
