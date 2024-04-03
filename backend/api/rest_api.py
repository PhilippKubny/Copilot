from fastapi import FastAPI

# Defining the api
app = FastAPI()

# The following function gets called whenever the website is loaded
@app.get('/')
async def root():
    return {'message': 'Hello world'}

@app.get('/test/{number}')
async def get_test(number):
    return {'message': f'Your number is {number}'}
