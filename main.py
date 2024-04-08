#preprosti geogrfski kviz

import random #zbirali bomo naključno zato importamo random

countries_cities = {"Austria": "Vienna",
                "Belgium": "Brussels",
                "Bulgaria": "Sofia",
                "Croatia": "Zagreb",
                "Cyprus": "Nicosia",
                "Czech Republic": "Prague",
                "Denmark": "Copenhagen",
                "Estonia": "Tallinn",
                "Finland": "Helsinki",
                "France": "Paris",
                "Germany": "Berlin",
                "Greece": "Athens",
                "Hungary": "Budapest",
                "Ireland": "Dublin",
                "Italy": "Rome",
                "Latvia": "Riga",
                "Lithuania": "Vilnius",
                "Luxembourg": "Luxembourg",
                "Malta": "Valletta",
                "Netherlands": "Amsterdam",
                "Poland": "Warsaw",
                "Portugal": "Lisbon",
                "Romania": "Bucharest",
                "Slovakia": "Bratislava",
                "Slovenia": "Ljubljana",
                "Spain": "Madrid",
                "Sweden": "Stockholm"}


#glavna funkcija kjer bo igra potekala. 

def geo_quiz(): 
    country = random.choice(list(countries_cities.keys())) #navedes med cem lahko izbira, funkcija random.choice je ze vstavljena funkcija
    capital = countries_cities[country]

    print(f"What is the capital city of: {country}?")
    answer = input("Answer: ")

#zavarujemo se, da damo vse crke v male črke z lower
    if answer.lower() == capital.lower():
        print("Congrats!!!")
    else:
        print(f"Ooops! The capital city of {country} is {capital}!")

    user_input = input("Do you want to guess again? (Y/N)")
    if user_input.lower == "Y":
        geo_quiz() #samo pokličemo funkcijo
    else:
        print("Thanks for playing!")

#call, da se bo igra zagnala
geo_quiz()
                    
