import math as m
import random as r

def genOTP() :     
    string = '1234'
    OTP = ""
    l = len(string)
    for i in range(4) :
        OTP += string[m.floor(r.random() * l)] 
  
    return (OTP) 

if __name__ == "__main__" :

    print("Your One Time Password is : ", genOTP());
