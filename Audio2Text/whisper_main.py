from flask import Flask, request
import whisper
import numpy as np

app = Flask(__name__)
model_base = whisper.load_model("base")

'''
Flask with things
https://github.com/openai/whisper
'''


@app.route("/", methods=['POST'])
def index():
    print(request)
    fname = "audio.m4a"

    file = request.files['data'].stream

    with open(fname, 'wb') as f:  # Open and rewrite file.
        f.write(file.read())
        f.close()

    results = model_base.transcribe(fname)
    # print(results)
    print(request.method)
    return {'text': results['text']}, 200


@app.route("/v2", methods=['POST'])
def dynamic():
    print(request)

    file = request.files['data'].stream
    buff = file.read()
    np_arr = np.frombuffer(buff, dtype=np.uint8).astype(np.float32)
    np_arr = whisper.pad_or_trim(np_arr)
    res = model_base.transcribe(np_arr,
                                verbose=True,
                                language='es')
    return res, 200


@app.route("/", methods=['GET'])
def index2():
    print("time")
    return {}, 200


app.run(debug=True)
