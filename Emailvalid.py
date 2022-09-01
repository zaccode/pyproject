#Email Validation using Regex
#a-z
#0-9
#. _    time 1
# @ time 1
# . 2,3

import re 

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user = input("Enter the email : ")

if (re.search(email_condition,user)):
    print("Right Email")

else:
    print("Wrong Email")

