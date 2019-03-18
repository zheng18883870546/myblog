from flask import Blueprint, render_template, request, redirect, url_for, g
from sqlalchemy import and_, or_

from back.models import Article, ArticleType

web_blue = Blueprint('web', __name__)


@web_blue.route('/index/')
def index():
    page = int(request.args.get('page', 1))

    # 每一页的条数多少，默认为10条
    per_page = int(request.args.get('per_page', 10))

    # 查询当前第几个的多少条数据
    paginate = Article.query.order_by('id').paginate(page, per_page, error_out=False)

    articles = paginate.items
    types = ArticleType.query.all()
    return render_template('web/index.html', articles=articles, types=types, paginate=paginate)


@web_blue.route('/info/<int:id>/')
def info(id):
    article = Article.query.get(id)
    n_article = Article.query.get(id-1)
    return render_template('web/info.html', article=article, n_article=n_article)


@web_blue.route('/category/<int:id>/')
def category(id):
    types = ArticleType.query.all()
    articles = Article.query.filter(Article.type == id).all()
    if not articles:
        error = '未找到相关文章'
        return render_template('web/category.html', articles=articles, types=types, error=error)
    else:
        return render_template('web/category.html', articles=articles, types=types)


@web_blue.route('/search/', methods=['POST'])
def search():
    content = request.form.get('keyboard')
    articles = Article.query.filter(or_(Article.title.contains(content),
                                    Article.content.contains(content))
                                    ).all()
    if request.method == 'POST':
        if not articles:
            error = '没有找到符合条件的文章'
            paginate = {}
            return render_template('web/index.html', error=error, paginate=paginate)
        else:
            paginate = {}
            return render_template('web/index.html', articles=articles, paginate=paginate)


@web_blue.route('/about/')
def about():
    return render_template('web/about.html')


@web_blue.route('/share/')
def share():
    page = int(request.args.get('page', 1))

    # 每一页的条数多少，默认为10条
    per_page = int(request.args.get('per_page', 8))

    # 查询当前第几个的多少条数据
    paginate = Article.query.order_by('id').paginate(page, per_page, error_out=False)

    articles = paginate.items
    return render_template('web/share.html', articles=articles)


@web_blue.route('/content/')
def content():
    article = Article.query.get(22)
    n_article = Article.query.get(21)
    return render_template('web/info.html', article=article, n_article=n_article)

    # return render_template('web/info.html',id=23)


# @web_blue.before_request
# def art_info():
#     types = ArticleType.query.all()
#     articles = Article.query.filter(Article.type == id).all()
#     g.types = types
#     g.articles = articles
# 狗子函数