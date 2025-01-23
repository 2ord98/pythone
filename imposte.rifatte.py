reddito =int(input ("inserisci il tuo reddito: "))

seconda_aliquota= 0.23
terza_aliquota= 0.35
quarta_aliquota= 0.43


if reddito <= 28000 :
  aliquote_due = seconda_aliquota*(reddito)
  totale_da_pagare = reddito-(aliquote_due)

elif 28001 <= reddito <= 50000 :
  aliquote_due = seconda_aliquota*(28000)
  aliquote_tre= terza_aliquota*(reddito-28001) 
  totale_da_pagare = reddito - ( aliquote_due + aliquote_tre)

else  :
  aliquote_due = seconda_aliquota*(28000)
  aliquote_tre= terza_aliquota*(21999) 
  aliquote_quattro= quarta_aliquota*(reddito-50000)
  totale_da_pagare = reddito - ( aliquote_due + (aliquote_tre)+ aliquote_quattro)
  

print ("dovrai pagare" , int(totale_da_pagare) , "euro")
