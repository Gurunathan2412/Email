import smtplib

my_mail = "Your MailID"
password = "Password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)

    connection.sendmail(my_mail, "Receiver Mail", msg="Subject:Hello\n\nHI hello")
