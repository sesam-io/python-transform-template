from flask import Flask, request, Response
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
    app.run(debug=True, host='0.0.0.0', port=5001)

