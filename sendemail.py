import smtplib as s

ob = s.SMTP('smtp.gmail.com',587) #make server first

ob.ehlo()
ob.starttls()
ob.login('boroleujval4@gmail.com','ujval@123')

subject = "test python "
body = "python "
massage = "subject: {}\n\n{}".format(subject,body)
listadd=['ujvalmborole@gmail.com']
ob.sendmail('boroleujval4@gmail.com',listadd,massage)
print("mail Send successfully")
ob.qute() #use to close the server


