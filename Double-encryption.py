import numpy

def seperate(a):
    b=[]
    for i in range(0,len(a)):
        b.append(a[i])

    return b

a1,a2,a3,a4=[],[],[],[]

def randu():

    joke=numpy.random.choice(range(0,255), 255, replace=False)
    cod=[]
    for i in range(0,len(joke)):
        cod.append(chr(joke[i]))

    return cod

numpy.random.seed(10)
a1=randu()
print(a1)
numpy.random.seed(20)
a2=randu()
numpy.random.seed(30)
a3=randu()
numpy.random.seed(40)
a4=randu()

print(a1)
print(a2)
print(a3)
print(a4)
def search_index(a,b):
    #b is an array
    #a is a character
    #i need to return the index value of a in b
    #this can be achieved by a simple for loop
    m=0
    for i in range(0,len(b)):
        if a==b[i]:
            m=i
    return m

def search_char(a,b):
    #a is an index
    #b is an array
    #i want to return the character at the index a in the array b
    return b[a]
con=True
while(con):
    a=int(input("Enter 1 for encyption and 2 for decryption: "))

    if (a==1):
        x=input("Enter the message to be encrypted: ")
        h=seperate(x)
        print("The seperated lettrs are: ")
        print(h)

        s=[]
        print(a1)
        for i in range(0,len(h)):
            s.append(search_index(h[i],a1)) #number array
            #search a1 and map each character to the index value on a1
        print("The Index values in a1 are: ")
        print (s)
        l=[]
        for i in range(0, len(s)):
            #now make a string from the index values of a1 onto the index values of a2
            l.append(search_char(s[i],a2)) #character array
        print("The characters in a2 are: ")
        print(l)
        j=[]
        #map the character from a2 onto index values in a3
        for i in range(0,len(l)):
            j.append(search_index(l[i],a3)) #number array
        print("The index values in a3 are: ")
        print(j)

        str=""
        for i in range (0,len(j)):
        #finally, map the index values of a3 into a
        #final array of characters of the corresponding indices in a4
            str=str+search_char(j[i],a4)# final string yayy

        #the string obtained after the a4 step is the encrypted string
        print ("The encypted string is: ")
        print(str)
        don=input("Do you want to do it again? Press Y for yes and anything else for no: ")
        if (don=="Y"):
            con=True
        else:
            con=False


    elif(a==2):
        x=input("Enter the message to be decrypted: ")
        h=seperate(x)
        print("Seperated letters are:")
        print(h)
        num=[]

        for i in range (0,len(h)):
        #finally, map the index values of a3 into a
        #final array of characters of the corresponding indices in a4
            num.append(search_index(h[i],a4))#number array
        print("Index values in a4 are: ")
        print(num)
        j=[]
        for i in range(0,len(num)):
            j.append(search_char(num[i],a3)) #character array
        print("Characters in a3 are: ")
        print(j)

        l=[]
        for i in range(0, len(j)):
            #now make a string from the index values of a1 onto the index values of a2
            l.append(search_index(j[i],a2)) #number array
        print("Index values in a2 are: ")
        print(l)

        s=""
        for i in range(0,len(l)):
            s+=(search_char(l[i],a1)) #character array
            #search a1 and map each character to the index value on a1
        print("The decrypted message is: ")
        print (s)
        don=input("Do you want to do it again? Press Y for yes and anything else for no: ")
        if (don=="Y"):
            con=True
        else:
            con=False


    else:
        print("Dont be silly. Try again and choose any of the given choices. Press ctrl+C to break out.")
        con=True
