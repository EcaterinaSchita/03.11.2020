n=eval(input('introdu numerele'))
x+1
suma=0
produsul=1
while x<n:
    produsul*=x
    suma+=x
    x+=1

print('suma numerelor este' , suma)  
print('produsul numerelor este', produsul)  
print('media aritmetica este' suma/n)