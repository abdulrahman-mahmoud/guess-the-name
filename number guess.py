guess = "soso"
guess_m =""
guess_try = 0
guess_limt = 3
out_limt = False
while guess!=guess_m and not out_limt:
    if guess_try<guess_limt:
        guess_m = input(" ENTER THE GUESS : ")
        guess_try +=1
    else:
        out_limt=True   
if out_limt:
    print('you losee the geuss')        
else:
    print('you win')    