import httplib, urllib, base64

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '7911c204a38749acba19d26e6bb2e763',
}

params = urllib.urlencode('{\
  "documents": [\
    {\
      "language": "string",\
      "id": "string",\
      "text": "string"\
    }\
  ]\
}')

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
