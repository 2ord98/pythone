reddito =int(input ("inserisci il tuo reddito: "))

prima_aliquota= 0.23
seconda_aliquota= 0.25
terza_aliquota= 0.35
quarta_aliquota= 0.45

if reddito <= 15000 :
  aliquote = prima_aliquota*(reddito)
  
elif 15001 <= reddito <= 28000 :
  aliquote = seconda_aliquota*(reddito)
  
elif 28001 <= reddito <= 50000 :
  aliquote = terza_aliquota*(reddito)
  
else  :
  aliquote = quarta_aliquota*(reddito)
  

print ("dovrai pagare" , int(reddito-aliquote) , "euro")
