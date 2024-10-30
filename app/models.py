from sqlalchemy import Column, Integer, String, Float
from app import app, db

class Categories(db.Model):
    id= Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(50), nullable=False, unique=True)

if __name__=="__main__":
    with app.app_context():
        #db.create_all()
        c1= Categories(name="Mobile")
        c2=Categories(name="Tablet")
        db.session.add_all([c1, c2])
        db.session.commit()