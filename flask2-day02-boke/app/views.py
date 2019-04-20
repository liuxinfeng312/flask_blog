from flask import Blueprint, request, render_template, session, redirect, url_for
from app.models import User, Backuser, Article

from app.exts import db, cache

blue=Blueprint('blue',__name__)


def init_views(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def test():
    return redirect(url_for('blue.index'))

@blue.route('/index/')#主页
def index():

    username=session.get('username')
    if username:

        article=Article.query.all()

        return render_template('web/webindex.html', username=username,article=article)
    return redirect(url_for('blue.login'))

@blue.route('/about/')#关于我
def about():
    username = session.get('username')
    if username:
        return render_template('web/webabout.html', username=username)
    return redirect(url_for('blue.login'))
@blue.route('/gbook/')#日记
def gbook():
    username = session.get('username')
    if username:
        return render_template('web/webgbook.html', username=username)
    return redirect(url_for('blue.login'))

@blue.route('/info/')#内容页
def info():
    username = session.get('username')
    if username:
        return render_template('web/webinfo.html', username=username)
    return redirect(url_for('blue.login'))

@blue.route('/infopic/')#内容页
def infopic():
    username = session.get('username')
    if username:
        return render_template('web/webinfopic.html', username=username)
    return redirect(url_for('blue.login'))

@blue.route('/list/')#
def list():
    username = session.get('username')
    if username:
        return render_template('web/weblist.html', username=username)
    return redirect(url_for('blue.login'))

@blue.route('/share/')#照片
def share():
    username = session.get('username')
    if username:
        return render_template('web/webshare.html', username=username)
    return redirect(url_for('blue.login'))
@blue.route('/register/',methods=['POST','GET'])#注册
def register():
    if request.method == 'GET':
        return render_template('web/webregister.html')
    elif request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')

        try:
            user=User()
            user.username=username
            user.password=password
            db.session.add(user)
            db.session.commit()


        except:
            context='该用户已存在'
            return render_template('web/webregister.html' ,context=context)
        session['username'] = username
        return redirect(url_for('blue.index'))


@blue.route('/login/',methods=['POST','GET'])#登陆

def login():
    if request.method=='GET':
        return render_template('web/weblogin.html')
    elif request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        users = User.query.filter(User.username == username).filter(User.password == password)
        if users.count():
            user=users.first()
            session['username']=user.username
            return redirect(url_for('blue.index'))
        else:
            context='用户名或密码错误'
            return render_template('web/weblogin.html',context=context)

@blue.route('/logout/',methods=['POST','GET'])#注销
def logout():
    username=session.get('username')
    if username:
        session.pop('username')
    return redirect(url_for('blue.index'))
#____________________________________________________
#后台管理视图×××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××
@blue.route('/backbase/',methods=['POST','GET'])
def backbase():

    return render_template('back/backbase.html')


@blue.route('/backaddarticle/',methods=['POST','GET'])#添加文章
def backaddarticle():

    if request.method=='GET':
        return render_template('back/backadd-article.html')
    elif request.method=='POST':
        title=request.form.get('title')
        context=request.form.get('content')
        article=Article()
        article.title=title
        article.context=context
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('blue.backarticle'))






@blue.route('/backarticle/',methods=['POST','GET'])#文章内容
def backarticle():
    username=session.get('backusername')
    if username:
        article=Article.query.all()


        return render_template('back/backarticle.html',username=username ,article=article)
    else:
        return redirect(url_for('blue.backlogin'))

@blue.route('/backlogin/',methods=['POST','GET'])#后台登陆
def backlogin():
    if request.method=='GET':


        return render_template('back/backlogin.html')

    elif request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('userpassword')
        users=Backuser.query.filter(Backuser.username==username).filter(Backuser.password==password)
        if users.count():

            user=users.first()
            session['backusername']=user.username
            return  redirect(url_for('blue.backarticle'))
        else:
            context='用户名或密码错误'
            return render_template('back/backlogin.html',context=context)



@blue.route('/backupdate/',methods=['POST','GET'])#更新文章
def backupdate():

    return render_template('back/backupdate-article.html')

@blue.route('/backlogout/')
def backlogout():
    username = session.get('backusername')
    if username:
        session.pop('backusername')
    return redirect(url_for('blue.backarticle'))

