from sqlalchemy.orm import relationship
from gino import Gino
# from sqlalchemy_imageattach.entity import Image, image_attachment


db = Gino()

class Book(db.Model):
    """Model for book in bookshelf"""
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    page = db.Column(db.Integer, nullable=False)
    at_created = db.Column(db.DateTime, nullable=False)
    # photo = image_attachment('BookPicture')
    comments = relationship('Comment')

class Comment(db.Model):
    """Model for comment to books"""
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    at_created = db.Column(db.DateTime, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

#Next step:
# class BookPicture(db.Model, Image):
#     """Model for book's picture"""
#     __tablename__ = 'book_picture' 
#     book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)
#     book = relationship('Book')