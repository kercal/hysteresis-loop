import random
import copy
import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt
a = np.random.randint(0, 2, size=(10, 10))  # Generiere Random 10x10 Matrix mit 0 oder 1 in den Zellen

def neighbors(matrix, rowNumber, colNumber):    # Funktion die Anzahl Nachbarn und Nachbarn selbst in einer Matrix zurückgibt
    result = []
    for rowAdd in range(-1, 2):
        newRow = rowNumber + rowAdd
        if newRow >= 0 and newRow <= len(matrix)-1:
            for colAdd in range(-1, 2):
                newCol = colNumber + colAdd
                if newCol >= 0 and newCol <= len(matrix)-1:
                    if newCol == colNumber and newRow == rowNumber:
                        continue
                    result.append(matrix[newCol][newRow])
    return (len(result),result)


def hysterese(strength,matrix):
    aNew = copy.deepcopy(matrix)    # Kopiere Matrix für nächsten Schritt
    indexZ = -1                     
    for zeile in enumerate(matrix):     # Iteration über die Zeilen der Matrix
        indexZ += 1                     # Merke den Zeilen-Index
        for zelle in range(len(zeile[1])):  # Iteriere über Zellen in Zeile
            prob = 0                        # Initialisiere Wahrscheinlichkeit
            nb = neighbors(matrix,zeile[0],zelle)   
            n = nb[0]                       # speichere Anzahl der Nachbarn
            nbList = nb[1]                  # speichere Liste von Nachbarn
        
            for k in nbList:                # Iteriere über Nachbarn (Summenzeichen in der Formel)
                if k != zeile[1][zelle]:    # Wende Formel an
                    prob += k / n
            prob = prob * strength
        

            if strength > 1:                # Je nach Richtung, initialisiere Zufallsexperiment, um Zelle im nächsten Schritt zu bestimmen
                if zeile[1][zelle] == 0:
                    l = [0,1]
                else:
                    l = [1,0]
            else: 
                if zeile[1][zelle] == 0:
                    l = [0,1]
                else:
                    l = [0,1]
            
            newValue = random.choices(l,weights = [(1-prob)*100,prob*100])  # Bestimme Zelle für nächsten Schritt mit gegebener Wahrscheinlichkeit
            aNew[indexZ,zelle] = newValue[0]        # fülle Matrix für nächsten Schritt mit neuen Werten
    return(aNew)


print("Zufällig generiertes Schema:")
print(a)        # Gebe Startzustand zurück
print("")
s = float(input("Bitte geben Sie eine Stärke zwischen 0 und 2 ein (>1 ändert die Richtung): "))
print("")
for i in range(5):      # Simuliere das Modell für 5 Zeitschritte mit gegebener Stärke nach Definition in der Formel
    n = hysterese(s,a)
    a = n

print("Ergebnis nach 5 Schritten:")
print(a)        # Gebe Endzustand zurüc