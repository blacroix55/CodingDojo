from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

def startGame():
    session.clear()
    session['number']=random.randint(1,101)
    session['guess_num']=0
    session['started']=True
    print ('random number generated, it is',session['number'])

@app.route('/')
def num_guessing_game():
    try:
        if session['started'] == False: # if the "started" flag is False, restart game
            startGame()
    except: # if "started" flag didn't exist(e.g. initial run of the route '/'), start game
        startGame()
    print ('Asking user to guess the number from 1-100')
    return render_template('index.html')

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    print("Received user's guess")
    session['guess'] = int(request.form['guess'])
    session['guess_num']+=1
    return redirect('/guess')

@app.route('/guess')
def guess():
    print ('Comparing guess to the actual number')
    if session['number']==session['guess']:
        print ('correct')
        session['response']="Correct!" 
    elif session['number']<session['guess']:
        print ('too high')
        session['response']="Too high!"
    elif session['number']>session['guess']:
        print ('too low')
        session['response']="Too low!"
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['started']=False    # Reset the "started" flag
    return redirect('/')

# @app.route('/play_again', methods=['POST'])
# def play_again():
#     print ("redirecting to root, user wants to play again")
#     return redirect('/')

if __name__=="__main__":      
    app.run(debug=True)    