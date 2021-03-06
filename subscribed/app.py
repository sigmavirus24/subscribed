from flask import (Flask, render_template, redirect, url_for, make_response,
                   Response, flash)
from github3 import GitHub, GitHubError
from os import getenv


gh = GitHub()
gh.set_user_agent('subscribed (https://subscribed.herokuapp.com)')

id, secret = (getenv('GH_ID', ''), getenv('GH_SECRET', ''))
if id and secret:
    gh.set_client_id(id, secret)

app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY', '')


@app.route('/')
def index():
    return render_template('index.html')


# Streaming is necessary for accounts like hcilab
# Taken directly from:
# http://flask.pocoo.org/docs/patterns/streaming/#streaming-from-templates
def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(**context)
    rv.enable_buffering(30)
    return rv


@app.route('/<login>/<repo>')
def repo_subscribers(login, repo):
    try:
        r = gh.repository(login, repo)
    except GitHubError:
        flash('Either the repository {0}/{1} does'.format(login, repo) +
              'not exist or it is not public.')
        return redirect(url_for('index'))

    return Response(stream_template('repo.html', repo=r))


@app.route('/<login>')
def user_subscriptions(login):
    failed = False
    try:
        u = gh.user(login)
    except GitHubError:
        failed = True

    if failed or u.type.lower() != 'user':
        flash('User {0} does not exist.'.format(login))
        return redirect(url_for('index'))

    return Response(stream_template('user.html', user=u))


ROBOTS = """User-agent: *
Disallow: /sigmavirus24
Disallow: /sigmavirus24/github3.py
"""
# Only disallow the two links on the front page until I can get requests
# working with the proxy


@app.route('/robots.txt')
def robots():
    resp = make_response()
    resp.data = ROBOTS
    resp.content_type = "text/plain"
    return resp
