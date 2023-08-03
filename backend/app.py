from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__) #An instance of the Flask class
CORS(app, resources={r"/*": {"origins": "*"}})

#Array representing the tiles of the map
__map__ = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]

def fetch_map():
    return __map__

def update_map(a,b, value):
    __map__[a][b] = value

def find_path(algorithm):
    pass

#Controller for choosing points on the map
def choose_points():
    #Point A
    print("Select a sqare for Starting position")
    points = [(0,0), (0,0)]
    #user input 
    start = 0,0 #Dummy input
    points[0] = start
    #update __map__
    
    #Point B
    print("Select a sqare for Finishing position")
    finish = 20,20 #Dummy input
    points[1]= finish
    #update __map__
    
    return points

#Controller for making walls in the map
def make_walls():
    choosing = True
    count = 0
    while(choosing):
        #get clicked square
        points = (0,0) #input
        __map__[points[0]][points[1]] = 1
        if(count>10):
            choosing = False
        count+=1        

#--------------------- API endpoints ---------------------
@app.route('/generate_map', methods=['GET'])
def generate_map_endpoint():
    choose_points() #First get the starting and ending positions
    make_walls() #Get user input for walls
    return jsonify(__map__)

#Responds to request for the map array from the front end
@app.route('/fetch_map', methods=['GET'])
def fetch_map_endpoint():
    map = fetch_map()
    return jsonify(map)

#Responds to request for the map array from the front end
@app.route('/update_map', methods=['POST'])
def update_map_endpoint():
    global __map__
    data = request.json
    i = data['i']
    j = data['j']
    value = data['value']
    __map__[i][j] = value

    return jsonify(__map__)

@app.route('/clear_map', methods=['POST'])
def clear_map_endpoint():
    global __map__
    temp_map = np.zeros((18,20), dtype=int)
    __map__ = temp_map.tolist()
    return jsonify(__map__)


@app.route('/find_path', methods=['POST'])
def path_endpoint():
    algorithm = request.json['algorithm']
    map = request.json['map']
    path = find_path(algorithm, map)
    return jsonify(path)


if __name__ == '__main__':
    app.run(debug=True)