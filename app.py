from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
user_name = ""

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        global user_name
        user_name = request.form.get('user_name')
        return redirect(url_for('benvingut'))
    return render_template('index.html')

@app.route("/benvingut")
def benvingut():
    global user_name
    if user_name:
        return render_template('benvingut.html', name=user_name)
    else:
        return redirect(url_for('home'))

# @app.route("/contingut")
# def contingut():
#     global user_name
#     if user_name:
#         return f"Lo siento, {user_name}, de momento no hay contenido disponible"
#     else:
#         return f"No puedo mostrarte el contenido, sin saber quién eres. Por favor entra tu nombre en <a href='{url_for('home')}'>la página inicial</a>."

#millora de codi renderitzant pàgina contingut.html
@app.route("/contingut")
def contingut():
    global user_name
    if user_name:
        return render_template('contingut.html', name=user_name, content_available=True)
    else:
        return render_template('contingut.html', name=None, content_available=False)

if __name__ == "__main__":
    app.run(debug=True)

    