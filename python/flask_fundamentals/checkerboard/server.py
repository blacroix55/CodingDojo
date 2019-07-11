from flask import Flask, render_template
app = Flask(__name__)    

@app.route ('/<int:x>')
def x_only(x):
    y=x
    color0="red"
    color1="green"
    return render_template('index.html',x=x,y=y,color0=color0,color1=color1)

@app.route ('/<int:x>/<int:y>')
def x_and_y(x,y):
    color0="red"
    color1="green"
    return render_template('index.html',x=x,y=y,color0=color0,color1=color1)

@app.route ('/<int:x>/<int:y>/<color0>/<color1>')
def x_and_y_and_colors(x,y,color0,color1):
    return render_template('index.html',x=x,y=y,color0=color0,color1=color1)

if __name__=="__main__":   
    app.run(debug=True)