from flask import Flask, render_template, redirect, url_for, make_response
from github3 import repository, user, GitHubError


app = Flask(__name__)

ROBOTS = """User-agent: *
Disallow: /sigmavirus24
Disallow: /sigmavirus24/github3.py
"""
# Only disallow the two links on the front page until I can get requests 
# working with the proxy


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<login>/<repo>')
def repo_subscribers(login, repo):
    try:
        r = repository(login, repo)
    except GitHubError:
        return redirect(url_for('index'))

    return render_template('repo.html', repo=r)


@app.route('/<login>')
def user_subscriptions(login):
    try:
        u = user(login)
    except GitHubError:
        return redirect(url_for('index'))

    return render_template('user.html', user=u)


@app.route('/robots.txt')
def robots():
    resp = make_response()
    resp.data = ROBOTS
    resp.content_type = "text/plain"
    return resp
