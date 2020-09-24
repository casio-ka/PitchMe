from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'
class Promotion(db.Model):
    __tablename__ = 'promotion'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    body = db.Column(db.String(1000))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment = db.relationship('CommentsPromotion', backref='promotion', lazy='dynamic')

    def save_promotion(self):
        db.session.add(self)
        db.session.commit()

class PromotionComments(db.Model):
    __tablename__ = 'productcomments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    promotion_id = db.Column(db.Integer, db.ForeignKey("promotion.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_promotioncomments(self):
        db.session.add(self)
        db.session.commit()

class PickupLines(db.Model):
    __tablename__ = 'pickuplines'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    body = db.Column(db.String(1000))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_pickuplines(self):
        db.session.add(self)
        db.session.commit()

class Product(db.Model):
    __tablename__ = 'productpitch'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    body = db.Column(db.String(1000))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_productpitch(self):
        db.session.add(self)
        db.session.commit()

class ProductComments(db.Model):
    __tablename__ = 'productcomments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    product_id = db.Column(db.Integer, db.ForeignKey("productpitch.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_productcomments(self):
        db.session.add(self)
        db.session.commit()
    
class Interview(db.Model):
    __tablename__ = 'interview'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    body = db.Column(db.String(1000))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_interview(self):
        db.session.add(self)
        db.session.commit()