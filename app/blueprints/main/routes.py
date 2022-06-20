from flask import render_template, request, flash, redirect, url_for
import requests
from .import bp as main
from flask_login import login_required
from ..auth.forms import BiteForm
from app.models import Bite, User
import random

@main.route('/', methods = ['GET'])
@login_required
def index():
    return render_template('index.html.j2')

@main.route('/my_bites', methods=[])
@login_required
def my_bites():
    return render_template('my_bites.html.j2')

@main.route('/bite', methods =['GET', 'POST'])
@login_required
def bite():
    form = BiteForm()
    if request.method =='POST' and form.validate_on_submit():
        location = form.location.data.lower()
        bite_search = Bite.query.filter_by(name=bite).first()
        if not bite_search:
            url = f'https://api.yelp.com/v3/businesses/search?location={location}'

            response = requests.get(url)
            if response.ok:
                bite = response.json()
                random_bite=random.randint(0,49)
                bite_dict={
                    "name": bite['businesses'][random_bite]["name"],
                    "image_url": bite['businesses'][random_bite]["image_url"],
                    "url": bite['businesses'][random_bite]["url"],
                    "categories": bite['businesses'][random_bite]["categories"][0]["title"]
                }
                bite_search = Bite()
                bite_search.from_dict(bite_dict)
                bite_search.save()

            else: 
                flash("This is not a valid location!", 'danger')
                return redirect(url_for('main.bite'))
        return render_template('bite.html.j2', bite=bite_search, form=form)
    return render_template('bite.html.j2', form=form)
