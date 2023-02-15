import sys
sys.path.append(r'../../ztools')
from utils.zemail import mail



mail("mingzhe.zou@easystack.cn", content="test").send()
input("按回车（Enter）继续")

e = mail("zoumingzhe@qq.com", "mingzhe.zou@easystack.cn")
e.attachment('/tmp/test_email.txt')
e.send()
input("按回车（Enter）继续")
