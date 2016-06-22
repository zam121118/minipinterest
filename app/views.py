#-*- coding: utf-8 -*-
#视图是响应来自网页浏览器的请求的处理器。在 Flask 中，视图是编写成 Python 函数。每一个视图函数是映射到一个或多个请求的 URL

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname': 'Miguel' } # fake user
	posts=[#fake array of posts
		{
			'author' : { 'nickname' : 'John' },
			'body' : 'Beautiful day in portland!'
		},
		{ 
			'author' : { 'nickname' : 'Susan' },
			'body' : 'The Avengers movie was so cool!'
		}
	]
	return render_template("index.html",title = 'Home',user = user,posts = posts)

@app.route('/login', methods = [ 'GET', 'POST' ])
def login():
	form = LoginForm()  ##form views
	if form.validate_on_submit():
		#accept form data
		flash('Login requested for OpenID = " '+ form.openid.data + '",remember_me = ' + str(form.remember_me.data))
		return redirect('/index')
	return render_template('login.html',
		title = 'Sign In',
		form = form,
		providers = app.config['OPENID_PROVIDERS'])
