import imaplib
import smtplib
import email
print "Welcome to your gmail bot","\n","Please enter ur email id"
email_id=raw_input()
print "Please enter ur password"
password=raw_input()
box=imaplib.IMAP4_SSL("imap.gmail.com")
box.login(str(email_id),str(password))
def sending_message():
    print "enter email id of receiver"
    rec_id=raw_input()
    box_s=smtplib.SMTP("smtp.gmail.com",587)
    box_s.starttls()
    box_s.login(str(email_id),str(password))
    mail=email.MIMEMultipart.MIMEMultipart()
    #print mail,1
    mail['From']=email_id
    mail['TO']=rec_id
    print "enter subject"
    mail['Subject']=raw_input()
    print "enter msg"
    main_body=raw_input()
    mail.attach(email.MIMEText.MIMEText(main_body,'plain'))
    final_mail=mail.as_string()
    box_s.sendmail(email_id,rec_id,final_mail)
    print "SUCCESSFULLy SENT MESSAGE"
    box_s.quit()
#sending_message()


def selection(k):
    if k==0:
        dic1={1:'all_',2:'viewing_unread',3:'viewing_before_and_after',4:'From_'}
    else:
         dic1={1:'all_',2:'deleting_read',3:'deleting_before_and_after',4:'From_'}
    for var1 in range(1,5):
        print var1 ," : ", dic1[var1]
    print "Please Select one of the above"
    var2=input()
    if var2!=2:
        dic2={1:"INBOX",2:"SENT "}
        for var3 in range(1,3):
            print var3," : ",dic2[var3]
        print "Please select one of the above"
        var4=input()
        if var4==1:
            box.select('inbox')
        else:
            box.select('[Gmail]/Sent Mail')
    if var2==2:
        box.select('inbox')
        validation,length= box.search(None,"(UNSEEN)")
    if var2==1:
        validation,length=box.search(None,'(ALL)')
    if var2==3 :
        for k in range(2):
            if k==0:
                print "SINCE"
            else:
                print "BEFORE"
            print "please enter date in the format 'dd'"
            date=input()
            dic3={1:"Jan",2: "Feb", 3: "Mar",4: "Apr",5: "May",6: "Jun",7:
                "Jul",8: "Aug" ,9: "Sep",10:"Oct",11: "Nov",12: "Dec"}
            for i in range (1,13):
                print i , dic3[i]
            print "select monthnumber"
            month=input()
            month=dic3[month]
            print "enter year yyyy"
            year=input()
            if k==0:
                since=[date,month,year]
            else :
                before=[date,month,year]
         
        validation,length=box.search(None,'(SINCE str(since[0])+"-"+str(since[1])+"-"+str(since[2]) BEFORE str(before[0])+str(before[1])+str(before[2]))')
    if var2==4:
        print "Enter the id of person"
        x=raw_input()
        validation,length=box.search(None,'(From str(x))')
    if k==0:
        jing=length[0].split()
        for  king in range(int(jing[-1]),int(jing[0])-1,-1):
            var,data=box.fetch(king,'(RFC822)')
            for subparts in data :
                if isinstance(subparts,tuple):
                    msg=email.message_from_string(subparts[1])
                    if  var2!=2 and var4==2:
                        print "Message sent to : ",msg['to']
                    else :
                        print "Message from : ",msg['from']
                    print
                    print "Subject : ",msg['subject']
                    print
                    for part in msg.walk():
                        if part.get_content_type()=='text/plain':
                         print part.get_payload()
            print

    else:
        jing=length[0].split()
        for  king in range(jing[-1],jing[0]-1,-1):
            box.store(king,'+FLAGS',r'(\Deleted)')
            box.explunge()
            box.close()
            box.logout()

def main():
    dic00={1:"send_email",2:"read_email",3:"delete_email"}
    for kk in range(1,4):
        print str(kk) +" : "+dic00[kk]
    print "Select the number"
    choice=input()
    if choice==1:
        sending_message()
    if choice==2:
        selection(0)
    if choice ==3:
        selection(1)
main()
