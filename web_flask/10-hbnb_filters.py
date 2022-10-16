#!/usr/bin/python3
'''Displays the following routes:
/hbnb_filters
'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    '''returns single state'''
    states = list(storage.all('State').values())
    amenities = list(storage.all('Amenity').values())
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    '''delete sqlalchemy session after each request'''
    storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
