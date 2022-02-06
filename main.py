


print("===================================================")
print("Benvenuto nella calcolatrice morente di Mada")
print("===================================================")
print(" ")

continua=True
while continua:

    #Acquisizione dati
    x=input("Primo numero: ")
    segno=input("Operazione:[+,-,*,/] ")
    y=input("Secondo numero: ")

    #Verifica dati
    if not(x.isdigit() and y.isdigit() and (segno=="+" or segno=="-" or segno=="*" or segno=="/")):
        print("Dati errati")
        continue

    #Elaborazione dati

    x=int(x)
    y=int(y)
    risultato=0
    
    #By NorbyVevo
    """ if segno in list('+-*/'):
        risultato=eval(str(x)+segno+str(y)) """
        

    if segno=="+":
        risultato=x+y
    if segno=="-":
        risultato=x-y
    if segno=="*":
        risultato=x*y
    if segno=="/":
        risultato=x/y


    print("Il risultato è: ",risultato)
    continua=(input("Vuoi continuare? [y]"))=="y"

print("Chiusura in corso")





