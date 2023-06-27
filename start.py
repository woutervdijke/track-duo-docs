import http.client

conn = http.client.HTTPSConnection("www.rijksoverheid.nl")

headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

conn.request("GET", "/documenten?trefwoord=duo&startdatum=&einddatum=&onderdeel=Ministerie%20van%20Onderwijs%2C%20Cultuur%20en%20Wetenschap&type=Alle%20documenten", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
