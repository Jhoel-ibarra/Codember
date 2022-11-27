
import csv
#usr:@midudev eme:mi@gmail.com psw:123456 age:22 loc:bcn fll:82

#fll:111 eme:yrfa@gmail.com usr:@codember psw:123456 age:21 loc:World

#psw:11133 loc:Canary fll:333 usr:@pheralb eme:pheralb@gmail.com

#usr:@itziar age:19 loc:isle psw:aaa fll:222 eme:itzi@gmail.com

#El primer usuario SÍ es válido. Tiene todos los campos.
#El segundo usuario SÍ es válido. Tiene todos los campos.
#El tercer usuario NO es válido. Le falta el campo `age`.
#El cuarto usuario SÍ es válido. Tiene todos los campos..
    
def ordenar(data):
    nuevo= []
    aux =[]
    for elem in data:
      if elem != []:
        aux.extend(elem)
      else: 
        nuevo.append(aux)
        aux = []

    return nuevo

def Usuarios(data):
    cantidad = 0
    valores = ["usr:","eme:","psw:","age:","loc:","fll:"]
    correcto = []
    for fila in data:
        string = str(fila)
        n = 0
        for elem in valores:
            if string.count(elem) > 0:
               n = n+ 1
        if n == 6 : 
          cantidad += 1
          correcto.append(fila)       
           
            
                 

    return cantidad , correcto

if __name__ == "__main__":

   f = open("data.csv")
   data = csv.reader(f)
  # data = pd.read_csv("data.csv", header=0)
   nuevo = ordenar(data)
   n , lista= Usuarios(nuevo)
   print(lista[-1])
   print(n)
