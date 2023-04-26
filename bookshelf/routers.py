from .views import CreateCommentView, start, book, ListBookCommentView


def setup_routes(app):
    app.router.add_get("/", start)
    app.router.add_get("/book/{name}", book, name="book_url")
    app.router.add_view("/api/comment_list/{name}", ListBookCommentView, name="book_for_comment")
    app.router.add_view("/api/comment_create", CreateCommentView)
    