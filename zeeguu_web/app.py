# -*- coding: utf8 -*-
import os
import os.path
import sys
import flask
import flask_assets
from zeeguu_web.crosscutting_concerns import CrossDomainApp

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

# *** Starting the App *** #
app = CrossDomainApp(__name__)

config_file = os.environ['ZEEGUU_WEB_CONFIG']
app.config.from_pyfile(config_file, silent=False)
configuration = app.config

assert "ZEEGUU_API" in app.config

print(" == Web running with API: " + app.config['ZEEGUU_API'])
# the umr blueprint needs to have the ZEEGUU_API in the os.environ['ZEEGUU_API']
os.environ['ZEEGUU_API'] = app.config['ZEEGUU_API']

from .account import account
from .bookmarks import bookmarks_blueprint
from .static_pages import static_pages

app.register_blueprint(account)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(static_pages)

from zeeguu_exercises import ex_blueprint

app.register_blueprint(ex_blueprint, url_prefix="/practice")

from umr import reader_blueprint

app.register_blueprint(reader_blueprint, url_prefix="/read")

env = flask_assets.Environment(app)
env.cache = app.instance_path
env.directory = os.path.join(app.instance_path, "gen")
env.url = "/gen"
env.append_path(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "static"
), "/static")


# create the instance folder and return the path
def instance_path(app):
    path = os.path.join(app.instance_path, "gen")
    try:
        os.makedirs(path)
    except Exception as e:
        print(("exception" + str(e)))
        if not os.path.isdir(path):
            raise
    return path


instance = flask.Blueprint("instance", __name__, static_folder=instance_path(app))
app.register_blueprint(instance)
