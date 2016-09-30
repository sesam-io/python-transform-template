=========================
python-transform-template
=========================

A python micro service template for transforming a JSON entity stream. This service is designed to be used with the `HTTP transform <https://docs.sesam.io/configuration.html#the-http-transform>`_ in a Sesam service instance. 

::

  $ python3 service/transform-service.py
   * Running on http://0.0.0.0:5001/ (Press CTRL+C to quit)
   * Restarting with stat
   * Debugger is active!
   * Debugger pin code: 260-787-156

The service listens on port 5001.

JSON entities can be posted to 'http://localhost:5001/transform'. The result is streamed back to the client.


Example:

::

   $ curl -s -XPOST 'http://localhost:5001/transform' -H "Content-type: application/json" -d '[{ "_id": "jane", "name": "Jane Doe" }]' | jq -S .
   [
     {
       "_id": "jane",
       "message": "Hello world!",
       "name": "Jane Doe"
     }
   ]

Note the example uses `curl <https://curl.haxx.se/>`_ to send the request and `jq <https://stedolan.github.io/jq/>`_ prettify the response.
