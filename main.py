x = 10000      #x ist die aktuelle Anzahl der noch übrigen Kokosnüsse 
b = 10000      #b ist die anzahl der Kokosnüsse, welche erst ganz am ende vom Durchgang geändert wird und zur Berechnung der bekommenen Anzahl an Kokosnüssen benötigt wird 
Nummer = 2022    #hier kann die Zahl des Piraten eingetragen werden, von welcher man die Anzahl wissen möchte
for a in range(1, Nummer + 1):   #hier wird für jeden piraten einzeln ein Durchgang gemacht
  y = 2023 - a    #Hier wird berechnet, wie viele Piraten übrig sind
  x = x - round(x/y, 0)    #Hier wird berechnet, wie viele Kokosnüsse der Pirat bekommt und diese Anzahl von den gesamten abgezogen
  print(f"Person {a} bekommt {b-x}")  #hier wird ausgegeben, wie viele Kokosnüsse die jeweilige Person bekommt
  b = x  #Hier wird b gleich x angepasst für die nächste Runde
  print(x)  #hier wird die Anzahl der Restlichen Kokosnüsse ausgegeben 



