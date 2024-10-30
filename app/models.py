from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app import app, db
from sqlalchemy.orm import relationship

class Categories(db.Model):
    id= Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(50), nullable=False, unique=True)
    prods= relationship('Products', backref='categories', lazy=True)

class Products(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description= Column(String(100), nullable=True)
    image= Column(String(100), nullable=True)
    price= Column(Float)
    categories_id= Column(Integer, ForeignKey(Categories.id), nullable=False)

data= [{
            "id": 1,
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
            "category_id": 1
        }, {
            "id": 2,
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
            "category_id": 2
        }, {
            "id": 3,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 1
        }]

if __name__=="__main__":
    with app.app_context():
        # db.create_all()

        for p in data:
            prod= Products(name=p['name'], description= p['description'],
                           image= p['image'], price=p['price'], categories_id=p['category_id'])
            db.session.add(prod)
        db.session.commit()