import webapp2
from webapp2_extras import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        country = self.request.headers.get('X-AppEngine-Country')
    	region = self.request.headers.get('X-AppEngine-Region')
    	city = self.request.headers.get('X-AppEngine-City')
    	latLong = self.request.headers.get('X-AppEngine-CityLatLong')

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(
            json.encode({
                'country': country,
                'region': region,
                'city': city,
                'latLong': latLong
            }))
        
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
