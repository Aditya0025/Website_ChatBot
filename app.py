from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# my_bot= ChatBot(name= 'PyBot', read_only = True,
# logic_adapters = [
#     'chatterbot.logic.BestMatch',
#     'chatterbot.logic.TimeLogicAdapter'
# ])

# inputs = ['hi','hai!',
# 'how do you do?',
# 'I am cool, how about you?',
# 'always cool buddy',
# 'glad to hear that',
# 'I really feel awesome',
# 'Excellent, glad to hear that',
# 'not so good',
# 'sorry to hear that',
# 'what is your name?',
# 'I am a chatbot. You can ask me a math questions',
# 'Pythagorean theorem', 'a1 squared plus b1 squared equals c1 squared',
# 'law of cosines','c1**2 = a1**2 + b1**2 - 2 * a1 * b1 * cos(gamma)'
# ]


# list_trainer = ListTrainer(my_bot)
# list_trainer.train(inputs)





# while True: 
#     request=input('you :') 

#     if request == 'OK' or request == 'ok': 

#         print('Bot: bye') 

#         break

#     else:

#         response=my_bot.get_response(request) 

#         print('Bot:', response)



# ------------- Flask Code to work on different format and convert it into Django


app = Flask(__name__)

my_bot= ChatBot(name= 'PyBot', read_only = True,
logic_adapters = [
    'chatterbot.logic.MathematicalEvaluation',
    'chatterbot.logic.BestMatch'
])


chatbot = ChatBot(name='my_bot', read_only=True,
logic_adapters=['chatterbot.logic.MathematicalEvaluation',  'chatterbot.logic.BestMatch'])


inputs = ['hi','hai!',
'how do you do?',
'I am cool, how about you?',
'always cool buddy',
'glad to hear that',
'I really feel awesome',
'Excellent, glad to hear that',
'not so good',
'sorry to hear that',
'what is your name?',
'I am a chatbot. You can ask me a math questions',
'Pythagorean theorem', 'a1 squared plus b1 squared equals c1 squared',
'law of cosines','c1**2 = a1**2 + b1**2 - 2 * a1 * b1 * cos(gamma)'
]
# math_que1 = ['Pythagorean theorem', 'a1 squared plus b1 squared equals c1 squared']
# math_que2 = ['law of cosines','c1**2 = a1**2 + b1**2 - 2 * a1 * b1 * cos(gamma)']

list_trainer = ListTrainer(my_bot)
list_trainer.train(inputs)

@app.route("/")
def home():
    return render_template('tut.html')

@app.route("/data", methods=['POST','GET'])
def get_bot_response():
    if request.method == 'POST':
        user_input = request.form['chatbox']
        print(user_input,"Here I am working for the input text for the format f the value i am looking for")
        return render_template('tut.html')



    # userText = request.form['input_text']    
    # result= chatbot.get_response(str(userText))
    # return render_template('Pop_up.html')


if __name__ == "__main__":
    app.run(debug=True)
