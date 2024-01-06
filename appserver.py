from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demonstration purposes
data = {
    '1': {'name': 'John', 'age': 30},
    '2': {'name': 'Jane', 'age': 25},
    '3': {'name': 'Bob', 'age': 35}
}

# Endpoint to get all data
@app.route('/api/data', methods=['GET'])
def get_all_data():
    return jsonify(data)

# Endpoint to get data by ID
@app.route('/api/data/<string:item_id>', methods=['GET'])
def get_data(item_id):
    if item_id in data:
        return jsonify(data[item_id])
    else:
        return jsonify({'error': 'Item not found'}), 404

# Endpoint to add new data
@app.route('/api/data', methods=['POST'])
def add_data():
    new_item = request.get_json()
    item_id = str(len(data) + 1)
    data[item_id] = new_item
    return jsonify({'id': item_id, 'message': 'Item added successfully'})

# Endpoint to update data by ID
@app.route('/api/data/<string:item_id>', methods=['PUT'])
def update_data(item_id):
    if item_id in data:
        updated_item = request.get_json()
        data[item_id] = updated_item
        return jsonify({'message': 'Item updated successfully'})
    else:
        return jsonify({'error': 'Item not found'}), 404

# Endpoint to delete data by ID
@app.route('/api/data/<string:item_id>', methods=['DELETE'])
def delete_data(item_id):
    if item_id in data:
        del data[item_id]
        return jsonify({'message': 'Item deleted successfully'})
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    # Run the app with host='0.0.0.0' and port=10000
    app.run(host='0.0.0.0', port=10000, debug=True)