def rec(n):
 if n<=1:
     return n
 else:
     return(rec(n-1)+rec(n-2))
n_terms=10
if n_terms<=0:
    print("invalid input Please input a +ve value")
else:
    print("Febnocci series")
for i in range(n_terms):
    print(rec(i))
    
print("____________")

def pwr(num,y):
 if y==0:
   return 1
 else:
   return num*pwr(num,y-1)

print(pwr(2,6))
print("__________")   


