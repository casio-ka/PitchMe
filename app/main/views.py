from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from . import main
from .forms import UpdateProfile,PromotionPitch, PickupLines, ProductPitch,InterviewPitch,PromotionComment
from flask_login import login_required, current_user
from .. import db,photos
from ..models import User,Role, Promotion,PickupLines,Product,Interview,PromotionComments



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


@main.route('/category/pickuplines', methods=['GET', 'POST'])
@login_required
def pickuplines():
    form = PickupLines()
    title = 'Post a pitch'
    if form.validate_on_submit():
        post = form.post.data
        body = form.body.data
        new_pick = PickupLines(post=post, user=current_user, body=body)
        new_pick.save_pick()
        return redirect(url_for('.listpickup'))
    return render_template("pickuppitch.html", pickup_form=form, title=title)

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
        return redirect(url_for('.listproduct'))
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
        new_interview.save_production()
        return redirect(url_for('.listinterview'))
    return render_template("interviewpitch.html", interview_form=form,title=title)

@main.route('/category/promotion')
def listproducts():
    title = 'Promotion'
    posts = Promotion.query.all()
    return render_template("promotion.html", mypost=posts,title=title)


@main.route('/promotion/<int:id>', methods=['POST', 'GET'])
def displayproduct(id):
    promotion = Promotion.query.get(id)
    form = PromotionComment()
    if form.validate_on_submit():
        comment = form.comment.data
        new_promo_comment = PromotionComments(comment=comment, promotion_id=id, user=current_user)
        new_promo_comment.save_promo_coments()

    comments = PromotionComments.query.filter_by(promotion_id=id).all()
    return render_template('promotionpitch.html', promotion=promotion, comment_form=form, comments=comments)