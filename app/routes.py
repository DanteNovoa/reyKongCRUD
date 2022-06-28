from app import application
from flask import render_template, url_for, redirect, flash
from app.forms import SignUpForm
import boto3

db = boto3.resource('dynamodb', region_name='us-east-1')
table = db.Table('signuptable')



@application.route('/')
@application.route('/home')
def home_page():
    return render_template('home.html')


@application.route('/signup', methods=['GET', 'POST'])
def sign_up():
    print("entre al sign up")
    form = SignUpForm()
    if form.validate_on_submit():
        table.put_item(
            Item={
                'email': form.email.data, 'first_name': form.first_name.data, 'last_name': form.last_name.data,
                'mobile': form.mobile.data, 'country': form.country.data,
                'newsletter': form.newsletter.data, 'club': form.club.data
            }
        )
        msg = 'Congratulations {} is now a Premium Member'.format(form.first_name.data)
        flash(msg)
        return redirect(url_for('home_page'))
    return render_template('signup.html', form=form)