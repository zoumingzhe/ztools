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
from email.message import EmailMessage
# ------------------------------------------------------------------------------
class mimetype():
    """
    """
    txt             = "text/plain"
# ------------------------------------------------------------------------------
class mail:
    """
    mail类提供了邮件收发处理。
    """
    def __init__(self, receivers, sender=None, subject=None, content=None):
        user = os.getlogin()
        host = socket.gethostname()
        info = "{}@{}".format(user, host)
        self.__emsg = EmailMessage()
        self.__emsg['Subject'] = subject
        self.__emsg['From']  = info if sender is None else sender
        self.__emsg['To'] = receivers
        self.__emsg.set_content(content if type(content) is str else str(content))
# ------------------------------------------------------------------------------
    def attachment(self, filepath, mimetype):
        """
        添加附件：
        输入参数：
        返回参数：None
        说明：调用该方法将在邮件中添加附件。
        """
        maintype, subtype = mimetype.split('/', 1)
        filename = os.path.basename(filepath)
        if not os.path.isfile(filepath):
            return False
        with open(filepath,'rb') as f:
            filedata = f.read()
        self.__emsg.add_attachment(filedata, filename=filename,\
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
