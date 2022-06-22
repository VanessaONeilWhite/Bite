from flask import render_template, request, flash, redirect, url_for
import requests
from .import bp as main
from flask_login import login_required, current_user
from ..auth.forms import BiteForm
from app.models import Bite, User
import random

@main.route('/', methods = ['GET'])
@login_required
def index():
    return render_template('index.html.j2')



@main.route('/bite', methods =['GET', 'POST'])
@login_required
def bite():
    form = BiteForm()
    print("how about here")
    if request.method =='POST' and form.validate_on_submit():
        location = form.location.data.lower()
        print("we got here")
        return redirect(url_for("main.bite_city", city=location))    
    return render_template('bite.html.j2', form=form)

@main.route('/bite/<city>', methods=['GET'])
@login_required
def bite_city(city):
    url = f'https://api.yelp.com/v3/businesses/search?location={city}'
    headers = {
        'Authorization': 'Bearer 70P0vBd2yppKIlxa4HU7gRgrfYUm57HayJwLIlINl-lc7Kqp4qMc4dYhNlPCbBIcIs_7eeYzEGBYazlI6pB62XkHFJSEVIZdU_jFdtAYIrmdHPpywRlH8RKV64-oYnYx',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    print(len(response.json()["businesses"]))
    if response.ok:
        bite = response.json()
        random_bite=random.randint(0,len(bite["businesses"])-1)
        bite_dict={
            "name": bite['businesses'][random_bite]["name"],
            "image_url": bite['businesses'][random_bite]["image_url"],
            "url": bite['businesses'][random_bite]["url"],
            "categories": bite['businesses'][random_bite]["categories"][0]["title"]
        }
        bite_search = Bite.query.filter_by(name=bite_dict["name"]).first()
        if not bite_search:
            
            bite_search = Bite()
            bite_search.from_dict(bite_dict)
            bite_search.save()
        

    else: 
        flash("This is not a valid location!", 'danger')
        return redirect(url_for('main.bite'))
    print(city)
    return render_template('bite_city.html.j2', bite=bite_search, city=city)

@main.route('/my_bites')
@login_required
def my_bites():
    my_bites=current_user.bites.all()
    print(my_bites)
    return render_template('my_bites.html.j2', bites=my_bites)

@main.route('/add_to_my_bites', methods=["GET", "POST"])
@login_required
def add_to_my_bites():
    print(request.form, "hi")
    city=request.form.get("city")
    id=request.form.get("id")
    if id:

        grabbed_bite = Bite.query.get(id)
        current_user.add_bites(grabbed_bite)
    return redirect(url_for('main.bite_city', city=city))



@main.route('/pass_bite/<int:id>')
@login_required
def pass_bite(id):
    pass_bite=Bite.qury.get(id)
    current_user.pass_bite(id)
    return redirect(url_for("main.bite"))
