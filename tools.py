import dns.resolver, requests, socket
def get_dns(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        ips = []
        for ip in result:
            ips.append(str(ip))
        return ips
    except Exception:
        return []

def get_headers(url):
    try:
        resp = requests.get(url, timeout=5)
        return resp.headers
    except Exception:
        return {}

def check_port(host, port):
    sock = socket.socket()
    sock.settimeout(3)
    result = sock.connect_ex((host, port))
    sock.close()
    return result
