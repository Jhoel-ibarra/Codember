

def buscar(lista):
   if len(lista) == 1: 
    return lista[0] 
   n = len(lista)//2
   nuevo = []
   print(len(lista))
   print(n)
   print(lista)
   for elem in range(n):
       nuevo.append(lista[elem*2])
      
   if len(lista) % 2 != 0:
      nuevo.pop(0)
      nuevo.append(lista[len(lista)-1])
   return buscar(nuevo)


if __name__ == "__main__":

   tecnologia  = [
     "Gorusuke",
     "DavidFabian",
     "ItziarZG",
     "edy WOLF",
     "MarcosGaPe",
     "Jose Jimenez",
     "Borja ",
     "Jhonathan Izquierdo Higuita",
     "MiLfeR322",
     "Sebastián Espínola",
     "Matias Luna",
     "Imanol Decima",
     "MarcoCasula",
     "MaríaBohórquez",
     "Renan",
     "IvanL'olivier",
     "Shonero",
     "Luichidev",
     "Faviola Narvaez",
     "Christopher Fuentes",
     "Kuro",
     "Juan Pablo Addeo",
     "Sergio Martínez",
     "Fran Enriquez González",
     "Diana",
     "tictools",
     "ConchaAsensio",
     "Emilio_Arreaza",
     "novamix",
     "Tomas Duclos",
     "Elaya",
     "Ignacio Palominos",
     "David C.",
     "Gerardo Felipe Conrado",
     "ElXuri",
     "David Borja Martinez",
     "JaviFelices",
     "CarlesSànchez",
     "Gorusuke",
     "DavidFabian",
     "ItziarZG",
     "edy WOLF",
     "MarcosGaPe",
     "Jose Jimenez",
     "Borja ",
  "Jhonathan Izquierdo Higuita",
  "MiLfeR322",
  "Sebastián Espínola",
  "Matias Luna",
  "Imanol Decima",
  "MarcoCasula",
  "MaríaBohórquez",
  "Renan",
  "IvanL'olivier",
  "Shonero",
  "Luichidev",
  "Faviola Narvaez",
  "Christopher Fuentes",
  "Kuro",
  "Juan Pablo Addeo",
  "Sergio Martínez",
  "Fran Enriquez González",
  "Diana",
  "tictools",
  "ConchaAsensio",
  "Emilio_Arreaza",
  "novamix",
  "Tomas Duclos",
  "Elaya",
  "Ignacio Palominos",
  "David C.",
  "Gerardo Felipe Conrado",
  "ElXuri",
  "David Borja Martinez",
  "JaviFelices",
  "CarlesSànchez",
  "Gorusuke",
  "DavidFabian",
  "ItziarZG",
  "edy WOLF",
  "MarcosGaPe",
  "Jose Jimenez",
  "Borja ",
  "Jhonathan Izquierdo Higuita",
  "MiLfeR322",
  "Sebastián Espínola",
  "Matias Luna",
  "Imanol Decima",
  "MarcoCasula",
  "MaríaBohórquez",
  "Renan",
  "IvanL'olivier",
  "Shonero",
  "Luichidev",
  "Faviola Narvaez",
  "Christopher Fuentes",
  "Kuro",
  "Juan Pablo Addeo",
  "Sergio Martínez",
  "Fran Enriquez González",
  "Diana",
  "tictools",
  "ConchaAsensio",
  "Emilio_Arreaza",
  "novamix",
  "Tomas Duclos",
  "Elaya",
  "Ignacio Palominos",
  "David C.",
  "Gerardo Felipe Conrado",
  "ElXuri",
  "David Borja Martinez",
  "JaviFelices",
  "CarlesSànchez"
    ] 
  # resultado = buscar(tecnologia)
   l = list(range(len(tecnologia)))
   bus = buscar(l)
   print(bus)
   print(tecnologia[bus])
