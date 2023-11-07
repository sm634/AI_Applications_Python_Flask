from flask import Flask, request, redirect, url_for, render_template

app = Flask('crud ops')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

# Redirecting to another web page.
@app.route('/admin')
def admin():
    return redirect('/login')

# using the url_for method to dynamically generate URLs for a given endpoint.
@app.route('/admin')
def admin():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return "<Login Page>"


"""CREATE Operation"""

# simple function for example below.
def create_new_record(name):
    return name

# An example for a Create Operation.
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # access form data
        name = request.form['name']
        # create a new record with the name
        record = create_new_record(name) # assuming a define funtion
        # redirect user to the new record
        return redirect(url_for('read', id=record.id))
    # Render the form for GET request
    return render_template('create.html') # assuming this html file exists.


"""READ Operation"""

# simple function for example below.
def get_record(id):
    return id

# An example of Read Operation
@app.route('/read/<int:id>', methods=['GET'])
def read(id):
    # Get the record by id
    record = get_record(id) # Assuming you have this function defined.
    # Render a template with the record.
    return render_template('read.html', record=record)


"""Update Operation"""

def update_record(id, name):
    id = id.replace(name)
    return id

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        # Access form data
        name = request.form['name']
        # Update the record with the new name
        update_record(id, name) # assuming this function is defined properly.
        return redirect(url_for('read', id=id))
    
    # Render the form for GET request with current data
    record = get_record(id) # Assuming you have this function defined.
    return render_template('update.html', record=record)


"""DELETE Operation"""

def delete_record(id):
    del id

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    # Delete the record
    delete_record(id) # Assuming you have this function defined
    # Redirect use to the homepage
    return redirect(url_for('home'))
