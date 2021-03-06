# RESTful-Web-Service

GET:
curl -i http://localhost:5000/cardata/car

PUT: 
curl -i -H "Content-Type: application/json" -X PUT -d "{"""model""":"""Civic"""}"  http://localhost:5000/cardata/car/2  

POST:
curl -i -H "Content-Type: application/json" -X POST -d"{"""id""":"""5""","""brand""":"""Toyota""","""model""":"""Fortuner"""}" http://localhost:5000/cardata/car

DELETE:
curl -i -X DELETE http://localhost:5000/cardata/car/5
