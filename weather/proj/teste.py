import requests

url = 'http://geonode.terravisiongeo.com.br/geoserver/geonode/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:poligonorolamoca&maxFeatures=50&outputFormat=application/json'
r = requests.get(url)
print r.json()

