from app import app, db
from models import User

with app.app_context():
    user = User.query.filter_by(email='jayson.ranckjay@gmail.com').first()
    if user:
        db.session.delete(user)
        db.session.commit()
        print('User deleted successfully!')
    else:
        print('User not found!')
