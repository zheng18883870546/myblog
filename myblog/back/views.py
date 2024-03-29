from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from back.models import User, Article, ArticleType, db
from utils.functions import is_login

back_blue = Blueprint('back',__name__)


@back_blue.route('/index/')
@is_login
def index():
    return render_template('back/index.html')


@back_blue.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('back/register.html')
    if request.method == 'POST':
        # 获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if username and password and password2:
            # 判断该账号是否被注册过
            user = User.query.filter(User.username == username).first()
            if user:
                error = '该账号已经注册，请更换账号'
                return render_template('back/register.html', error=error)
            else:
                if password2 == password:
                    # 保存数据
                    user = User()
                    user.username = username
                    user.password = generate_password_hash(password)
                    user.save()
                    return redirect(url_for('back.login'))

                else:
                    # 密码错误
                    error = '两次密码不一致'
                    return render_template('back/register.html', error=error)

        else:
            error = '请填写完整的信息'
            return render_template('back/register.html', error=error)


@back_blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('back/login.html')
    if request.method == 'POST':
        # 获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user = User.query.filter(User.username == username).first()
            if not user:
                error = '该账号不存在，请去注册'
                return render_template('back/login.html', error=error)
            if not check_password_hash(user.password, password):
                error = '密码错误，请输入正确的密码'
                return render_template('back/login.html', error=error)
            # 账号和密码匹配正确，跳转到首页
            session['user_id'] = user.id
            return redirect(url_for('back.index'))
        else:
            error = '请填写完整的登录信息'
            return render_template('back/login.html', error=error)


@back_blue.route('/logout/',methods=['GET'])
@is_login
def logout():
    del session['user_id']
    return redirect(url_for('back.login'))


@back_blue.route('/a_type/',methods=['GET','POST'])
@is_login
def a_type():
    if request.method == 'GET':
        types = ArticleType.query.all()
        return render_template('back/category_list.html', types=types)


@back_blue.route('/add_type/',methods=['GET', 'POST'])
@is_login
def add_type():
    if request.method == 'GET':
        return render_template('back/category_add.html')
    if request.method == 'POST':
        atype = request.form.get('atype')
        if atype:
            # 保存分类信息
            art_type = ArticleType()
            art_type.t_name = atype
            db.session.add(art_type)
            db.session.commit()
            return redirect(url_for('back.a_type'))
        else:
            error = '请填写分类信息'
            return render_template('back/category_add.html', error=error)


@back_blue.route('/del_type/<int:id>/', methods=['GET'])
@is_login
def del_type(id):
    # 删除分类
    atype = ArticleType.query.get(id)
    db.session.delete(atype)
    db.session.commit()
    return redirect(url_for('back.a_type'))


@back_blue.route('/article_list/', methods=['GET'])
@is_login
def article_list():
    page = int(request.args.get('page', 1))

    # 每一页的条数多少，默认为10条
    per_page = int(request.args.get('per_page', 10))

    # 查询当前第几个的多少条数据
    paginate = Article.query.order_by('id').paginate(page, per_page, error_out=False)
    articles = paginate.items
    return render_template('back/article_list.html', articles=articles, paginate=paginate)


@back_blue.route('/article_add/', methods=['GET', 'POST'])
@is_login
def article_add():
    if request.method == 'GET':
        types = ArticleType.query.all()
        return render_template('back/article_detail.html', types=types)

    if request.method == 'POST':
        title = request.form.get('name')
        desc = request.form.get('desc')
        category = request.form.get('category')
        content = request.form.get('content')
        if title and desc and category and content:
            # 保存
            art = Article()
            art.title = title
            art.desc = desc
            art.content = content
            art.type = category
            db.session.add(art)
            db.session.commit()
            return redirect(url_for('back.article_list'))
        else:
            types = ArticleType.query.all()
            error = '请填写完整的文章信息'
            return render_template('back/article_detail.html', error=error, types=types)


@back_blue.route('/article_change/<int:id>/', methods=['GET', 'POST'])
@is_login
def article_change(id):
    if request.method == 'GET':
        types = ArticleType.query.all()
        article = Article.query.get(id)
        return render_template('back/article_change.html', article=article, types=types)
    if request.method == 'POST':
        title = request.form.get('name')
        desc = request.form.get('desc')
        category = request.form.get('category')
        content = request.form.get('content')
        if title and desc and category and content:
            # 保存
            art = Article()
            art.title = title
            art.desc = desc
            art.content = content
            art.type = category
            db.session.commit()
            return redirect(url_for('back.article_list'))
        else:
            article = Article.query.get(id)
            types = ArticleType.query.all()
            error = '请修改文章信息'
            return render_template('back/article_change.html', error=error, article=article, types=types)


@back_blue.route('/del_article/<int:id>/', methods=['GET'])
@is_login
def del_article(id):
    if request.method == 'GET':
        article = Article.query.get(id)
        db.session.delete(article)
        db.session.commit()
        return redirect(url_for('back.article_list'))


@back_blue.route('/user_list/', methods=['GET'])
@is_login
def user_list():
    if request.method == 'GET':
        return render_template('back/user_list.html')
    if request.method == 'POST':
        pass