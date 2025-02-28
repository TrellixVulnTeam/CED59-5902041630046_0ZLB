from flask import Flask ,render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret'

class LoginForm(FlaskForm):
    name = StringField('name', validators=[InputRequired('A username is required!'), Length(min=5, max=10, message='Must be be')])
    username = StringField('username', validators=[InputRequired('Password is required!')])
    email = StringField('email', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = LoginForm()

    if form.validate_on_submit():
        return '<h1> The username is {}. The password is{}.'.format(form,username.date, form.password.data)
    return render_template("from_baifern.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
