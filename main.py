import pandas
import datetime as dt
import random
import smtplib

PLACEHOLDER = "[NAME]"
MY_EMAIL = ""
PASSWORD = ""

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

now = dt.datetime.now()
today = (now.month, now.day)

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path, "r") as letter:
        letter_content = letter.read()
        letter_content = letter_content.replace(PLACEHOLDER, birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_dict[today]["email"],
            msg=f"Subject:Happy Birthday!\n\n{letter_content}"
        )




