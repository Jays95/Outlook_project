from app import app, db
from models import User

with app.app_context():
    db.create_all()
    user = User(email='new.email@example.com')
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    print('User created successfully!')
