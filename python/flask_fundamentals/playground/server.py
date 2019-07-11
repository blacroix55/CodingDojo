from flask import Flask, render_template
app = Flask(__name__)    

@app.route('/play/<num_boxes>')  
def playground(num_boxes):
    boxes={}
    boxes["num"]=int(num_boxes)
    return render_template('index.html',boxes=boxes)

if __name__=="__main__":   
    app.run(debug=True)