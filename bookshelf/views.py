import aiohttp_jinja2
from aiohttp import web

@aiohttp_jinja2.template("base.html")
async def base(request):
    return {'title': 'Hi aiohttp'}