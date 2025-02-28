from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    content_type = db.Column(db.String(10), default='plain')  # "plain" or "html"
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            "id": self.id,
            "recipient": self.recipient,
            "subject": self.subject,
            "content": self.content,
            "content_type": self.content_type,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None
        }