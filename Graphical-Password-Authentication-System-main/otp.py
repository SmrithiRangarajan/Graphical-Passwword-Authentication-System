import math as m
import random as r

def genOTP() : 
    string1 = '1234'
    string2 = 'ABCD'
    OTP1 = ""
    OTP2 = ""
    l1 = len(string1)
    l2 = len(string2)
    for i in range(1) : 
        OTP1 += string1[m.floor(r.random() * l1)]
        OTP2 += string2[m.floor(r.random() * l2)] 
  
    return (OTP1 + OTP2) 

if __name__ == "__main__" :

    print("Your One Time Password is : ", genOTP());
