import socket
import whois

def dns_exists(domain):
    try:
        socket.gethostbyname(domain)
        return True
    except:
        return False


def whois_registered(domain):
    try:
        info = whois.whois(domain)
        return bool(info.domain_name)
    except:
        return False


def check_domain(domain):
    dns = dns_exists(domain)
    registered = whois_registered(domain)

    if registered:
        status = "Registered"
    elif dns:
        status = "DNS Found"
    else:
        status = "Available"

    return {
        "domain": domain,
        "status": status,
        "dns": dns,
        "registered": registered
    }
