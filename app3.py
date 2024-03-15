import yagmail

# Set up your Gmail account
yag = yagmail.SMTP('yadav.aishwar253@gmail.com', '86918054922$')

# Compose and send the email
subject = 'Hello from Yagmail!'
body = 'This is a Yagmail test email.'
yag.send('aishwar253@outlook.com', subject, body)

# Close the connection
yag.close()