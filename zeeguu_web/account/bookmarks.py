from zeeguu_web.account.api.bookmarks import get_learned_bookmarks, get_bookmarks_by_date, star_bookmark, \
    report_learned_bookmark, \
    unstar_bookmark, delete_bookmark, \
    get_top_bookmarks, get_starred_bookmarks, get_bookmarks_for_article
from . import account, login_first
import flask


@account.route("/bookmarks")
@login_first
def bookmarks():
    # d = datetime.datetime.now() - datetime.timedelta(days=7)
    data = get_bookmarks_by_date()

    sorted_dates = data["sorted_dates"]
    urls_for_date = data["urls_for_date"]
    contexts_for_url = data["contexts_for_url"]
    bookmarks_for_context = data["bookmarks_for_context"]
    bookmark_counts_by_date = data["bookmark_counts_by_date"]

    return flask.render_template("bookmarks.html",
                                 sorted_dates=sorted_dates,
                                 urls_for_date=urls_for_date,
                                 contexts_for_url=contexts_for_url,
                                 bookmarks_for_context=bookmarks_for_context,
                                 bookmark_counts_by_date=bookmark_counts_by_date
                                 )

@account.route("/bookmarks_for_article/<int:article_id>")
@login_first
def bookmarks_for_article1(article_id: int):

    data = get_bookmarks_for_article(article_id)

    return flask.render_template("bookmarks_for_article.html", **data)


@account.route("/bookmarks_for_article/<int:article_id>/<int:user_id>")
@login_first
def bookmarks_for_article2(article_id: int, user_id):

    data = get_bookmarks_for_article(article_id, user_id)

    return flask.render_template("bookmarks_for_article.html", **data)


@account.route("/top_bookmarks")
@login_first
def top_bookmarks():
    bookmarks = get_top_bookmarks(10)

    return flask.render_template("bookmarks_top.html",
                                 bookmarks=bookmarks)


@account.route("/learned_bookmarks")
@login_first
def learned_bookmarks():
    bookmarks = get_learned_bookmarks()

    return flask.render_template("bookmarks_learned.html",
                                 bookmarks=bookmarks)


@account.route("/starred_bookmarks")
@login_first
def starred_bookmarks():
    bookmarks = get_starred_bookmarks()

    return flask.render_template("bookmarks_starred.html",
                                 bookmarks=bookmarks)


# These following endpoints are invoked via ajax calls from the bookmarks page
@account.route("/report_learned_bookmark/<bookmark_id>", methods=("POST",))
@login_first
def post_report_learned_bookmark(bookmark_id):
    return report_learned_bookmark(bookmark_id)


@account.route("/delete_bookmark/<bookmark_id>", methods=("POST",))
@login_first
def delete(bookmark_id):
    return delete_bookmark(bookmark_id)


@account.route("/starred_bookmark/<bookmark_id>", methods=("POST",))
@login_first
def starred_word(bookmark_id):
    return star_bookmark(bookmark_id)


@account.route("/unstarred_bookmark/<bookmark_id>", methods=("POST",))
@login_first
def unstarred_word(bookmark_id):
    return unstar_bookmark(bookmark_id)
