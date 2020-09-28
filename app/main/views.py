from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from . import main
from .forms import UpdateProfile,PromotionPitch, PickupLinesPitch, ProductPitch,InterviewPitch,PromotionComment,ProductComment,PickupComment,InterviewComment
from flask_login import login_required, current_user
from .. import db,photos
from ..models import User,Role, Promotion,PickupLines,Product,Interview,PromotionComments,ProductComments,PickupComments,InterviewComments
import markdown2



@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    title = 'Home - Welcome to The Pitch of Your Life'

    return render_template('index.html', title=title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/category/promotionpitch', methods=['GET', 'POST'])
@login_required
def promotion():
    form = PromotionPitch()
    title = 'Post a pitch'
    if form.validate_on_submit():
        post = form.post.data
        body = form.body.data
        new_promotion = Promotion(post=post, user=current_user, body=body)
        new_promotion.save_promotion()
        return redirect(url_for('.listpromotion'))
    return render_template("promotionpitch.html", promotion_form=form, title=title)


@main.route('/category/pickuppitch', methods=['GET', 'POST'])
@login_required
def pickuppitch():
    form = PickupLinesPitch()
    title = 'Post a pitch'
    if form.validate_on_submit():
        post = form.post.data
        body = form.body.data
        new_pickupline = PickupLines(post=post, user=current_user, body=body)
        new_pickupline.save_pickuplines()
        return redirect(url_for('.listpickuppitch'))
    return render_template("pickup_pitch.html", pickup_form=form, title=title)

@main.route('/category/productpitch', methods=['GET', 'POST'])
@login_required
def productpitch():
    form = ProductPitch()
    title = 'Post a pitch'
    if form.validate_on_submit():
        post = form.post.data
        body = form.body.data
        new_product = Product(post=post, user=current_user, body=body)
        new_product.save_product()
        return redirect(url_for('.listproducts'))
    return render_template("productpitch.html", product_form=form)

@main.route('/category/interviewpitch', methods=['GET', 'POST'])
@login_required
def interview():
    form = InterviewPitch()
    title = 'Post a pitch'
    if form.validate_on_submit():
        post = form.post.data
        body = form.body.data
        new_interview = Interview(post=post, user=current_user, body=body)
        new_interview.save_interview()
        return redirect(url_for('.listinterview'))
    return render_template("interviewpitch.html", interview_form=form,title=title)

#Productlist

@main.route('/category/product')
def listproducts():
    title = 'Products'
    posts = Product.query.all()
    return render_template("products.html", mypost=posts,title=title)


@main.route('/product/<int:id>', methods=['POST', 'GET'])
def displayproduct(id):
    products = Product.query.get(id)
    form = ProductComment()
    if form.validate_on_submit():
        comment = form.comment.data
        new_productcomment = ProductComments(comment=comment, product_id=id, user=current_user)
        new_productcomment.save_productcomments()

    comments = ProductComments.query.filter_by(product_id=id).all()
    return render_template('prod_display.html', products=products, comment_form=form, comments=comments)

#Promolist
    
@main.route('/category/promotion')
def listpromotion():
    title = 'Promotion'
    posts = Promotion.query.all()
    return render_template("promotion.html", mypost=posts,title=title)


@main.route('/promotion/<int:id>', methods=['POST', 'GET'])
def displaypromotion(id):
    promo = Promotion.query.get(id)
    form = PromotionComment()
    if form.validate_on_submit():
        comment = form.comment.data
        new_promotioncomment = PromotionComments(comment=comment, promo_id=id, user=current_user)
        new_promotioncomment.save_promotioncomments()

    comments = ProductComments.query.filter_by(promo_id=id).all()
    return render_template('promo_display.html', promo=promo, comment_form=form, comments=comments)

 #PickupList

@main.route('/category/pickuplines')
def listpickuppitch():
    title = 'Pickup Lines'
    posts = PickupLines.query.all()
    return render_template("pickup.html", mypost=posts,title=title)


@main.route('/pickuplines/<int:id>', methods=['POST', 'GET'])
def displaypickupline(id):
    pickup = PickupLines.query.get(id)
    form = PickupComment()
    if form.validate_on_submit():
        comment = form.comment.data
        new_pickupcomment = PickupComments(comment=comment, pickuplines_id=id, user=current_user)
        new_pickupcomment.save_pickupcomments()

    comments = PickupComments.query.filter_by(pickuplines_id=id).all()
    return render_template('pickup_display.html', pickup=pickup, comment_form=form, comments=comments)

#InterviewList

@main.route('/category/interview')
def listinterview():
    title = 'Interviews'
    posts = Interview.query.all()
    return render_template("interview.html", mypost=posts,title=title)


@main.route('/interview/<int:id>', methods=['POST', 'GET'])
def displayinterview(id):
    interview = Interview.query.get(id)
    form = InterviewComment()
    if form.validate_on_submit():
        comment = form.comment.data
        new_interviewcomment = InterviewComments(comment=comment, interview_id=id, user=current_user)
        new_interviewcomment.save_interviewcomments()

    comments = InterviewComments.query.filter_by(interview_id=id).all()
    return render_template('interview_display.html', interview=interview, comment_form=form, comments=comments)

@main.route('/like/<int:interview_id>/<action>')
@login_required
def interviewlike_action(interview_id, action):
    interviewlikes = Interview.query.filter_by(id=interview_id).first_or_404()
    if action == 'like':
        current_user.like_post(interviewlikes)
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_post(interviewlikes)
        db.session.commit()
    return redirect(request.referrer)

@main.route('/like/<int:product_id>/<action>')
@login_required
def productlike_action(product_id, action):
    productlikes = Product.query.filter_by(id=product_id).first_or_404()
    if action == 'like':
        current_user.like_post(productlikes)
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_post(productlikes)
        db.session.commit()
    return redirect(request.referrer)

@main.route('/like/<int:pickuplines_id>/<action>')
@login_required
def pickuplike_action(pickuplines_id, action):
    pickupikes = PickupLines.query.filter_by(id=pickuplines_id).first_or_404()
    if action == 'like':
        current_user.like_post(pickupikes)
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_post(pickupikes)
        db.session.commit()
    return redirect(request.referrer)

@main.route('/like/<int:promotion_id>/<action>')
@login_required
def promolike_action(promotion_id, action):
    promolikes = Promotion.query.filter_by(id=promotion_id).first_or_404()
    if action == 'like':
        current_user.like_post(promolikes)
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_post(promolikes)
        db.session.commit()
    return redirect(request.referrer)