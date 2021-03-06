from flask import Flask, render_template
from flask import jsonify
from flask import request

app = Flask(__name__)

carData = [
    {
        'id':'1',
        'brand':'Tata',
        'model':'Hexa',
    },
    {
        'id':'2',
        'brand':'Honda',
        'model':'City',
    },
    {
        'id':'3',
        'brand':'Mahindra',
        'model':'Thar',
    },
    {
        'id':'4',
        'brand':'Maruti',
        'model':'Swift',
    },
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardata/car',methods=['GET'])
def getAllCars():
    return jsonify({'cars':carData})

@app.route('/cardata/car/<carId>',methods=['GET'])
def getCar(carId):
    car = [ car for car in carData if (car['id'] == carId) ] 
    return jsonify({'car':car})


@app.route('/cardata/car/<carId>',methods=['PUT'])
def updateCar(carId):

    em = [ car for car in carData if (car['id'] == carId) ]

    if 'model' in request.json : 
        em[0]['model'] = request.json['model']

    if 'brand' in request.json:
        em[0]['brand'] = request.json['brand']

    return jsonify({'car':em[0]})


@app.route('/cardata/car',methods=['POST'])
def createCar():

    dat = {
    'id':request.json['id'],
    'model':request.json['model'],
    'brand':request.json['brand']
    }
    carData.append(dat)
    return jsonify(dat)

@app.route('/cardata/car/<carId>',methods=['DELETE'])
def deleteCar(carId):
    em = [ car for car in carData if (car['id'] == carId) ]

    if len(em) == 0:
       abort(404)

    carData.remove(em[0])
    return jsonify({'response':'Success'})

if __name__ == '__main__':
 app.run()