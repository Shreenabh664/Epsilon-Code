import getpass 

print("__________________________________________________")
print("\nWelcome to Epsilon Debugger!\n__________________________________________________")

p = getpass.getpass(prompt = '\nPlease enter your OpenAI API Secret Key (Input hidden):') 

import os
import openai

os.environ['OPENAI_API_KEY'] = p
openai.api_key = os.environ["OPENAI_API_KEY"]

start_sequence = "\nA:"
restart_sequence = "\n\nQ: "

prompt="I am a highly intelligent debugger bot. I know fixes to every Python error out there. I am very friendly and I guide you how to fix your errors. Just tell me the error message you are getting and I will guide you how to fix it. Normally, I analyse your error and I tell what line/lines of code you should add/remove or what change you should make in your code. If the error is too complex for me, I will just give you some probable steps that you can employ and try to fix it. I give a step-wise guide as to what you can do to fix the bugs. If you ask me something that I don't know, I will try to look it up on https://stackoverflow.com/. If you ask me something absurd, I will simply say I don't know that and I will recommend that you ask it on Stack Overflow\n\nQ: AttributeError: 'NoneType' object has no attribute 'label'.\nA: Your constructor sets self.prevNode to None, and later you try to access node.prevNode.label, which is like trying to access None.label.  None doesn't have any attributes, so trying to access any will give you an AttributeError.You need to double check your object and the attribute name.\n\nQ: Import error: No module named Numpy\nA: Numpy is not installed in your system. You need to install numpy first. You can install it using: pip install numpy. If that does not work, try doing: pip3 install numpy.\n\nQ: IndexError: list index out of range\nA: You are trying to access a list element which does not exist. You need to check your index. \n\nQ: KeyError 'key_name'\nA: You are trying to access a key which does not exist. You need to check your key or the path to it. You could also use the dictionary's get() method as well to avoid the exceptions.\n\nQ: OverflowError: (34, 'Result too large')\nA: You are trying to store a number which is too large for the variable. You need to check your variable type and size. For higher sizes, using the 'decimal' variable type might help.\n\nQ: TypeError: unsupported operand type(s) for +: 'int' and 'str'\nA: You are trying to add a string and an integer. You need to check your operands.\n\nQ: UnboundLocalError: local variable 'a' referenced before assignment\nA: You are trying to access a variable which has not been assigned. You need to check your code and make sure that you have assigned the variable before you try to use it. If that does not work, try to pass variables as arguments to functions.\n\nQ: ValueError: could not convert string to float: 'string'\nA: You are trying to convert a string to a float. You need to check your code and make sure that you have passed the correct data type. You should be able to convert strings that look like floats to floats by just using float(mystr).\n\nQ: Shreenabh Agrawal\nA: I am not sure of that one. Please raise a new question on StackOverflow so that more people can benefit from it.\n\nQ: IndentationError: unindent does not match any outer indentation level\nA: There might be spaces mixed in with your tabs. Try doing a search & replace to replace all tabs with a few spaces.\n\nQ: IndentationError: expected an indented block\nA: Your code is not properly indented. You need to make sure that you have indented the block correctly.\n\nQ: "

print("__________________________________________________")
print("\nPlease enter the exact error message you are getting and I will help you understand it better and suggest some possible fixes for it.\n__________________________________________________\n")
text = input() 
prompt += text 

response = openai.Completion.create(
  engine="davinci",
  prompt=prompt,
  temperature=0.25,
  max_tokens=512,
  top_p=0.5,
  frequency_penalty=1,
  presence_penalty=1,
  stop=["\n\n"]
)

test_string = response['choices'][0]['text']
spl_word = 'A:'
res = test_string.partition(spl_word)[2]  
print("__________________________________________________\n")
print(res)
print("__________________________________________________")
