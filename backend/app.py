from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__) #An instance of the Flask class
CORS(app)
#Function to generate a maze upon request
#Returns an 2d array containing the maze data.
"""Example:
maze =   
  [1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 1, 1],
  [2, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 3],
  [1, 1, 1, 1, 1, 1, 1]
] """
def generate_maze():
    maze = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1],
        [2, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 3],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    return maze

def find_path(algorithm, maze):
    pass

#--------------------- API endpoints ---------------------

@app.route('/generate_maze', methods=['GET'])
def maze_endpoint():
    maze = generate_maze()
    return jsonify(maze)

@app.route('/find_path', methods=['POST'])
def path_endpoint():
    algorithm = request.json['algorithm']
    maze = request.json['maze']
    path = find_path(algorithm, maze)
    return jsonify(path)


if __name__ == '__main__':
    app.run(debug=True)