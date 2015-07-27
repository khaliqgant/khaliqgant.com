import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import requests
import requests_cache

from flask import Flask, render_template

app = Flask(__name__)

requests_cache.install_cache(
    'github_cache', backend='sqlite', expire_after=180
)


def github():
    """ retrieve github activity"""
    username = 'khaliqgant'
    url = "https://api.github.com/users/%s/events" % (username)
    response = requests.get(url)
    # transform this into a dict and probably utf-8 encode
    return response


@app.route('/')
def index():
    gh_activities = github()
    return render_template('layout.html', gh_activities=gh_activities)


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
