import requests


list_of_pers = ['Hulk', 'Captain America', 'Thanos']


def get_intellect():
    intelligence_dict = {}
    for pers in list_of_pers:
        response = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{pers}")
        characteristic_list = response.json()['results']
        for items in characteristic_list:
            if items['name'] in list_of_pers:
                intelligence_dict[items['name']] = int(items['powerstats']['intelligence'])

    return intelligence_dict


def most_int_intelligence():
    print(f'Самый высокий показатель интеллекта у: {max(get_intellect(), key=get_intellect().get)}')


most_int_intelligence()
