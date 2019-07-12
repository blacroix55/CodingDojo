from flask import Flask, render_template
app = Flask(__name__)    

@app.route('/play/<num>/<color>')  
def playground(num,color):
    boxes={}
    boxes["num"]=int(num)
    boxes["color"]=color
    return render_template('index.html',boxes=boxes)

if __name__=="__main__":   
    app.run(debug=True)