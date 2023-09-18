username = str(input("enter username : "))
email = str(input("enter email : "))

filepath1 = "creds.txt"
filepath2 = "creds_email.txt"
f1 = open(filepath1 , "r")
f2 = open(filepath2 , "r")
# file reading to get original credentials
lines1 = f1.readlines()
lines2 = f2.readlines()
#print(lines1)
#spl = lines1.split("\n")
#print(spl)
#print(len(lines))#no of lines
for i in range (len(lines1)):
    spl = lines1[i].split(" ")
    spl1 = lines2[i].split(" ")
    if spl[i] == username:
        if spl1[i] == email:
            print("details authenticated")
            break
        else:
            print("invalid email")
            break
    else:
        print("invalid username")
        break
