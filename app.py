from flask import Flask,  request, render_template,flash, redirect
from flask_mail import Mail, Message
from config import usuario_outlook, activit_outlook, secret_key
import smtplib
#import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)
app.secret_key= secret_key


@app.route("/")
def index():
    return render_template("index.html")


#configurações de email
@app.route("/sendMail", methods=["GET","POST"])
def sendMail():

    host = "smtp.office365.com"
    port = "587"
    login = usuario_outlook
    senha = activit_outlook

    server = smtplib.SMTP(host,port)
    server.ehlo()
    server.starttls()
    server.login(login, senha)

    usuario = request.form.get("nome")
    corpoMsg = request.form.get("mensagem")


    #2-Contruir email tipo mime
    body =f"""{corpoMsg}"""

    email_msg = MIMEMultipart()
    email_msg["From"] = login
    email_msg["to"] = usuario_outlook
    email_msg["Subject"] = f"Olá Fernando, {usuario} enviou uma mensagem para você"
    email_msg.attach(MIMEText(body,"plain"))

    #3-Enviar email tipo mime
    server.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())
    server.quit()

    flash("Seu E-mail foi enviado!")
    return render_template("index.html")    








if __name__ == "__main__":
    app.run()