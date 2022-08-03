from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')


@app.route("/dynamicvsm")
def dynamicvsm():
    return '''
    <br>
    <h1>dynamicVSM<h1/>
    <br>
    <h3>IT Cloud Consulting and Digital Transformation<h3/>
    <br>
    <h4>dynamicVSM.com is a confluence for DevOps and Value Stream Management. It is a resource for code snippets, clone-able demos, educational exercises, related information and industry news. Our aim is to collect and share industry knowledge and techniques to build partnerships that help people and businesses grow in the tech industry. <h4/>
    <br>
    Visit: <a href="https://www.dynamicvsm.com">https://www.dynamicvsm.com</a>
    <br>
    '''

@app.route("/cava")
def cava():
    return '''
    <br>
    <h1>CAVA<h1/>
    <br>
    <h3>Greek-American restaurant chain<h3/>
    <br>
    <h4>CAVA is a growing Mediterranean culinary brand with a flavorful and healthy fast-casual restaurant experience featuring customizable & craveable salads, grain bowls, pitas, and house-made juices.<h4/>
    <br>
    Visit: <a href="https://www.cava.com">https://www.cava.com</a>
    <br>
    '''



@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
