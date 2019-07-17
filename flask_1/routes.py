import os
def save_picture(form_picture):
    
    f_name,f_ext=os.path.splitext(form_picture.filename)
    picture_fn = f_name + f_ext
    picture_path=os.path.join(app.root_path,'static/pictures',picture_fn)
    form_picture.save(picture_path)
    
    return picture_fn


from flask import render_template,url_for,flash,redirect,request
from flask_1 import app,db,bcrypt
from flask_1.models import user
from flask_1.forms import RegistrationForm,LoginForm,UpdateAccountForm,DataForm1,DataForm2
from flask_login import login_user,current_user,logout_user,login_required


posts=[
       {
        'name':'Aman Punetha',
        'email':'amanpunetha@gmail.com',
        'date': 'July 01,2019'
        
        
        },
       {
        'name':'Ajay Bisht',
        'email':'ajaybisht@gmail.com',
        'date': 'July 02,2019'
        }
       
       ]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['get','post'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        User=user(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(User)
        db.session.commit()
        flash(f'Thank you for reister!','success')
        flash(f'You are now able to access your account!','success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['get','post'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        User=user.query.filter_by(email=form.email.data).first()
        if User and bcrypt.check_password_hash(User.password,form.password.data):
            login_user(User,remember=form.remember.data)
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password','danger')
    return render_template('login.html',title='Login',form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route("/account",methods=['get','post'])
@login_required
def account():
    form=UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file=save_picture(form.picture.data)
            current_user.image_file=picture_file
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash(f"Your account has been updated!",'success')
        return redirect(url_for('account'))
    elif request.method=='GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
    image_file=url_for('static',filename='pictures/'+ current_user.image_file)
    return render_template('account.html',title='Account',image_file=image_file,form=form)


@app.route("/dataform",methods=['get','post'])
@login_required
def dataform():
    form=DataForm1()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file=save_picture(form.picture.data)
            from flask_1.temp import text_extract
            text_extract(picture_file)
        else:
            print("not done")
        flash(f"Your image is going for data processing .Just wait for result!",'success')
        return redirect(url_for('dataform2'))
       
    image_file=url_for('static',filename='pictures/'+ current_user.image_file)
    return render_template('data_extractor.html',image_file=image_file,title='Data Analyzer',form=form)


@app.route("/dataform2",methods=['get','post'])
@login_required
def dataform2():
    form=DataForm2()
    image_file=url_for('static',filename='pictures/'+ current_user.image_file)
    return render_template('data_visual.html',image_file=image_file,form=form)
    