#!/usr/bin/python3
'''Displays the following routes:
/hbnb
'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb():
    '''returns single state'''
    states = list(storage.all('State').values())
    amenities = list(storage.all('Amenity').values())
    places = list(storage.all("Place").values())
    users = list(storage.all("User").values())
    place_owner_objs = []
    for place in places:
        for user in users:
            if place.user_id == user.id:
                place_owner_objs.append(["{} {}".format(
                    user.first_name, user.last_name), place])
    place_owner_objs.sort(key=lambda p: p[1].name)
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           place_owner_objs=place_owner_objs)

@app.teardown_appcontext
def teardown(self):
    '''delete sqlalchemy session after each request'''
    storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
