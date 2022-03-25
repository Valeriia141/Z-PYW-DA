if __name__ == '__main__':
    import requests

    response = requests.get("http://hp-api.herokuapp.com/api/characters")
    list_of_characters = response.json()
    num = 1
    for actor in list_of_characters:
        if actor.get('actor'):
            print(num, actor.get('actor'))
        num = num + 1

    actor = input("enter the actor's name : ")
    characters = { 1 : 'alive',
                   2 : 'alternate_actores',
                   3 : 'alternate_names',
                   4 : 'ancestry',
                   5 : 'dateOfBirth',
                   6 : 'eyeColour',
                   7 : 'gender',
                   8 : 'hairColour',
                   9 : 'hogwartsStaff',
                   10 : 'hogwartsStudent',
                   11 : 'house',
                   12 : 'image',
                   13 : 'name',
                   14 : 'patronus',
                   15 : 'species',
                   16 : 'wand',
                   17 : 'wizard',
                   18 : 'yearOfBirth'}
    for key, value in characters.items():
        print(key, value)
    character = int(input("what do you want to know? : "))

    for actors in list_of_characters:
        if actors.get('actor') == actor:
            value = actors.get(characters[character])
            if value == '':
                print("I do not know(")
            else:
                print(value)

    input('Press ENTER to exit')