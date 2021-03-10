from flask import Flask

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def root(planet_name):
    return f'''
        <!DOCTYPE html> 
        <html>
            <head>
                <meta charset="utf-8">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
                rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
                crossorigin="anonymous">
                <title>Варианты выбора</title>
            </head>
            <body>
                <h1>Моё предложение: {planet_name}</h1>
                <h3>Эта планета близка к Земле;</h2>
                <h3 class="alert alert-success">На ней много необходимых ресурсов;</h3>
                <h3 class="alert alert-secondary">На ней есть вода и атмосфера;</h3>
                <h3 class="alert alert-warning">На ней есть небольшое магнитное поле;</h3>
                <h3 class="alert alert-danger">Наконец, она просто красива!</h3>
            </body>
        </html>
        '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
