from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

types = {
    'farm': { 'min': 10, 'max': 20},
    'cave': { 'min': 5, 'max': 10},
    'house': { 'min': 2, 'max': 50},
    'casino': { 'min': -50, 'max': 50}
} 

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'log' not in session:
        session['log'] = ''
    if 'moves' not in session:
        session['moves'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    print ('processing money')
    session['moves'] += 1
    print (request.form)
    # clear logs+score if user clicks reset button
    if request.form['type']=="reset":
        session.clear()
        return redirect('/')
    # deactivate all "find gold" buttons once user has made 15 moves.  NO CHEATING!
    if session['moves']<=15:
        print ("*"*40)
        min=types[request.form['type']]['min']
        max=types[request.form['type']]['max']
        change=random.randint(min,max)
        session['gold']+=change
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        if change < 0:
            log = "<div class='red small'>Entered a casino and lost "+str(change)+" gold... Ouch. ("+str(now)+")</div>"
        else:
            log = "<div class='green small'>Earned "+str(change)+" from the "+request.form['type']+"! ("+str(now)+")</div>"
        session['log']=log+session['log']
    return redirect('/')

if __name__=="__main__":      
    app.run(debug=True)  