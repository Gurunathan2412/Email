import smtplib

my_mail = "Your mail here"
password = "Password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)

    connection.sendmail(my_mail, "pythonpractice2412@yahoo.com", msg="Subject:Hello\n\nHI hello")
