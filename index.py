

from flask import Flask, request, render_template
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def Average() :
    if request.method=="POST":
        x=int(request.form['phy'])
        y=int(request.form['chem'])
        z=int(request.form['math'])
        name = request.form['name']
        avg=float((x+y+z)/3)
        return render_template('average.html',avg=avg,name=name)
    else :
        return render_template('index.html')
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)