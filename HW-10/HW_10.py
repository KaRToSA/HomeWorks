from flask import Flask, request
from flask_wtf import FlaskForm
from flask.json import jsonify
from wtforms import StringField, validators, ValidationError
import os

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)



# 1.
# По адресу /locales должен возвращаться массив в
# формате json с тремя локалями: ['ru', 'en', 'it']

@app.route('/locales', methods=['GET'])
def home():
    py_local = {'RU':'russian','EN':'english',"IT":'italian',"KZ":'kazakh'}
    return jsonify(py_local)


# 2.
# По адресу /sum/<int:first>/<int:second> должен получать
# в url-адресе два числа, возвращать их сумму

@app.route('/sum/<int:first>/<int:second>', methods=['GET'])
def sumer(first,second):
    return str(first+second)

# 3.
#По адресу /greet/<user_name> должен получать имя пользователя,
# возвращать текст 'Hello, имя_которое_прислали'
@app.route('/greet/<user_name>')
def hello(user_name):
    return "Hello, " + user_name


# 4.
# По адресу /form/user должен принимать POST запрос с параментрами:
# email, пароль и подтверждение пароля.
# Необходимо валидировать email, что обязательно присутствует,
# валидировать пароли, что они минимум 6 символов в длину и совпадают.
# Возрващать пользователю json вида:
#  "status" - 0 или 1 (если ошибка валидации),
#  "errors" - список ошибок, если они есть,
#  или пустой список.

def write_to_file_data(file,content,mode="a"):
    # print("Writing data!")
    with open(file,mode = mode,) as f:
        return f.write(content)
def read_the_file_data(file):
    print("Reading file!")
    with open(file) as f:
        return f.read()
def confirm_spassword(form, field):
    if form.data['password'] != form.data['confirm_password']:
        raise ValidationError('Пароли не совпадают"')

class ContactForm(FlaskForm):
    email = StringField(validators=[
                                    validators.InputRequired(),
                                    validators.Email(),
    ])
    password = StringField(validators=[
                                    validators.InputRequired(),
                                    validators.Length(min = 6)
    ])
    confirm_password = StringField(validators = [
                                    validators.InputRequired(),
                                    validators.EqualTo("password")
    ])

@app.route('/form/user',methods=["GET","POST"])
def third():
    status_output = {0: 'Проверка пройдена', 1: 'Ошибка валидации'}
    if request.method == "POST":
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())
        if (form.validate()):
            status_check = jsonify(status_output[0])
            return status_check
        else:
            status_check = jsonify(status_output[1])
            return status_check

# 5.
# По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого
# файла из папки ./files.
# Файлы можно туда положить любые текстовые. А если такого нет - 404.

@app.route('/serve/<path:filename>', methods =['GET', 'POST'])
def show_file(filename):
    opened_file = open(filename, 'r')
    read_file = opened_file.read()
    opened_file.close()
    return read_file

if __name__ == '__main__':
    app.run()
