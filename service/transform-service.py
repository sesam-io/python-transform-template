from flask import Flask, request, Response
import cherrypy
import json
import logging
import paste.translogger


app = Flask(__name__)

logger = logging.getLogger("transform-service")


@app.route('/', methods=['GET'])
def root():
    return Response(status=200, response="I am Groot!")


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
    format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    # Log to stdout, change to or add a (Rotating)FileHandler to log to a file
    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(logging.Formatter(format_string))
    logger.addHandler(stdout_handler)

    # Comment these two lines if you don't want access request logging
    app.wsgi_app = paste.translogger.TransLogger(app.wsgi_app, logger_name=logger.name,
                                                 setup_console_handler=False)
    app.logger.addHandler(stdout_handler)

    logger.propagate = False
    logger.setLevel(logging.INFO)

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


