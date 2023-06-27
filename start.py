import http.client

conn = http.client.HTTPSConnection("www.rijksoverheid.nl")

headers = {
       }

conn.request("GET", "/documenten?trefwoord=duo&startdatum=&einddatum=&onderdeel=Ministerie%20van%20Onderwijs%2C%20Cultuur%20en%20Wetenschap&type=Alle%20documenten", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
