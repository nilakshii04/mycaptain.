myDict={"py":"PYTHON","c":"C program","html":"HTML","jsp":"JAVA","docs":"word document" }
#print(myDict)
file=input("enter a filename:")
file=file.split(".")
#print(file[-1])
f=myDict.get(file[-1])
print("The extension of the given filename is "+f)