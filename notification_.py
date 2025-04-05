import pandas
import smtplib

my_email = "your email here"
password = "your password here"

def absent_students():
    data = pandas.read_csv("records.csv")
    all_words = data.to_dict(orient='records')
    email = []
    list_of_absent = []
    for i in all_words:
        if i['present'] != "P":
            rollno = i['rollno']
            name = i['name']
            email.append(i['email'])
            list_of_absent.append(f"{rollno} - {name}")
    for i in range(len(email)):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email[i],
                msg="Subject:ABSENT!\n\nYou didn't attend today's class. Try to be regular"
            )
    return list_of_absent
