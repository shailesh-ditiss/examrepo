from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return "Welcome to ITIL Exam END Module "
    
@app.route("/modules", methods=["GET"])
def sh_modules():
    return "1.FCN, 2.Security Concepts, 3.COSA, 4.NDC, 5.PKI 6,ITIL & Devops, 7.Compliance Audit"
    
@app.route("/me", methods=["GET"])
def sh_details():
    return "PRN:230344223049, Name: Nilesh Sonkamble, Ph_no: 9545782708"
    
app.run(host="0.0.0.0", port=4000, debug=True)
