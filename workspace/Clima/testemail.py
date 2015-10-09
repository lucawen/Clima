import smtplib

fromaddr = 'wilson@solvecorp.com.br'
toaddrs  = 'wbeirigo@terravisiongeo.com.br'
msg = 'There was a terrible error that occured and I wanted you to know!'


# Credentials (if needed)
username = 'wilson@solvecorp.com.br'
password = 'wilci5w7'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
