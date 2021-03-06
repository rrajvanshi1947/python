from flask import Flask, redirect, url_for, request, render_template, make_response
app = Flask(__name__)

@app.route('/') #Define the fn first and write app.add_url_rule('/','hello', hello_world)
def hello_world():
    return 'Hello World'

# url_for example
@app.route('/hello/<name>')
def hello_name(name):
    if name == 'roopam':        #Couldn't do isinstance(name, int) or type(name) == 'int' to check for int
        return redirect(url_for('hello_world'))
    else:
        return redirect(url_for('success', name = name))

@app.route('/integercheck/<int:studentid>')
def hello_student(studentid):
    return 'Hello Student %d' %studentid

@app.route('/floatcheck/<float:value>')
def hello_float(value):
    return 'Hello float %f' % value

@app.route('/python/')  #Returns same result for both /python and /python/
def hello_python():
    return 'Hello Python'

@app.route('/success/<name>')
def success(name):
    return '%s has successfully logged in!' % (name.capitalize())

# POST, GET Methods
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':            #Cannot get to print name for if
        user = request.form['nm']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))

# Templates
@app.route('/templatetest/<value>')
def template_test(value):
    return render_template('test.html', name = value)

@app.route('/passfail/<int:value>')
def result(value):
    return render_template('pass_fail.html', score = value)

# Set and Read Cookies
@app.route('/setcookie', methods = ['POST', 'GET'])
def set_cookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('setcookie.html', name = user))
        resp.set_cookie('userID', user)
        return resp

@app.route('/getcookie')
def getCookie():
        name = request.cookies.get('userID')
        return 'The cookie value is %s' %name

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)