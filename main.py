from aiohttp import web
import jinja2
import aiohttp_jinja2

def setup_routes(application):
    """function for setting urls application"""
    from bookshelf.routers import setup_routes as setup_bookshelf_routes
    setup_bookshelf_routes(application)

def setup_external_libraries(application):
    """function for setting directories libraries"""
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader("templates"))

def setup_app(application):
    """function for setting application"""
    setup_external_libraries(application)
    setup_routes(application)

app = web.Application()

if __name__ == "__main__":
    setup_app(app)
    web.run_app(app, port=8080)
