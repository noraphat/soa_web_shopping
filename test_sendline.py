from songline import Sendline
token = 'ACRwZ6dSgOHePJlKl46D9hufiIdcoa9OXaYnxuS5dXS' 
messenger = Sendline(token)
messenger.sendtext('สวัสดีจากพี่ยุ่ง')
messenger.sticker(1,1)
messenger.sendimage('https://img.pngio.com/python-logo-python-logo-png-268_300.png')
#send message messenger.sendtext(‘Hello world’)

#send sticker messenger.sticker(1,1)

#send image messenger.sendimage(’https://img.pngio.com/python-logo-python-logo-png-268_300.png’)