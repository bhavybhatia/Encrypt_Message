s=input("Enter Your message : \t")
k=int(input("Set a key : ")) # This will be used for decrypt your message...
inc=50
cni=50
c=''
cr = ''
for i in s :
    c+=chr(ord(i)+inc)
    inc+=1
print(c)

key=int(input("Enter Key to view to message : "))
while(key!=k):
    key=int(input("Incorrect key...\nRe-Enter your key : "))
    if key == k :
        for i in c :
            cr+=chr(ord(i)-cni)
            cni+=1
        print("The message was : ",cr)

if key==k:
    for i in c:
        cr+=chr(ord(i)-cni)
        cni+=1
    print("The message was : ",cr)
