from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime





# Create a form class
class rewardform(FlaskForm):
    reward_name = StringField('Name: ', validators=[DataRequired()])
    reward_submit = SubmitField('Submit')


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/manage_rewards')
def rmanage():
    return render_template('rmanage.html')

@app.route('/add_rewards', methods=['GET','POST'])
def addrewards():
    reward_name=None
    form=rewardform()
    if form.validate_on_submit():
        reward_name=form.reward_name.data
        form.reward_name.data=''
        flash('Added Successfully','success')
    return render_template('addr.html',reward_name=reward_name,form=form)
