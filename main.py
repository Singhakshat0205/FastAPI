import fastapi

app = fastapi.FastAPI()

@app.get("/")
def hello():
    return {'message':'Hello, World!'}


@app.get("/about")

def about():
    return {'message':'You are on the about page '}