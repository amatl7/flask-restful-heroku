from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import psycopg2


app = Flask(__name__)
api = Api(app)
CORS(app)


class status (Resource):
    def get(self):
        try:
            return {'data': 'Api is Running'}
        except:
            return {'data': 'An Error Occurred during fetching Api'}


class Sum(Resource):
    def get(self, a, b):
        return jsonify({'data': a+b})


api.add_resource(status, '/')
api.add_resource(Sum, '/add/<int:a>,<int:b>')

# class executeQuery (Resource):
#     def get(self, queryStr):
#         try:
#             cursor.execute(queryStr)
#             myArr = []
#             myStr = ""

#             for query in cursor:
#                 myArr.append(str(query))
#                 myStr += str(query) + '.'
#             return {'QueryResult':myArr}
#         except:
#             return []


# api.add_resource(executeQuery, '/data/<queryStr>')

class getItemTable (Resource):
    def get(self):
        connection = psycopg2.connect(host='csce-315-db.engr.tamu.edu', database='csce315_912_11', user='csce315_912_matl', password='1')
        cursor = connection.cursor()
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

# class getMenuTable (Resource):
#     def get(self):
#         try:
#             cursor.execute('SELECT * FROM menutable')
#             myArr = []

#             for query in cursor:
#                 myArr.append(str(query))
#             # Returning an api for showing in  reactjs
#             return {
#                 'QueryResult':myArr
#                 }
#         except:
#             return []


# api.add_resource(getMenuTable, '/data/menutable')

# class getOrderTable (Resource):
#     def get(self):
#         try:
#             cursor.execute('SELECT * FROM ordertable')
#             myArr = []

#             for query in cursor:
#                 myArr.append(str(query))
#             # Returning an api for showing in  reactjs
#             return {
#                 'QueryResult':myArr
#                 }
#         except:
#             return []


# api.add_resource(getOrderTable, '/data/ordertable')

# class runUpdate (Resource):
#     def get(self, queryStr):
#         try:
#             cursor.execute(queryStr)

#             # Returning an api for showing in  reactjs
#             connection.commit()
#             return {
#                 'QueryResult':'Success'
#                 }
#         except:
#             return 'Query failed'


# api.add_resource(runUpdate, '/result/<queryStr>')

if __name__ == '__main__':
    app.run()