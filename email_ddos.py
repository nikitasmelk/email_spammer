import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
#Parse text file for list of emails
#Enter emails on separate lines in the text file
with open("email_list.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

#Ask user for number of emails
num = int(input("Enter the number of emails you want to send to each person -> "))

#Enter your email data
email_user = 'sender_email@whatever.com'
email_password = 'sender_password'

#Subject ... duh
subject = "Title... here"

msg = MIMEMultipart()
msg['From'] = email_user
msg['Subject'] = subject

#Body of your email
body = "Text ... here plz"

msg.attach(MIMEText(body,'plain'))

for i in range(len(content)):
    #print process to console
    print("---------------")
    print(content[i])
     
    to = content[i]

    x = num

    while x > 0:
        x -= 1 #decremeny
        # send server request
        try: 
            text = msg.as_string()
            # this is a gmail port, try other if using other email provider
            server = smtplib.SMTP('smtp.gmail.com',587) 
            print(server)
            server.starttls()
            server.login(email_user,email_password)
            server.sendmail(email_user,content[i],text)
            server.quit()

            print ('Email sent!')
            print(" ")
        except: 
            print ('Something went wrong...')
            print(" ")

    print("DONE!")
