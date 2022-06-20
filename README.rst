=========================
python-transform-template
=========================

A python microservice template for transforming a JSON entity stream. This service is designed to be used with the `HTTP transform <https://docs.sesam.io/configuration.html#the-http-transform>`_ in a Sesam service instance.

::

  $ python3 service/transform-service.py
  [14/Mar/2019:10:32:40] ENGINE Bus STARTING
  [14/Mar/2019:10:32:40] ENGINE Started monitor thread '_TimeoutMonitor'.
  [14/Mar/2019:10:32:40] ENGINE Serving on http://0.0.0.0:5001
  [14/Mar/2019:10:32:40] ENGINE Bus STARTED

The service listens on port 5001. The port number can be changed by passing in the PORT environment variable.

JSON entities can be posted to 'http://localhost:5001/transform'. The result is streamed back to the client.


Examples:

::

   $ curl -s -XPOST 'http://localhost:5001/transform' -H "Content-type: application/json" -d '[{ "_id": "jane", "name": "Jane Doe" }]' | jq -S .
   [
     {
       "_id": "jane",
       "message": "Hello world!",
       "name": "Jane Doe"
     }
   ]

::

   $ curl -s -XPOST 'http://localhost:5001/transform' -H "Content-type: application/json" -d @sample.json |jq -S .
   [
     {
       "_id": "jane",
       "message": "Hello world!",
       "name": "Jane Doe"
     },
     {
       "_id": "john",
       "message": "Hello world!",
       "name": "John Smith"
     }
   ]

Note the example uses `curl <https://curl.haxx.se/>`_ to send the request and `jq <https://stedolan.github.io/jq/>`_ prettify the response.
