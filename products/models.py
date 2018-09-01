from sqlalchemy import Column, Integer, String
from core.database import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    price = Column(Integer)
    description = Column(String(120))
    img_path = Column(String(120))

    def __init__(self, title=None, price=None, description=None, img_path=None):
        self.title = title
        self.price = price
        self.description = description
        self.img_path = img_path

    def __repr__(self):
        return '<Product %r>' % self.title

