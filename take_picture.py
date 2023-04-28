# THis script will take the picture with the pic and send it or store. 
import smtplib,ssl
import time
from picamera import PiCamera
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
timestr = time.strftime(“%m, %d,%Y – %H:%M:%S”)
print timestr
#data_folder = Path(“/home/pi/photos/”)
camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture(‘%s.jpg’ % timestr)  # image path set
sleep(5)
camera.stop_preview()
def send_an_email():
    toaddr = ‘me+gitallotment@mattnics.com‘      # To id
    me = ‘me+gitallotment@mattnics.com‘          # your id
    subject = “Photo of the Day”   # Subject

    msg = MIMEMultipart()
    msg[‘Subject’] = subject
    msg[‘From’] = me
    msg[‘To’] = toaddr
    msg.preamble = “test “
    #msg.attach(MIMEText(text))

    part = MIMEBase(‘application’, “octet-stream”)
    part.set_payload(open(“%s.jpg” % timestr, “rb”).read())
    encoders.encode_base64(part)
    part.add_header(‘Content-Disposition’, ‘attachment; filename= “%s.jpg”‘ % timestr)   # File name and format name
    msg.attach(part)
    try:
      s = smtplib.SMTP(‘smtp.gmail.com’, 587)  # Protocol
      s.ehlo()
      s.starttls()
      s.ehlo()
      s.login(user = ‘xxxx@gmail.com‘, password = ‘your_email_pass‘)  # User id & password
      #s.send_message(msg)
      s.sendmail(me, toaddr, msg.as_string())
      s.quit()
    #except:
    #   print (“Error: unable to send email”)
    except SMTPException as error:
          print (“Error”)                # Exception

send_an_email()
