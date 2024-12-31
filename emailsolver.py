import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = 'mayanks2831@gmail.com'
sender_password = "xrpl pevi mnho sgpp"
receiver_email = "ee23b045@smail.iitm.ac.in"

message = MIMEMultipart()

message['From']=sender_email

message['To']=receiver_email

message['Subject']="About Me!!"

body = "Hi this is mayank and like solving problems in technological sphere."
body_html = """<html>
  <head>Hello</head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="https://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>"""

part1 = MIMEText(body, 'plain')
part2 = MIMEText(body_html,'html')
message.attach(part1)
message.attach(part2)
smtp_server = "smtp.gmail.com"
port = 587  # TLS port
try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # Encrypt the connection
        server.login(sender_email, sender_password)  # Authenticate
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
