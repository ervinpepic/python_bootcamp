import smtplib

my_email = "myemail@email"
my_password = "mypass"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
            from_addr=my_email, 
            to_addrs="myemail@email", 
            msg="Subject:Testni email\n\nTest from VSCode"
    )