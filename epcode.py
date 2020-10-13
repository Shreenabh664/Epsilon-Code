import os
import openai

def getcode(secretKey, codeDescription):

  os.environ['OPENAI_API_KEY'] = secretKey
  openai.api_key = os.environ["OPENAI_API_KEY"]

  start_sequence = "\nA:"
  restart_sequence = "\n\nQ: "

  prompt="I am a highly intelligent Python Bot and I can give you a simple code snippet in Python for your task. My code is \"properly indented\". I print only \"one line of code per line\". I \"don't use comments\". I \"import all libraries\" every time. I never use comments in the code. I never use \"#\" in my code.\n\nQ: Ask user for a number between 1 and 24th prime number. Test if it is a Fibonacci number.\nA: \nprint(\"Enter a number between 1 and 89: \")\nn = int(input())\nif n in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]:\n    print(\"You entered: \", n)\nelse:\n    print(\"That is not a Fibonacci number.\")\n#Generated with Epsilon-Code\n\nQ: calculate the sine value of number stored in \"num\".\nA: \nimport math\nprint(\"Enter a number: \")\nnum = int(input())\nsin_value = math.sin(num) \nprint(\"The sine of your number is: \", sin_value, \".\") \n#Generated with Epsilon-Code\n\nQ: Print the top and bottom rows of the data frame\nA: \nimport pandas as pd\nimport numpy as np\ndf = pd.DataFrame(np.random.randint(1, 10, size=(5, 4)), columns=['a', 'b', 'c', 'd']) \nprint(\"The top row and bottom rows are:\n\", df.iloc[[0, -1]])\n#Generated with Epsilon-Code\n\nQ: make a decision tree classifier on the IRIS dataset.\nA:\nfrom sklearn import datasets\nfrom sklearn import metrics\nfrom sklearn.tree import DecisionTreeClassifier\ndataset = datasets.load_iris()\nmodel = DecisionTreeClassifier()\nmodel.fit(dataset.data, dataset.target)\nprint(model)\nexpected = dataset.target\npredicted = model.predict(dataset.data)\nprint(metrics.classification_report(expected, predicted))\n#Generated with Epsilon-Code\n\nQ: delete all vowels from input text.\nA:\nimport re\nprint(\"Enter some text (all vowels in it will be removed): \")\ntext = input() \nregexp = r'[aeiouAEIOU]'\nprint(re.sub('\b'.join(regexp), '', text))\n#Generated with Epsilon-Code\n\nQ: plot sin x\nA:\nimport matplotlib.pyplot as plt\nimport numpy as np\nx = np.linspace(-10, 10, 100)\ny = np.sin(x) \nplt.plot(x, y) \nplt.show()\n#Generated with Epsilon-Code\n\nQ: ask user to enter 3 numbers one by one. print the product.\nA:\nprint(\"Enter three numbers one by one: \")\nn1 = int(input()) \nn2 = int(input()) \nn3 = int(input()) \nproduct_number = n1 * n2 * n3\nprint(\"The product of your three numbers is: \", product_number, \".\")\n#Generated with Epsilon-Code\n\nQ: perform a google search of what the user wants and print the top result.\nA:\nimport requests\nfrom bs4 import BeautifulSoup\nsearch_url = \"https://www.google.com/search?q=\" + input() \nr = requests.get(search_url)\nhtml = r.text \nsoup = BeautifulSoup(html, 'lxml') \nprint(soup)\n#Generated with Epsilon-Code\n\nQ: Print what part of the day is going on right now.\nA:\nimport time\nmytime = time.localtime()\nif mytime.tm_hour < 6 or mytime.tm_hour > 18:\n    print ('It is night-time')\nelse:\n    print ('It is day-time')\n#Generated with Epsilon-Code\n\nQ: make a password generator\nA:\nimport random\ncharacters = 'abcdefghijklmnopqrstuvwxyz[];\',./{}:\"<>?\\|12345678980!@#$%^&*()-=_+~`'\ncharacters = list(characters)\npassword = ''\nfor i in range(0, random.randint(8, 13)):\n    char = random.choice(characters)\n    password+=char\nprint('Your password is:', password)\n#Generated with Epsilon-Code\n\nQ: delete first line of multi-line string. \nA:\nimport re\ntext = input() \nregexp = r'^\s*(.*)$'\nprint(re.sub('\b'.join(regexp), '', text))\n#Generated with Epsilon-Code\n\nQ: check if the year entered by user is a leap year\nA:\nimport datetime\nyear = int(input())\nif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): \n    print(\"It is a leap year\")\nelse:\n    print(\"It is not a leap year\")\n#Generated with Epsilon-Code\n\nQ: calculate factorial of number given by user\nA:\nimport math\nprint(\"Enter a number: \")\nnum = int(input())\nfactorial_number = 1 \nfor i in range(1, num + 1): \n    factorial_number *= i \nprint(factorial_number)\n#Generated with Epsilon-Code\n\nQ: "
  
  prompt += codeDescription 

  response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    temperature=0.1,
    max_tokens=512,
    top_p=0.5,
    frequency_penalty=1,
    presence_penalty=1,
    stop=["\n\n"]
  )

  test_string = response['choices'][0]['text']
  spl_word = 'A:'
  res = test_string.partition(spl_word)[2]  

  outF = open("EpsilonCodeOutput.py", "a")
  outF.writelines(res)
  outF.close()

def getdebug(secretKey, mainError):

  os.environ['OPENAI_API_KEY'] = secretKey
  openai.api_key = os.environ["OPENAI_API_KEY"]

  start_sequence = "\nA:"
  restart_sequence = "\n\nQ: "

  prompt="I am a highly intelligent debugger bot. I know fixes to every Python error out there. I am very friendly and I guide you how to fix your errors. Just tell me the error message you are getting and I will guide you how to fix it. Normally, I analyse your error and I tell what line/lines of code you should add/remove or what change you should make in your code. If the error is too complex for me, I will just give you some probable steps that you can employ and try to fix it. I give a step-wise guide as to what you can do to fix the bugs. If you ask me something that I don't know, I will try to look it up on https://stackoverflow.com/. If you ask me something absurd, I will simply say I don't know that and I will recommend that you ask it on Stack Overflow\n\nQ: AttributeError: 'NoneType' object has no attribute 'label'.\nA: Your constructor sets self.prevNode to None, and later you try to access node.prevNode.label, which is like trying to access None.label.  None doesn't have any attributes, so trying to access any will give you an AttributeError.You need to double check your object and the attribute name.\n\nQ: Import error: No module named Numpy\nA: Numpy is not installed in your system. You need to install numpy first. You can install it using: pip install numpy. If that does not work, try doing: pip3 install numpy.\n\nQ: IndexError: list index out of range\nA: You are trying to access a list element which does not exist. You need to check your index. \n\nQ: KeyError 'key_name'\nA: You are trying to access a key which does not exist. You need to check your key or the path to it. You could also use the dictionary's get() method as well to avoid the exceptions.\n\nQ: OverflowError: (34, 'Result too large')\nA: You are trying to store a number which is too large for the variable. You need to check your variable type and size. For higher sizes, using the 'decimal' variable type might help.\n\nQ: TypeError: unsupported operand type(s) for +: 'int' and 'str'\nA: You are trying to add a string and an integer. You need to check your operands.\n\nQ: UnboundLocalError: local variable 'a' referenced before assignment\nA: You are trying to access a variable which has not been assigned. You need to check your code and make sure that you have assigned the variable before you try to use it. If that does not work, try to pass variables as arguments to functions.\n\nQ: ValueError: could not convert string to float: 'string'\nA: You are trying to convert a string to a float. You need to check your code and make sure that you have passed the correct data type. You should be able to convert strings that look like floats to floats by just using float(mystr).\n\nQ: Shreenabh Agrawal\nA: I am not sure of that one. Please raise a new question on StackOverflow so that more people can benefit from it.\n\nQ: IndentationError: unindent does not match any outer indentation level\nA: There might be spaces mixed in with your tabs. Try doing a search & replace to replace all tabs with a few spaces.\n\nQ: IndentationError: expected an indented block\nA: Your code is not properly indented. You need to make sure that you have indented the block correctly.\n\nQ: "
  prompt += mainError 

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

  outF = open("EpsilonCodeErrorLogs.txt", "a")
  outF.writelines(res)
  outF.close()
