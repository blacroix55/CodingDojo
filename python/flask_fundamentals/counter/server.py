from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

# our index route will handle rendering our form:
@app.route('/')
def index():
    try:
        session['root_page_counter']+=1
    except:
        session['root_page_counter']=0
    print (session['root_page_counter'])
    return render_template('index.html')

@app.route('/clicky-clicky', methods=['POST'])
def reset():
    print("Got Post Info")
    print(request.form)
    if 'add-two' in request.form:
        print ('ADD TWO FOUND!')
        session['root_page_counter']+=1
    elif 'reset' in request.form:
        print ('RESET FOUND!')
        session['root_page_counter']=0
    return redirect('/')

# @app.route('/show')
# def show_user():
#     print ("showing the user into from the form")
#     print (request.form)
#     return render_template("show.html")

if __name__ == "__main__":
    app.run(debug=True)