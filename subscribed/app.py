from flask import Flask, render_template, redirect, url_for
from github3 import repository, user, GitHubError


app = Flask(__name__)


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
