from flask import Flask, render_template, request, jsonify
import traceback
import pcode
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
    outputs, registers = hmmm.main(code, inputs)
    print(registers)
    return jsonify(result = [outputs, registers])
  except Exception as e: 
    return jsonify(result = "Error: " + str(e))


@app.route('/background_process_testInputs')
def background_process_testInputs():
  input = eval(request.args.get('input'))
  ans = pcode.correctFunc(input)
  return jsonify(result = "The answer is " + str(ans))

@app.route('/background_process_testOutputs')
def background_process_testOutputs():
  output = eval(request.args.get('output'))
  ans = pcode.correctFunc(output)
  if ans == 9:
    return jsonify(result = "Correct, an input of " + str(output) + " works")
  else:
    return jsonify(result = "Incorrect, an input of {} gives you an output of {}".format(str(output), ans) )


@app.route('/change_type', methods = ["POST", "GET"])
def change_type():
  if request.method == "POST":
    newView = request.form.to_dict()['hiddenSelect']
    if newView == "test inputs":
      return render_template('testInputs.html')
    elif newView == "write code":
      return render_template("writeCode.html")
    elif newView == "test outputs":
      return render_template("testOutputs.html")
    else:
      return render_template("writeCode.html")

if __name__ == "__main__":
    app.run(debug = True)

