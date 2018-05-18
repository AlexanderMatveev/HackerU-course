from ftplib import FTP

ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect('127.0.0.1', 21)
try:
    ftp.login("user", "123456")
except Exception:
    print(e)
ftp.retrlines('LIST')
