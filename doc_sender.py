import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from dotenv import load_dotenv
import os
load_dotenv()

def send_docs(student_name, student_email , file_path , content , subject):
    # Your Gmail credentials
    sender_email = os.getenv('EMAIL')
    sender_password = os.getenv('PASSWORD')
    sender_name = 'Siddharth Singh'

    # Email content
    subjective = subject
    # body = f"Dear {student_name},\n\nCongratulations on completing the course! Attached is your certificate.\n\nBest regards,\n{sender_name} \nUpflairs Pvt. Ltd. Jaipur Rajsthan"


    body = f"Dear {student_name},\n\n {content}.\n\nBest Regards Team Upflairs,\n{sender_name} \nUpflairs Pvt. Ltd. Jaipur Rajsthan"

    # Creating the email message
    message = MIMEMultipart()
    message['From'] = f'{sender_name} <{sender_email}>'
    message['To'] = student_email
    message['Subject'] = subjective

    # Attach the certificate file (replace 'certificate.pdf' with your actual file)
    with open(file_path, 'rb') as attachment:
        part = MIMEText(body)
        message.attach(part)

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="certificate.png"')
        message.attach(part)

    # Connect to Gmail's SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, student_email, message.as_string())







