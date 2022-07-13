from app import application
from flask import render_template, url_for, redirect, flash
from app.forms import SignUpForm
import app.spotify as SP
import app.youtube as YT
import boto3


db = boto3.resource('dynamodb', region_name='us-east-1')
table = db.Table('signuptable')


@application.route('/')
@application.route('/home')
def home_page():
    return render_template('home.html')


@application.route('/spotify100', methods=['GET', 'POST'])
def spotify100():
    top = SP.get_top_100()
    top100 = dict(top)
    return render_template('spotify.html', top100=top100)

@application.route('/youtube100', methods=['GET', 'POST'])
def youtube100():
    channel_info = YT.get_channel_info()
    return render_template('youtube.html', channel_info=channel_info)