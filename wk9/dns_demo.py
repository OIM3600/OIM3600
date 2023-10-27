# dns_map = {
#     'google.com': '142.251.40.228',
#     'babson.edu': '54.86.78.46',
#     'github.com': '140.82.114.4',
#     'one.one.one.one': '1.1.1.1',
# }




# def resolve_domain(domain):
#     if domain in dns_map:
#         return dns_map[domain]
#     else:
#         return None



import socket

def resolve_domain(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except:
        return None

domain_name = input('Enter the domain name to resolve: ')
ip_address = resolve_domain(domain_name)
print(ip_address)
