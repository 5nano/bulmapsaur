from flask import Flask
from flask import request, jsonify
import json

app = Flask(__name__)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)



@app.route('/postjson', methods=['GET'])
def postJsonHandler():
    p1 = Person("John", 36)
    p1.myfunc()
    return json.dumps(p1.__dict__)


app.run(port=8090)