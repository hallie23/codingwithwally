from flask import Flask, render_template, request, jsonify
import traceback
import hmmm
import json

app = Flask(__name__)

@app.route('/', methods = ["POST", "GET"])
def index():
    return render_template('writeCode.html')

@app.route('/background_process_writeHMMM')
def background_process_writeHMMM():
  code = request.args.get('code')
  inputs = request.args.get('inputs')
  try:
    print('hi')
    outputs, states = hmmm.main(code, inputs)
    print("outputs: ")
    print(outputs)
    if states == None:
      return jsonify(result = outputs)
    print(states)
    return jsonify(result = [outputs, states[-1]])
  except Exception as e: 
    return jsonify(result = "Error: " + str(e))

@app.route('/background_process_HMMMstep')
def background_process_HMMMstep():
  code = request.args.get('code')
  state = json.loads(request.args.get('state'))
  input = request.args.get('input')
  try:
    print('state', state)
    if len(state[3]) != 0:
      state[3] = {int(k):v for (k,v) in state[3].items()}
    outputs, states = hmmm.main(code, input, state)
    print('outputs', outputs)
    print('states', states)
    if states == None:
      return jsonify(result = outputs)
    return jsonify(result = [outputs, states[-1]])
  except Exception as e: 
    return jsonify(result = "Error: " + str(e))

if __name__ == "__main__":
    app.run(debug = True)

