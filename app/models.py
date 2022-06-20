from app import db, login
from flask_login import UserMixin
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id= db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email= db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    created_on= db.Column(db.DateTime, default=dt.utcnow)
    icon= db.Column(db.String)
    def __repr__(self):
        return f'<User: {self.email} | {self.id}>'

    def __str__(self):
        return f'<User: {self.email} | {self.first_name} {self.last_name}>'
    
    def hash_password(self, original_password):
        return generate_password_hash(original_password)

    def check_hashed_password(self, login_password):
        return check_password_hash(self.password, login_password)

    def from_dict(self,data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email=data['email']
        self.password = self.hash_password(data['password'])
        self.icon = data['icon']

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_icon_url(self):
        return f'https://avatars.dicebar.com/api/initials/{self.icon}.svg'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Bite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    image_url=db.Column(db.String)
    url=db.Column(db.String)
    categories= db.Column(db.String)

    def __repr__(self):
        return f'<Bite: {self.id} | Body: {self.name}'

    def from_dict(self, bite_dict):
        self.name=bite_dict["name"]
        self.image_url=bite_dict["image_url"]
        self.url=bite_dict["url"]
        self.categories=bite_dict["categories"]

    def to_dict(self):
        data={
            'id':self.id,
            'name': self.name,
            'image_url': self.image_url,
            'url': self.url,
            'categories':self.categories
        }
        return data
    
    def save(self): 
        db.session.add(self)
        db.session.commit()