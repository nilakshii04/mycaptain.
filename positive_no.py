n = []
nosElem = int(input("Enter no. of Elements:"))
print("")
for z in range(1,nosElem+1):
  nos = int(input("Enter Number {} : ".format(z)))
  n.append(nos)
print("")
print("Answer ->")
print("")
for i in n:
  if i>0:
    print(i)