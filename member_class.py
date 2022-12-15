import json
from json import JSONEncoder
class discordUser(JSONEncoder):
  
  def __init__(person, name): #intializer
    person.name = name
    person.mentionList = []

  def toJson(person):
    return json.dumps(person, default=lambda o: o.__dict__)