from bookshelf.models import Book, Comment, db
from config import DATABASE_URL


class DBAccessor:
    def __init__(self):
        self.message = Comment
        self.book = Book
        self.db = None

    def setup(self, application):
        application.on_startup.append(self._on_connect)
        application.on_cleanup.append(self._on_disconnect)

    async def _on_connect(self, application):
        self.config = DATABASE_URL
        await db.set_bind(DATABASE_URL)
        self.db = db
        application["db"] = self

    async def _on_disconnect(self, _):
        if self.db is not None:
            await self.db.pop_bind().close()

database_accessor = DBAccessor()
