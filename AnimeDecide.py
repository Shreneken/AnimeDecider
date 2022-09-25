from random import choice
import requests

min_rating = input("What minimum rating do you want?\n")
genre = input("What genre do you feel like watching?\n").lower()

genre_collection = {"action" : 1, "adventure" : 2, "racing" : 3, "comedy" : 4, "avant garde" : 5,
                    "mythology" : 6, "mystery" : 7, "drama" : 8, "ecchi" : 9, "fantasy" : 10 }
                    
score_parameter = {"min_score" : min_rating,
                    "genres" : genre_collection[genre]}
score_response = requests.get("https://api.jikan.moe/v4/anime", params = score_parameter)

#gets random anime according to the input rating and genre
try:
    animeTitle = choice([(d["titles"][0]["title"], d["url"]) for d in score_response.json()["data"]])
    print("The anime chosen for you is:\n" + animeTitle[0] + "\n" + animeTitle[1])
except:
    print("No such anime exists!")

