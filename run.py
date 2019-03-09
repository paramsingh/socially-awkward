from social.webserver import create_app

def run():
    create_app().run(debug=True)


if __name__ == '__main__':
    run()
