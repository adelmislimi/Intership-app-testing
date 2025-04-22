from flask import Blueprint, request, jsonify
from .models import Internship, Application
from . import db

main = Blueprint('main', __name__)

@main.route('/internships', methods=['GET'])
def get_internships():
    internships = Internship.query.all()
    return jsonify([{"id": i.id, "title": i.title, "description": i.description} for i in internships])

@main.route('/internships', methods=['POST'])
def post_internship():
    data = request.get_json()
    internship = Internship(title=data['title'], description=data['description'])
    db.session.add(internship)
    db.session.commit()
    return jsonify({"message": "Internship posted!"}), 201

@main.route('/apply', methods=['POST'])
def apply():
    data = request.get_json()
    application = Application(student_name=data['student_name'], internship_id=data['internship_id'])
    db.session.add(application)
    db.session.commit()
    return jsonify({"message": "Application submitted!"}), 201
