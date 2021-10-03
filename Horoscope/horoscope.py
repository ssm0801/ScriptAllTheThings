"""
Horoscope
- Check your daily horoscope based on your zodiac sign . Who knows today's your lucky day .
Author : Ashish Patwal
Date : 01/10/21
"""

"""
Inquirer module is a clone of the famous Inquirer.js package and it shares part of the goals and philosophy.
Inquirer ease the process of asking end user questions, parsing, validating answers, managing hierarchical prompts and providing error feedback.
"""


import requests
import inquirer
from bs4 import BeautifulSoup

zodiacSign = {
    "Aquarius": 1,
    "Aries": 2,
    "Cancer": 3,
    "Capricorn": 4,
    "Gemini": 5,
    "Leo": 6,
    "Libra": 7,
    "Pisces": 8,
    "Sagittarius": 9,
    "Scorpio": 10,
    "Taurus": 11,
    "Virgo": 12,
}


def horoscope(zodiac_sign: int, day: str) -> str:
    """returns the horoscope"""
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find("div", class_="main-horoscope").p.text


if __name__ == "__main__":
    questions = [
        inquirer.List(
            "sign",
            message="Choose your Zodiac ",
            choices=zodiacSign.keys(),
        ),
        inquirer.List(
            "day", message="Choose a day ", choices=["Yesterday", "Today", "Tomorrow"]
        ),
    ]
    answers = inquirer.prompt(questions)
    horoscope_text = horoscope(zodiacSign[answers["sign"]], answers["day"])
    print(horoscope_text)
