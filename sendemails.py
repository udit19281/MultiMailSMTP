import smtplib
from time import sleep
import os
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
print("This Script only works using gmail account make sure you have allowed less secure apps from your gmail account settings. ")
username = input("Sender email :")
password = input("Sender password :")
print("[+] server stated [+]")
try:
    s.login(username, password)
except Exception as e:
    print(e)
    os._exit(0)
print("logged in successfully")
msg = """Subject:{subject}
To: {rec}
From :{sender}
{msge}
"""
usercount = int(input("Enter number of receiver:"))
userlist = []
for i in range(usercount):
    user = input("Enter receiver {h} email address:".format(h=i+1))
    userlist.append(user)

print("\nSelect a mode to use \n1)Send an email to all receivers ")
print("2)Send multiple emails to each receiver \n")

option = int(input())
if(option == 1):
    subject = input("Enter subject:")
    message = input("Enter your message:")
    for i in range(usercount):
        email = userlist[i]
        s.sendmail(username, email, msg.format(subject=subject,
                                               rec=email, sender=username, msge=message))
        sleep(3)
        print("Email sent to {m}".format(m=email))
    s.quit()
    os._exit(0)

elif option == 2:
    emcount = int(input("Enter number of emails to be sent to each receiver : "))
    sublist = []
    messages = []
    for i in range(emcount):
        gg = input("Enter Subject {i} :".format(i=i+1))
        mm = input("Enter Message {i} :".format(i=i+1))
        messages.append(mm)
        sublist.append(gg)
    i = 0
    sub = 0
    while (i) < emcount:
        subject = sublist[i]
        message = messages[i]
        for j in range(usercount):
            email = userlist[j]
            s.sendmail(username, email, msg.format(subject=subject,rec=email, sender=username, msge=message))
            sleep(2)
            print("Email sent to {m} with subject {s}".format(m=email, s=subject))
        i += 1
    s.quit()
    os._exit(0)
