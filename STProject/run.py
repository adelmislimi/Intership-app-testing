from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

def create_app():
    app = Flask(__name__)

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["internship_db"]
    internships = db["internships"]
    applications = db["applications"]

    @app.route('/')
    def home():
        return 'Welcome to the Internship API (MongoDB Version)'

    @app.route('/internships', methods=['GET'])
    def get_internships():
        all_data = list(internships.find())
        for item in all_data:
            item['_id'] = str(item['_id'])  # Convert ObjectId to string for JSON
        return jsonify(all_data)

    @app.route('/internships', methods=['POST'])
    def create_internship():
        data = request.get_json()
        internships.insert_one({
            "title": data["title"],
            "description": data["description"]
        })
        return jsonify({"message": "Internship created"}), 201

    @app.route('/apply', methods=['POST'])
    def apply():
        data = request.get_json()
        applications.insert_one({
            "student_name": data["student_name"],
            "internship_id": data["internship_id"]
        })
        return jsonify({"message": "Application submitted"}), 201

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
