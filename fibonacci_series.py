n = input("Enter the Limit: ")
n = int(n)
x,y,a,b = 1,1,0,0
print('The required Fibb series is: ')
while(a<=n):
  a = x+y
  print(x)
  b=a
  x=y
  y=b
