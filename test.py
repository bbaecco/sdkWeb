import os, logging
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename  #업로드 된 파일의 이름이 안전한지 확인

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/echo_call/<param>') #get echo api
def get_echo_call(param):
    return jsonify({"param": param})

@app.route('/container') #get container api
def get_echo_call2():
    params = request.get_json()
    #key, value 나누기
    jsonList = dict(params).items()
    for res in jsonList:
        print(res)

    return jsonify(jsonList)

@app.route('/echo_call', methods=['POST']) #post echo api
def post_echo_call():
    param = request.get_json()
    return jsonify(param)

#파일 업로드 처리
# @app.route('/fileUpload')
# def fileUpload():
#     f = request.files['file']
#     f.save('./uploads/' + secure_filename(f.filename))
#     return 'success'
#     print(f.filename)
#     # return '', 200


app.config['UPLOAD_FOLDER'] = './uploads/'

@app.route('/upload', methods=['POST'])
def Upload():
    target = os.path.join(app.config['UPLOAD_FOLDER'], 'test')
    if not os.path.isdir(target):
        os.mkdir(target)
    # logger.info("welcome to upload`")
    file = request.files['file']
    filename = secure_filename(file.filename)
    if not file:
        return "not file", 400
    destination = "/".join([target, filename])
    file.save(destination)
    # session['uploadFilePath'] = destination
    response = "success"
    return response



if __name__ == "__main__":
    app.run()