from fastapi import FastAPI

try:
    app = FastAPI()

    @app.get('/')

    def function():
        return{'message':'hello,FastApi'}
except Exception as e:
    print('error message:',e)   