from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib, ssl, email

class EmailBot:
  """Class to email you when something happens.
  """
  email_address = ""
  account_name = ""
  secrets_path = "~/.emailbot"
  def __init__(self, recipient, bot_identifier):
    """Constructor for EmailBot.

    Args:
        recipient (string): address to send emails to
        bot_identifier (string): identifier in secrets field
    """ 
    self.email_address = recipient
    self.bot_identifier = bot_identifier
  

  def email_me(self, subject="Task Complete", message="Task Complete"):
    """Send an email with optional subject and message.

    Args:
        subject (str, optional): subject of email. Defaults to "Task Complete".
        message (str, optional): body of email. Defaults to "Task Complete".
    """
    port = 465

    username, password = self.get_password()
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        msg = MIMEMultipart()
        msg["From"] = username
        msg["To"] = self.email_address
        msg["Subject"] = subject

        body = message
        msg.attach(MIMEText(body, "plain"))
        server.login(username, password)
        server.sendmail(username, self.email_address, msg.as_string())
  

  def set_secrets_path(self, path):
    """Update secrets path to "path".

    Args:
        path (string): path to secrets file. 
    """
    self.secrets_path = path
  
  def get_password(self):
    with open(os.path.expanduser(self.secrets_path)) as f:
      for line in f:
        if self.bot_identifier in line:
          tokens = line.split("\t")
          tokens = [token.rstrip() for token in tokens]
          return tokens[1:]