from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to the Flask'

@app.route('/cal',methods=["GET"])
def math_oprerator():
    operation=request.json["operation"]
    number1=request.json["number1"]    
    number2=request.json["number2"]

    if operation=="add":
        result=int(number1)+int(number2)
    elif operation=="multi":
        result=int(number1)*int(number2)
    elif operation=="div":
        result=int(number1)/int(number2)
    else:
        result=int(number1)-int(number2)

    return "the operation is {} and the result is {}".format(operation,result)





if __name__== '__main__':

    app.run(debug=True)