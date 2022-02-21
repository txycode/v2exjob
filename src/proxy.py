import aiosocks
from aiosocks.connector import ProxyConnector

conn = ProxyConnector(proxy=aiosocks.Socks5Addr(PROXY_ADDRESS, PROXY_PORT), proxy_auth=None, remote_resolve=True)