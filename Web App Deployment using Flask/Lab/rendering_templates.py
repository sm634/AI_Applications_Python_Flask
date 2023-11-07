from flask import Flask, render_template, request 

app = Flask("Rendering Template", template_folder='templates/')

@app.route('/sample') # static webpage
def getSampleHtml():
    return render_template('sample.html') # use the 'sample.html' script to render the webpage/template generated from that code.  

@app.route('/user/<username>', methods=['GET'])
def greetUser(username):
    return render_template("sample.html", title='SAMPLE', name=username) # rendering the template from sample.html while passing in the arguments expected from that code.

# @app.route('user', methods=['GET'])
# def greetUserBasedOnReq():
#     username = request.args.get("username")
#     return render_template("result.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)
