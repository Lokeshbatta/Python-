str1=input("enter the number:")
alphabets=0
digit=0
space=0
special=0
a=[]
spl=[]
d=[]
for i in range(len(str1)):
    if(str1[i].isalpha()):
        alphabets=alphabets+1
        a.append(str1[i])
    elif(str1[i].isdigit()):
          digit=digit+1
          d.append(str1[i])
    elif(str1[i].isspace()):
          space=space+1
    else:
        special=special+1
        spl.append(str1[i])
print("alphabets:",alphabets)         
print("space:",space)
print("digit:",digit)
