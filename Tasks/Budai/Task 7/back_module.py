import json


def add_album(album):
    new_album = {'title': album.get_title(),
                 'artist': album.get_artist(),
                 'year': album.get_year(),
                 'genre': album.get_genre()}
    try:
        with open('albums.json', encoding='utf-8', mode='r') as file:
            data = json.load(file)
        data['albums'].append(new_album)
        with open('albums.json', encoding='utf-8', mode='w') as file1:
            json.dump(data, file1, ensure_ascii=False, indent=2)
    except FileNotFoundError:
        print('File not found')


def get_all_albums():
    try:
        with open('albums.json', encoding='utf-8', mode='r') as file:
            data = json.load(file)
            return data['albums']
    except FileNotFoundError:
        print('File not found')


def search_title(text):
    for album in get_all_albums():
        if text.lower() in album['title'].lower():
            yield album


def search_artist(text):
    for album in get_all_albums():
        if text.lower() in album['artist'].lower():
            yield album


def search_year(year):
    for album in get_all_albums():
        if year == album['year']:
            yield album


def search_genre(text):
    for album in get_all_albums():
        if text.lower() in album['genre'].lower():
            yield album
