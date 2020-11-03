n=1
suma_p=0
suma_n=0
nr_p=0
nr_n=0
while n<12:
    t=eval(input('introdu temperaturile'))
    if t>=0:
        suma_p+=t
        nr_p+=1
    if t<0:
        suma_n+=t
        nr_n+=1
    n+=1
        
print ('media temperaturilor pozitive este' , (round(suma_p/nr_p , 2)))     
print ('media temperaturilor negative este ', (round(suma_n/nr_n , 2)))   