from flask import Blueprint, request, jsonify
from .mail import send_email
from .models import db, Email
from functools import wraps
from config import Config

routes_app = Blueprint('routes_app', __name__)

def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-KEY')

        if api_key and api_key == Config.API_KEY:
            return view_function(*args, **kwargs)
        else:
            return jsonify({"error": "Unauthorized: Invalid or missing API key"}), 401
    return decorated_function

@routes_app.route('/send', methods=['POST'])
@require_api_key
def send_mail():
    data = request.json
    to_email = data.get('to')
    subject = data.get('subject')
    content = data.get('content')
    content_type = data.get('content_type', 'plain')

    if not all([to_email, subject, content]):
        return jsonify({"error": "Missing required fields"}), 400

    if send_email(to_email, subject, content, content_type):
        # Save email details to the database
        new_email = Email(
            recipient=to_email,
            subject=subject,
            content=content,
            content_type=content_type
        )
        db.session.add(new_email)
        db.session.commit()

        return jsonify({"message": "Email sent successfully", "email": new_email.to_dict()}), 200
    else:
        return jsonify({"error": "Failed to send email"}), 500

@routes_app.route('/emails', methods=['GET'])
@require_api_key
def get_emails():
    emails = Email.query.all()
    return jsonify([email.to_dict() for email in emails]), 200

@routes_app.route('/emails/<int:id>', methods=['GET'])
@require_api_key
def get_email(id):
    email = Email.query.get_or_404(id)
    return jsonify(email.to_dict()), 200

@routes_app.route('/emails/<int:id>', methods=['DELETE'])
@require_api_key
def delete_email(id):
    email = Email.query.get_or_404(id)
    db.session.delete(email)
    db.session.commit()
    return jsonify({"message": "Email deleted successfully"}), 200