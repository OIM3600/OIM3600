# dns_data = {
#     "google.com": "142.250.176.206",
#     "github.com": "140.82.114.4",
#     "www.babson.edu": "54.221.247.18",
# }


# def resolve_domain(domain):
#     if domain in dns_data:
#         return dns_data[domain]
#     else:
#         return None


# domain_name = input("Enter a website domain to resolve: ")
# ip_address = resolve_domain(domain_name)

# print(ip_address)


# =============================
import socket


def resolve_domain(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

domain_name = input("Enter a website domain to resolve: ")
ip_address = resolve_domain(domain_name)

print(ip_address)