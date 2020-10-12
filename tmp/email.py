#This is just a copy of an email script

# KML attachment
filename='20140210204804.kml'
fp = open(filename, "rb")
att = email.mime.application.MIMEApplication(fp.read(),_subtype="kml")
fp.close()
att.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(att)