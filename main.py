
for abc in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z"]:
  salida = open('english-'+abc+'.txt','w')
  fichero = open('english.txt', 'r')

  for linea in fichero:
    #print (len(linea))
    if(len(linea) == 9 and linea[0] == abc):
      salida.write(linea)  
  salida.close()
  fichero.close()


 
