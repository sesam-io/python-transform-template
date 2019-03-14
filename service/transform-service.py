from flask import Flask, request, Response
import cherrypy
import json
import os

app = Flask(__name__)


@app.route('/transform', methods=['POST'])
def receiver():

    def generate(entities):
        # insert {"message": "Hello world!"} into each entity
        yield "["
        for index, entity in enumerate(entities):
            if index > 0:
                yield ","
            entity["message"] = "Hello world!"
            yield json.dumps(entity)
        yield "]"

    # get entities from request
    entities = request.get_json()

    # create the response
    return Response(generate(entities), mimetype='application/json')


if __name__ == '__main__':
    cherrypy.tree.graft(app, '/')

    # Set the configuration of the web server to production mode
    cherrypy.config.update({
        'environment': 'production',
        'engine.autoreload_on': False,
        'log.screen': True,
        'server.socket_port': 5001,
        'server.socket_host': '0.0.0.0'
    })

    # Start the CherryPy WSGI web server
    cherrypy.engine.start()
    cherrypy.engine.block()


