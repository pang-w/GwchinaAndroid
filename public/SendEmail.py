import os,time,smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders
from email.mime.base import MIMEBase

from public import Log

log = Log.Logger(logger='SendEmail').getLog()

# 3.定义：发送邮件，发送最新测试报告html
def SendEmail(html_path,log_path):
    try:
        # 打开文件
        f = open(html_path, 'rb')
        # 读取文件内容
        mail_body = f.read()
        # 关闭文件
        f.close()

        # 发送邮箱服务器
        smtpserver = 'smtp.exmail.qq.com'
        # 发送邮箱用户名/密码
        user = 'zhangjg@txtws.com'
        password = 'Lwtx0720'
        # 发送邮箱
        sender = 'zhangjg@txtws.com'
        # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@163.com'
        receiver = ['719910919@qq.com','zhangjg@txtws.com']
        # 发送邮件主题以及Html附件
        subject = '自动化测试报告'

        msg = MIMEMultipart('mixed')

        msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
        msg.attach(msg_html1)

        msg_html = MIMEText(mail_body, 'html', 'utf-8')
        # day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # html_path = os.path.dirname(os.path.abspath('.')) + '\\report\\' + day
        FileName = html_path[-31:]
        # msg_html["Content-Disposition"] = 'attachment; filename="InterFaceTestResult.html"'
        msg_html["Content-Disposition"] = 'attachment; filename= %s ' % FileName
        msg.attach(msg_html)

        # 附件-log
        c_type = 'application/octet-stream'
        maintype, subtype = c_type.split('/', 1)
        LogFile = MIMEBase(maintype, subtype)
        LogFile.set_payload(open(log_path, 'rb').read())
        LogFileName = log_path[-20:]
        LogFile.add_header('Content-Disposition', 'attachment', filename=LogFileName)
        encoders.encode_base64(LogFile)
        msg.attach(LogFile)

        # 要加上msg['From']这句话，否则会报554的错误。
        # 要在163设置授权码（即客户端的密码），否则会报535
        msg['From'] = 'zhangjg@txtws.com'
        #    msg['To'] = 'XXX@doov.com.cn'
        # 多个收件人
        msg['To'] = ";".join(receiver)
        msg['Subject'] = Header(subject, 'utf-8')

        # 连接发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, 25)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print('邮件发送成功')
    except Exception as e:
        log.critical('邮件发送失败：%s ' % e)
        print('邮件发送失败：%s ' % e)

# ======查找测试目录，找到最新生成的测试报告文件======
def FindNewHtml(HtmlPath):
    lists = os.listdir(HtmlPath)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(HtmlPath + "\\" + fn))  # 按时间排序
    file_new = os.path.join(HtmlPath, lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)
    return file_new

def FindNewLog(LogPath):
    lists = os.listdir(LogPath)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(LogPath + "\\" + fn))  # 按时间排序
    file_new = os.path.join(LogPath, lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)
    return file_new

if __name__ == '__main__':
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    html_path = os.path.dirname(os.path.abspath('.')) + '\\report\\' + day
    log_path = os.path.dirname(os.path.abspath('.')) + '\\log\\' + day

    HtmlPath = FindNewHtml(html_path)
    LogPath = FindNewLog(log_path)
    SendEmail(HtmlPath,LogPath)