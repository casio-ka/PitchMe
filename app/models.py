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
    promotion = db.relationship('Promotion', backref='user', lazy='dynamic')
    pickuplines = db.relationship('PickupLines', backref='user', lazy='dynamic')
    product = db.relationship('Product', backref='user', lazy='dynamic')
    interview = db.relationship('Interview', backref='user', lazy='dynamic')
    promotioncomments = db.relationship('PromotionComments', backref='user', lazy='dynamic')
    pickuplinecomments = db.relationship('PickupComments', backref='user', lazy='dynamic')
    productcomments = db.relationship('ProductComments', backref='user', lazy='dynamic')
    interviewcomments = db.relationship('InterviewComments', backref='user', lazy='dynamic')
    interviewlikes = db.relationship('InterviewLikes',foreign_keys='InterviewLikes.user_id',backref='user', lazy='dynamic')
    productlikes = db.relationship('ProductLikes',foreign_keys='ProductLikes.user_id',backref='user', lazy='dynamic')
    pickuplikes = db.relationship('PickupLikes',foreign_keys='PickupLikes.user_id',backref='user', lazy='dynamic')
    promolikes = db.relationship('PromoLikes',foreign_keys='PromoLikes.user_id',backref='user', lazy='dynamic')

#InterviewLikes 
    def like_post(self, interview):
        if not self.has_liked_post(interview):
            like = InterviewLikes(user_id=self.id, interview_id=interview.id)
            db.session.add(like)

    def unlike_post(self, interview):
        if self.has_liked_post(interview):
            InterviewLikes.query.filter_by(user_id=self.id,interview_id=interview.id).delete()

    def has_liked_post(self, interview):
        return InterviewLikes.query.filter(
               InterviewLikes.user_id == self.id,InterviewLikes.interview_id == interview.id).count() > 0
#ProductLikes    
    def like_post(self, product):
        if not self.has_liked_post(product):
            like = ProductLikes(user_id=self.id, product_id=product.id)
            db.session.add(like)

    def unlike_post(self, product):
        if self.has_liked_post(product):
            ProductLikes.query.filter_by(user_id=self.id,product_id=product.id).delete()

    def has_liked_post(self, product):
        return ProductLikes.query.filter(
               ProductLikes.user_id == self.id,ProductLikes.product_id == product.id).count() > 0

#PickupLikes    
    def like_post(self, pickuplines):
        if not self.has_liked_post(pickuplines):
            like = PickupLikes(user_id=self.id, pickuplines_id=pickuplines.id)
            db.session.add(like)

    def unlike_post(self, pickuplines):
        if self.has_liked_post(pickuplines):
            PickupLikes.query.filter_by(user_id=self.id,pickuplines_id=pickuplines.id).delete()

    def has_liked_post(self, pickuplines):
        return PickupLikes.query.filter(
               PickupLikes.user_id == self.id,PickupLikes.pickuplines_id == pickuplines.id).count() > 0

#PromotionLikes    
    def like_post(self, promotion):
        if not self.has_liked_post(promotion):
            like = PromoLikes(user_id=self.id, promotion_id=promotion.id)
            db.session.add(like)

    def unlike_post(self, promotion):
        if self.has_liked_post(promotion):
            PromoLikes.query.filter_by(user_id=self.id,promotion_id=promotion.id).delete()

    def has_liked_post(self, promotion):
        return PromoLikes.query.filter(
               PromoLikes.user_id == self.id,PromoLikes.promotion_id == promotion.id).count() > 0
    

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
    comment = db.relationship('PromotionComments', backref='promotion', lazy='dynamic')
    promolikes = db.relationship('PromoLikes', backref='promotion', lazy='dynamic')

    def save_promotion(self):
        db.session.add(self)
        db.session.commit()

class PromotionComments(db.Model):
    __tablename__ = 'promotioncomments'

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
    comment = db.relationship('PickupComments', backref='pickuplines', lazy='dynamic')
    pickuplikes = db.relationship('PickupLikes', backref='pickuplines', lazy='dynamic')

    def save_pickuplines(self):
        db.session.add(self)
        db.session.commit()

class PickupComments(db.Model):
    __tablename__ = 'pickupcomments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    pickuplines_id = db.Column(db.Integer, db.ForeignKey("pickuplines.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_pickupcomments(self):
        db.session.add(self)
        db.session.commit()

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    body = db.Column(db.String(1000))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment = db.relationship('ProductComments', backref='product', lazy='dynamic')
    productlikes = db.relationship('ProductLikes', backref='product', lazy='dynamic')

    def save_product(self):
        db.session.add(self)
        db.session.commit()

class ProductComments(db.Model):
    __tablename__ = 'productcomments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
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
    comment = db.relationship('InterviewComments', backref='interview', lazy='dynamic')
    interviewlikes = db.relationship('InterviewLikes', backref='interview', lazy='dynamic')

    def save_interview(self):
        db.session.add(self)
        db.session.commit()

class InterviewComments(db.Model):
    __tablename__ = 'interviewcomments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    interview_id = db.Column(db.Integer, db.ForeignKey("interview.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_interviewcomments(self):
        db.session.add(self)
        db.session.commit()

class InterviewLikes(db.Model):
    __tablename__='interviewlikes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    interview_id = db.Column(db.Integer, db.ForeignKey("interview.id"))

class ProductLikes(db.Model):
    __tablename__='productlikes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))

class PickupLikes(db.Model):
    __tablename__='pickuplikes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pickuplines_id = db.Column(db.Integer, db.ForeignKey("pickuplines.id"))

class PromoLikes(db.Model):
    __tablename__='promolikes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    promotion_id = db.Column(db.Integer, db.ForeignKey("promotion.id"))

