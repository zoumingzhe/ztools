import sys
sys.path.append(r'../../ztools')
from utils.zemail import mail




mail("zoumingzhe@qq.com", subject = "test", content="This is test mail").send()
input("按回车（Enter）继续")

mail("zoumingzhe@qq.com", "mingzhe.zou@easystack.cn", content="test").send()
input("按回车（Enter）继续")

e = mail("zoumingzhe@qq.com", "mingzhe.zou@easystack.cn", subject = "test attachment")
e.attachment('/tmp/test_email.txt')
e.send()
input("按回车（Enter）继续")
