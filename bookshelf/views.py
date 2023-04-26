import aiohttp_jinja2
from aiohttp import web
from .models import Book, Comment
from datetime import datetime


@aiohttp_jinja2.template("start.html")
async def start(request):
    books = await Book.query.order_by(Book.id.desc()).gino.all()
    print(books)
    return {'title': 'start', 
            'context': books
            }

@aiohttp_jinja2.template("book.html")
async def book(request):
    book_name = int(request.match_info['name'])
    book = await Book.query.where(Book.id==book_name).gino.first()
    # book = await Book.get(book_name)
    return {'title': book.title, 
            'context': book
            }

class ListBookCommentView(web.View):
    async def get(self):
        url_data = self.request.url
        print(url_data)
        id_book = int(str(url_data).split('/')[-1])
        print(id_book)
        book_comments = await Comment.query.where(Comment.book_id==id_book).gino.all()
        book_comments_data = []
        for comment in book_comments:
            book_comments_data.append({
                    "id": comment.id,
                    "text": comment.text,
                    "at_created": str(comment.at_created),
            })
        return web.json_response(data={'messages': book_comments_data})   
   

class CreateCommentView(web.View):
    async def post(self):
        data = await self.request.json()
        comment = await self.request.app["db"].message.create(
            text=data['text'],
            at_created=datetime.now(),
            book_id=int(data['book']),
        )
        format = "%Y-%m-%d %H.%M.%S"
        time = f"{comment.at_created:{format}}"
        print(time)        
        return web.json_response(data={'message': {
            'id': comment.id,
            'text': comment.text,
            'at_created': time,
            'book_id': int(comment.book_id),
        }})    
    