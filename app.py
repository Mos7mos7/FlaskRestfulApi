from flask import Flask

from resources.courses import course_api
from resources.reviews import review_api
import models


app=Flask(__name__)
app.register_blueprint(course_api)
app.register_blueprint(review_api)

@app.route('/')
def hello_world():
    return 'hello world'

if __name__=='__main__':
   # models.initalize()
    app.run(port=8000,debug=True,host='127.0.0.1')
