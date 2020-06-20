from flask import Flask, request, abort, jsonify, send_from_directory, render_template
import os
import io
from stp2json import stp2json

app = Flask(__name__)


@app.route('/files')
def list_files():
    'This endpoint is just to check whether the server saved the uploaded data on file/ or not!'
    files = []
    for filename in os.listdir('files/'):
        path = f'files/{filename}'
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stp2json')
def codes():
    return render_template('codes.html')


@app.route('/stp2json/<filename>', methods=['POST'])
def post_file(filename):
    '''Upload a file.'''
    ext = filename.split('.')[1]
    if ext not in extensions:

        abort(400, "something wrong with the uploaded data!!!")

    if '/' in filename:
        # Return 400 BAD REQUEST
        abort(400, 'no subdirectories directories allowed')

    with open(f'files/{filename}', 'wb') as fp:
        fp.write(request.data)

    try:
        stp_json = stp2json.stp2json(filePath=f'files/{filename}')
        # Delete the file after converting it to json and sending the response back
        os.remove(f'files/{filename}')
        return stp_json
    except:
        os.remove(f'files/{filename}')
        # Return 201 CREATED
        abort(400, f'something wrong with {filename} file!')

    return {}


if __name__ == '__main__':
    extensions = ['stp', 'step']
    port = int(os.environ.get('PORT', 33508))
    app.run(host='0.0.0.0', port=port, debug=True)
