from flask import Flask
app = Flask(__name__)

Filey = open("PikeTechResume.htm", mode= 'r')
webString = Filey.read()

@app.route('/admin')
def idontlikeyou():
    return webString


if __name__ == '__main__':
    app.run()
