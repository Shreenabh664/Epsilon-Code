import getpass 

print("__________________________________________________")
print("\nWelcome to Epsilon Code-Gen!\n__________________________________________________")

p = getpass.getpass(prompt = '\nPlease enter your OpenAI API Secret Key (Input hidden):') 

import os
import openai

os.environ['OPENAI_API_KEY'] = p
openai.api_key = os.environ["OPENAI_API_KEY"]

start_sequence = "\nA:"
restart_sequence = "\n\nQ: "

prompt="I am a highly intelligent Python Bot and I can give you a simple code snippet in Python for your task. My code is \"properly indented\". I print only \"one line of code per line\". I \"don't use comments\". I \"import all libraries\" every time. I never use comments in the code. I never use \"#\" in my code.\n\nQ: Ask user for a number between 1 and 24th prime number. Test if it is a Fibonacci number.\nA: \nprint(\"Enter a number between 1 and 89: \")\nn = int(input())\nif n in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]:\n    print(\"You entered: \", n)\nelse:\n    print(\"That is not a Fibonacci number.\")\n#Generated with Epsilon-Code\n\nQ: calculate the sine value of number stored in \"num\".\nA: \nimport math\nprint(\"Enter a number: \")\nnum = int(input())\nsin_value = math.sin(num) \nprint(\"The sine of your number is: \", sin_value, \".\") \n#Generated with Epsilon-Code\n\nQ: Print the top and bottom rows of the data frame\nA: \nimport pandas as pd\nimport numpy as np\ndf = pd.DataFrame(np.random.randint(1, 10, size=(5, 4)), columns=['a', 'b', 'c', 'd']) \nprint(\"The top row and bottom rows are:\n\", df.iloc[[0, -1]])\n#Generated with Epsilon-Code\n\nQ: make a decision tree classifier on the IRIS dataset.\nA:\nfrom sklearn import datasets\nfrom sklearn import metrics\nfrom sklearn.tree import DecisionTreeClassifier\ndataset = datasets.load_iris()\nmodel = DecisionTreeClassifier()\nmodel.fit(dataset.data, dataset.target)\nprint(model)\nexpected = dataset.target\npredicted = model.predict(dataset.data)\nprint(metrics.classification_report(expected, predicted))\n#Generated with Epsilon-Code\n\nQ: delete all vowels from input text.\nA:\nimport re\nprint(\"Enter some text (all vowels in it will be removed): \")\ntext = input() \nregexp = r'[aeiouAEIOU]'\nprint(re.sub('\b'.join(regexp), '', text))\n#Generated with Epsilon-Code\n\nQ: plot sin x\nA:\nimport matplotlib.pyplot as plt\nimport numpy as np\nx = np.linspace(-10, 10, 100)\ny = np.sin(x) \nplt.plot(x, y) \nplt.show()\n#Generated with Epsilon-Code\n\nQ: ask user to enter 3 numbers one by one. print the product.\nA:\nprint(\"Enter three numbers one by one: \")\nn1 = int(input()) \nn2 = int(input()) \nn3 = int(input()) \nproduct_number = n1 * n2 * n3\nprint(\"The product of your three numbers is: \", product_number, \".\")\n#Generated with Epsilon-Code\n\nQ: perform a google search of what the user wants and print the top result.\nA:\nimport requests\nfrom bs4 import BeautifulSoup\nsearch_url = \"https://www.google.com/search?q=\" + input() \nr = requests.get(search_url)\nhtml = r.text \nsoup = BeautifulSoup(html, 'lxml') \nprint(soup)\n#Generated with Epsilon-Code\n\nQ: Print what part of the day is going on right now.\nA:\nimport time\nmytime = time.localtime()\nif mytime.tm_hour < 6 or mytime.tm_hour > 18:\n    print ('It is night-time')\nelse:\n    print ('It is day-time')\n#Generated with Epsilon-Code\n\nQ: make a password generator\nA:\nimport random\ncharacters = 'abcdefghijklmnopqrstuvwxyz[];\',./{}:\"<>?\\|12345678980!@#$%^&*()-=_+~`'\ncharacters = list(characters)\npassword = ''\nfor i in range(0, random.randint(8, 13)):\n    char = random.choice(characters)\n    password+=char\nprint('Your password is:', password)\n#Generated with Epsilon-Code\n\nQ: delete first line of multi-line string. \nA:\nimport re\ntext = input() \nregexp = r'^\s*(.*)$'\nprint(re.sub('\b'.join(regexp), '', text))\n#Generated with Epsilon-Code\n\nQ: check if the year entered by user is a leap year\nA:\nimport datetime\nyear = int(input())\nif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): \n    print(\"It is a leap year\")\nelse:\n    print(\"It is not a leap year\")\n#Generated with Epsilon-Code\n\nQ: calculate factorial of number given by user\nA:\nimport math\nprint(\"Enter a number: \")\nnum = int(input())\nfactorial_number = 1 \nfor i in range(1, num + 1): \n    factorial_number *= i \nprint(factorial_number)\n#Generated with Epsilon-Code\n\nQ: "


print("__________________________________________________")
print("\nEnter a brief description of what code you want to generate.\n(Please specify a step-by-step guide to how the code should work.\nSpecify any specific libraries/methods that you want the code to use):\n__________________________________________________\n")
text = input() 
prompt += text 

response = openai.Completion.create(
  engine="davinci",
  prompt=prompt,
  temperature=0.1,
  max_tokens=512,
  top_p=0.5,
  frequency_penalty=1,
  #logit_bias = {'#': -1},
  presence_penalty=1,
  stop=["\n\n"]
)

test_string = response['choices'][0]['text']
spl_word = 'A:'
res = test_string.partition(spl_word)[2]  
print("__________________________________________________")
print(res)
print("__________________________________________________")
