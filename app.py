from flask import Flask, render_template, request, redirect
import message
import helpers
import os


#creating an object of Flassk class to create the app
app = Flask(__name__)
# os.environ['GOOGLE_APPLICATION_CREDENTIALS']='./static/jsonkey.json'


@app.route('/')
def index():
    if request.method == "GET":
        return render_template('index.html')
    

@app.route('/features', methods = ["GET", "POST"])
def features():
    if request.method == "GET":
        return render_template('features.html')
    
    else:
        phone_number = request.form["phone_number"]
        print(phone_number)
        print(type(phone_number))
        coords = request.form["coords"]
        coordinates = coords.split(',')
        try:
            os.remove('static/AfterImage.png')
            os.remove('static/BeforeImage.png')
            os.remove('static/outputAfter.png')
            os.remove('static/outputBefore.png')
            os.remove('static/result.png')
        except:
            pass
        helpers.getBeforeAndAfterImages(coordinates)
        if phone_number != "":
            message.send_message(phone_number, coords)
        return redirect('/contact')


@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route('/pricing') #by default is GET request
def leaderboard():
    return render_template('pricing.html')


if __name__ == '__main__':
    #./ngrok http 3000
    app.run(port=3000) #debug = True //in order to not run every time