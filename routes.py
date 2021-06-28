from flask import Flask, render_template, request, jsonify
import traceback
import hmmm

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
    return jsonify(result = [outputs, states])
  except Exception as e: 
    return jsonify(result = "Error: " + str(e))

if __name__ == "__main__":
    app.run(debug = True)

