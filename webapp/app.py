from flask import *  
from torun import crack
app = Flask(__name__, static_url_path='/static')  
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        name=f.filename
        f.save("static/"+name)       
        result=crack(name)

        return render_template("success.html", name = name,result=result,ad="/static/"+name)  
  
if __name__ == '__main__':  
    app.run(debug = True) 