import requests


def intelligence_heroes(heroes_name = [], url=''):
    response = requests.get(url)
    max_int = 0
    for hero in heroes_name:
        for persona in response.json():
            if persona['name'] == hero:
                powerstats = persona['powerstats']['intelligence']
                if max_int < powerstats:
                    max_int = powerstats
                    name_heroes = hero
    return max_int, name_heroes


print(intelligence_heroes(['Hulk','Thanos','Captain America'], 'https://akabab.github.io/superhero-api/api/all.json'))
