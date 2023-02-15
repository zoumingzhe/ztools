# coding=utf-8
# ------------------------------------------------------------------------------
# 类 mail
# ------------------------------------------------------------------------------
# 变更履历：
# 2023-01-30 | Zou Mingzhe   | Ver0.1  | 初始版本
# ------------------------------------------------------------------------------
# MAP：
# 未测试 | attachment(self, ...)        | 添加附件
# 未测试 | send(self, ...)              | 发送邮件
# ------------------------------------------------------------------------------
import os
import socket
import smtplib
import mimetypes
from email.message import EmailMessage
# ------------------------------------------------------------------------------
class mail:
    """
    mail类提供了邮件收发处理。
    """
    def __init__(self, *args, **kwargs):
        user = os.getlogin()
        host = socket.gethostname()
        info = "{}@{}".format(user, host)
        receiver = args
        sender = kwargs['sender'] if 'sender' in kwargs else info
        subject = kwargs['subject'] if 'subject' in kwargs else None
        content = kwargs['content'] if 'content' in kwargs else None
        self.__emsg = EmailMessage()
        self.__emsg['Subject'] = subject
        self.__emsg['From'] = sender
        self.__emsg['To'] = receiver
        self.__emsg.set_content(content if type(content) is str else str(content))
# ------------------------------------------------------------------------------
    def attachment(self, filepath, mimetype = None):
        """
        添加附件：
        输入参数：
        返回参数：None
        说明：调用该方法将在邮件中添加附件。
        """
        if not os.path.isfile(filepath):
            return False

        mimetype, encoding = mimetypes.guess_type(filepath)
        if mimetype is None:
            return False
        maintype, subtype = mimetype.split('/', 1)

        with open(filepath,'rb') as f:
            filedata = f.read()
        filename = os.path.basename(filepath)
        self.__emsg.add_attachment(filedata, filename=filename,
                                   maintype=maintype, subtype=subtype)
        return True
# ------------------------------------------------------------------------------
    def send(self):
        """
        发送邮件：
        输入参数：
        返回参数：bool
        说明：调用该方法将发送邮件，并返回发送成功状态。
        """
        try:
            with smtplib.SMTP('localhost') as smtp:
                smtp.send_message(self.__emsg)
        except smtplib.SMTPException:
            return False
        return True
# ------------------------------------------------------------------------------
