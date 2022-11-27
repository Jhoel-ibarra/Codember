import csv

valores ={
"97": "a",
"98": "b",
"99": "c",
"100": "d",
"101": "e",
"102": "f",
"103": "g",
"104": "h",
"105": "i",
"106": "j",
"107": "k",
"108": "l",
"109": "m",
"110": "n",
"111": "o",
"112": "p",
"113": "q",
"114": "r",
"115": "s",
"116": "t",
"117": "u",
"118": "v",
"119": "w",
"120": "x",
"121": "y",
"122": "z"
}

def traductor(text):
    aux_text = text
    prueba =""
    while len(aux_text) != 0:
        if aux_text[0] == " ":
            prueba += " "
            aux_text = aux_text[1:]
            print(prueba)
            print(aux_text)

        elif str(aux_text[:2]) in valores:
            prueba += valores[str(aux_text[:2])]
            aux_text = aux_text[2:]
        else:
            prueba += valores[str(aux_text[:3])]
            aux_text = aux_text[3:]

    return prueba        
            

   
    

if __name__ == "__main__":
   ''' f = open("data.csv")
   data = csv.reader(f, delimiter=" ")
   print(list(data))'''
   text = "11610497110107115 102111114 11210897121105110103 9911110010110998101114 11210810197115101 11510497114101"
   print(text)
   resultado = traductor(text)
   print(resultado)
   