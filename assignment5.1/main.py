from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hoho Palm"

if __name__ == '__main__':
    app.run()
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form action="/" method="post">
        Name : <input type="text" name="name"/> Surname : <input type="text" name="surname"/><br>
        Email : <input type="text" name="email"/><br>
        Username : <input type="text" name="Username"/><br>
        Password : <input type="password" name="pass"/><br>
        <input type="submit" name="submit" value="submit">
    </form>
</body>
</html>