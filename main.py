import smtplib

my_mail = "binarybrains22@gmail.com"#"pythonpractice2430@gmail.com"
password = "@r7unm33n4"#"sairam2430"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)

    connection.sendmail(my_mail, "pythonpractice2412@yahoo.com", msg="Subject:Hello\n\nHI hello")
