import http.client

conn = http.client.HTTPSConnection("www.rijksoverheid.nl")

headers = {
    'cookie': "_pk_id.4.e7da=740478e2e16cd1c5.1665567680.9.1666344548.1666344198.; stg_returning_visitor=Fri%252C%252028%2520Oct%25202022%252009%3A32%3A54%2520GMT; stg_traffic_source_priority=4; _pk_ses.bf9c05f0-c13f-4e22-80c7-e603d39fc616.e7da=*; stg_externalReferrer=; _pk_id.bf9c05f0-c13f-4e22-80c7-e603d39fc616.e7da=b2effe964d484016.1666949573.28.1687857971.1687856915.; stg_last_interaction=Tue%252C%252027%2520Jun%25202023%252009%3A26%3A28%2520GMT",
    'authority': "www.rijksoverheid.nl",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
    'cache-control': "max-age=0",
    'sec-ch-ua': ""Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': ""macOS"",
    'sec-fetch-dest': "document",
    'sec-fetch-mode': "navigate",
    'sec-fetch-site': "none",
    'sec-fetch-user': "?1",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

conn.request("GET", "/documenten?trefwoord=duo&startdatum=&einddatum=&onderdeel=Ministerie%20van%20Onderwijs%2C%20Cultuur%20en%20Wetenschap&type=Alle%20documenten", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
