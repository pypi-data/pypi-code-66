import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ntpath


class FMailError(Exception):
    pass


class FMailConfig:

    """
    Utility class to store mail server configuration
    """

    username = ""
    password = ""
    host = ""
    port = None

    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password


class FAttachment:

    """
    Utility class to store and pass files to mail
    """

    fname = ""
    path = ""
    ftype = ""
    fsize = ""
    fdata = ""

    def __init__(self, path: str):

        if not isinstance(path, str):
            raise FMailError("Path must be a string!")

        if not path:
            raise FMailError("Path cannot be empty!")

        self.fname = ntpath.basename(path)
        self.path = path

        try:
            with open(self.path, mode='rb') as file:
                self.fdata = file.read()
        except Exception as exception:
            raise FMailError(str(exception)) from exception


class FMessage:

    """
    Mail message class used to store whole mail data
    """

    subject = None
    body_plain = None
    body_html = None
    msg_type = None
    message = None
    from_addr = None
    to_addrs = []
    cc_addrs = []
    bcc_addrs = []
    attachments = []

    def __init__(
            self, subject: str, body_plain: str, body_html: str,
            from_addr: str, to_addrs: list = None, cc_addrs: list = None,
            bcc_addrs: list = None, attachments: list = None):

        self.subject = subject if subject else ""
        self.body_plain = body_plain if body_plain else ""
        self.body_html = body_html if body_html else ""
        self.from_addr = from_addr if from_addr else ""
        self.to_addrs = to_addrs if to_addrs else []
        self.cc_addrs = cc_addrs if cc_addrs else []
        self.bcc_addrs = bcc_addrs if bcc_addrs else []
        self.attachments = attachments if attachments else []

    def __validate_message(self):

        if not isinstance(self.subject, str):
            raise FMailError('Subject must be a string!')

        if not isinstance(self.body_plain, str):
            raise FMailError('Body PLAIN must be a string!')

        if not isinstance(self.body_html, str):
            raise FMailError('Body HTML must be a string!')

        if not isinstance(self.from_addr, str):
            raise FMailError('From address must be a string!')

        if not isinstance(self.to_addrs, list):
            raise FMailError('To field must be a list!')

        if not self.subject:
            raise FMailError('Subject cannot be empty!')

        if not self.from_addr:
            raise FMailError('From address cannot be empty!')

        if not self.to_addrs:
            raise FMailError('To field cannot be empty!')

    def __create_message(self):
        """
        Create complete multipart mail
        """

        self.__validate_message()

        message = MIMEMultipart('alternative')
        message['From'] = self.from_addr
        message['To'] = ','.join(self.to_addrs)
        message['Subject'] = self.subject
        message['Bcc'] = ','.join(self.bcc_addrs)
        message['Cc'] = ','.join(self.cc_addrs)
        message.attach(MIMEText(self.body_plain, 'plain'))

        if self.body_html:
            message.attach(MIMEText(self.body_html, 'html'))

        for file in self.attachments:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(file.fdata)
            encoders.encode_base64(attachment)
            attachment.add_header(
                'Content-Disposition',
                f'attachment; filename= {file.fname}'
            )
            message.attach(attachment)
        self.message = message

    def build(self):
        """
        Build multipart message
        """
        self.__create_message()

    def get_message(self):
        """
        Return payload for sendmail
        """
        self.__create_message()
        to_addrs = self.to_addrs + self.cc_addrs + self.bcc_addrs
        return [self.from_addr, to_addrs, self.message.as_string()]


class FMail:

    """
    Main class used to send emails with specified config
    """

    config = None
    app = None

    def __init__(self, config=None, app=None):

        self.config = config
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Not tested
        Flask integration
        Load mail server configuration from Flask config
        """

        host = app.config.get('FMAIL_HOST')

        if not host:
            raise FMailError("Mail server host not provided!")

        port = app.config.get("FMAIL_PORT")

        if not port:
            port = 25
            app.config.setdefault('FMAIL_PORT', 25)

        username = app.config.get('FMAIL_USERNAME')
        password = app.config.get('FMAIL_PASSWORD')

        self.config = FMailConfig(**{
            'host': host,
            'port': port,
            'username': username,
            'password': password
        })

    def set_config(self,config):

        self.config = config

    def send(self, obj, config=None):
        """
        Send mail or list of mails
        :type obj: FMessage | list[FMessage]
        :type config: FMailConfig

        Pass optional custom config to send messages
        """

        if not config:
            config = self.config

        if isinstance(obj, FMessage):
            self.__send([obj], config)
        elif isinstance(obj, list):
            self.__send(obj, config)
        else:
            raise FMailError("Invalid object passed to send method!")

    def __send(self, fmessages, config):
        """
        Send mails with smtplib
        """

        if not isinstance(config, FMailConfig):
            raise FMailError("Invalid config object!")

        if config.port == 25:
            with smtplib.SMTP(config.host, config.port) as server:

                for fmessage in fmessages:
                    server.sendmail(*fmessage.get_message())
        else:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(
                    config.host, config.port,
                    context=context) as server:

                server.login(config.username, config.password)

                for fmessage in fmessages:
                    server.sendmail(*fmessage.get_message())

    def dispatch(self):
        """
        Not implemented
        Dispatch messages to celery queue
        """

    def retry(self):
        """
        Not implemented
        Retry messages from failed celery queue
        """
