from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error +1
        except:
            error = error +1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay,2)
    speed = round(len(userinput)/time_r)

    return  speed
while True:
    ck = input("ready to test : y/n :: ")
    if ck == "y":
        test = ["Real time speech recognition for regional languages "," microphone or a telephone is converted from acoustic signal to a set of words in speech recognition","which deals with speech recognition has to get adapted to the unpredictable "," At its core, this project is built in the python programming language."]
        test1 = r.choice(test)
        print(test1)
        print()
        time1 = time()
        testinput = input("Enter : ")
        time2 = time()

        print("Speed : ",speed_time(time1,time2,testinput)," w/sec")
        print("Error : ",mistake(test1,testinput))
    elif ck == "n":
        break
    else:
        print("wrong input")
        
