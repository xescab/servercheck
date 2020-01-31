import requests
import asyncio

def get(server):
    pass

async def ping(server, results):
    pass

async def make_requests(servers, results):
    pass

def ping_servers(servers):
    """Connect to servers and return successes and failures"""
    results = {'success': [], 'failure': []}
    asyncio.run(make_requests(servers, results))
    return results