from flask import Flask

CONFIG_PATH = "./config.py"

# Создание приложения
app = Flask(__name__)


# Функция вывода страницы с ошибкой 404, если она не найдена
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Страница не найдена</h1><p>Попробуйте другой запрос</p>", 404


# Функция вывода страны с ошибкой 500 по вине сервера
@app.errorhandler(500)
def page_not_found(e):
    return "<h1>Ошибка на стороне сервера</h1><p>Сообщите в тех. поддержку</p>", 500

# Запуск веб-приложения
if __name__ == '__main__':
    app.run()
