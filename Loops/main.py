## For loop
n = 5

for i in range(0,n):
    for k in range(n - i):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()

print()
'''
output :
        * 
      * * * 
    * * * * * 
  * * * * * * * 
'''

for i in range(n,0,-1):
    for k in range(n - i):
        print(" ",end=" ")
    for j in range(2*i -1):
        print("*",end=" ")
    print()

'''
output : 
* * * * * * * * * 
  * * * * * * * 
    * * * * *
      * * *
        *
'''