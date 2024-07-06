import ssl
import requests

# Check OpenSSL version
print("OpenSSL version:", ssl.OPENSSL_VERSION)

# Test an HTTPS request
try:
    response = requests.get("https://www.google.com")
    print("Request succeeded, status code:", response.status_code)
except requests.exceptions.SSLError as e:
    print("SSL error:", e)


import requests
print(requests.certs.where())