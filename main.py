from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import psycopg2
connection = psycopg2.connect(host='csce-315-db.engr.tamu.edu', database='csce315_912_11', user='csce315_912_matl', password='1')
cursor = connection.cursor()

app = Flask(__name__)
api = Api(app)
CORS(app)

class executeQuery (Resource):
    def get(self, queryStr):
        try:
            cursor.execute(queryStr)
            myArr = []
            myStr = ""

            for query in cursor:
                myArr.append(str(query))
                myStr += str(query) + '.'
            return {'QueryResult':myArr}
        except:
            return []


api.add_resource(executeQuery, '/data/<queryStr>')

class getItemTable (Resource):
    def get(self):
        try:
            cursor.execute('SELECT * FROM itemtable')
            myArr = []

            for query in cursor:
                myArr.append(str(query))
            # Returning an api for showing in  reactjs
            return {
                'QueryResult':myArr
                }
        except:
            return []


api.add_resource(getItemTable, '/data/itemtable')

class getMenuTable (Resource):
    def get(self):
        try:
            cursor.execute('SELECT * FROM menutable')
            myArr = []

            for query in cursor:
                myArr.append(str(query))
            # Returning an api for showing in  reactjs
            return {
                'QueryResult':myArr
                }
        except:
            return []


api.add_resource(getMenuTable, '/data/menutable')

class getOrderTable (Resource):
    def get(self):
        try:
            cursor.execute('SELECT * FROM ordertable')
            myArr = []

            for query in cursor:
                myArr.append(str(query))
            # Returning an api for showing in  reactjs
            return {
                'QueryResult':myArr
                }
        except:
            return []


api.add_resource(getOrderTable, '/data/ordertable')

class runUpdate (Resource):
    def get(self, queryStr):
        try:
            cursor.execute(queryStr)

            # Returning an api for showing in  reactjs
            connection.commit()
            return {
                'QueryResult':'Success'
                }
        except:
            return 'Query failed'


api.add_resource(runUpdate, '/result/<queryStr>')

if __name__ == '__main__':
    app.run()