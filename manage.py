from subscribed import app
from os import environ


if __name__ == '__main__':
    port = int(environ.get('PORT', '5000'))
    app.run(host='0.0.0.0', port=port)
