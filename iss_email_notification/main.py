import requests
import json
import datetime as dt
import smtplib
import time

MY_LAT = 42.217529
MY_LNG = -70.936897
MY_EMAIL = "domgarseeyah@gmail.com"
MY_PASS = "cnlgawlvvxcarddw"

def is_iss_overhead():
    req = requests.get(url="http://api.open-notify.org/iss-now.json")
    #req = requests.get(url="https://api.nasa.gov/planetary/apod?api_key=a8JmmvRdhpmezLqGXdkFjXhLM5UUaQeXtEO11AI0")
    req.raise_for_status()
    print(req)
    response = req.json()
    iss_lat = float(response['iss_position']['latitude'])
    iss_lng = float(response['iss_position']['longitude'])
    print(iss_lat, iss_lng)

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LNG-5 <= iss_lng <= MY_LNG:
        return True

def is_nighty():
    params = {
        "lat": MY_LAT,
        "lng":  MY_LNG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()

    # #or fstring the url to get the same results
    # url_totes = f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}&formatted=0"
    # response = requests.get(url=url_totes)
    # data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour
    print(time_now)
    if time_now >= sunset or time_now <= sunrise:
    return True

while True:
    time.sleep(600)
    #Run iss notification email
    if is_iss_overhead() and is_nighty():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="dom_garcia@myyahoo.com",
                                msg=f"Subject:ISS Overhead Notification\n\nThe International Space Station is Currently flying overhead near your set coordinates({MY_LAT}, {MY_LNG}).")


