f=open("4.txt","w")
f.write("Jith Jolly")
f.close()
f=open("abc.txt",'r')
str=f.read()
print("Read Strings:",str)
print("File",f.name,"Closed")
