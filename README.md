# Epsilon-Code
![Shield 1](https://img.shields.io/pypi/v/epsilon-code)
![Shield 2](https://img.shields.io/pypi/l/epsilon-code)
![Shield 3](https://img.shields.io/pypi/format/epsilon-code)
![Shield 4](https://img.shields.io/pypi/pyversions/epsilon-code)
![Shield 5](https://img.shields.io/pypi/implementation/epsilon-code)

Generate and debug Python code- with some help from AI

![Epsilon Code Logo](https://img.techpowerup.org/201013/epsilon-2.png)

For all sort of information, have a look at the [official website](https://epsilon.shreenabh.com/).

## Installation

We update our latest, most stable and best build on PyPI regularly. You can fetch the latest one simply by doing:
```bash
pip install epsilon-code
```
Note: Usage of Epsilon-Code needs an OpenAI API Key in all cases. Get yours [here](https://beta.openai.com).

To use our Python module "epcode", follow the following process:
### Generating Code
You need to use the function "getcode". Here's how to do it:
```python
from epsilon_code import epcode

epcode.getcode("Your OpenAI API Key goes here (with the quotes)", "A brief description of what you want your code to do (specify any specific methods/libraries/APIs you want the code to use)")
```
The generated code will be saved as a ```.py``` file in the current working directory. If you run the function multiple times, that file will be appended with all the code.
### Getting Debugging Help
You need to use the function "getdebug". Here's how to do it:
```python
from epsilon_code import epcode

epcode.getdebug("Your OpenAI API Key goes here (with the quotes)", "Final line of the traceback with the exact error message.")
```
The generated debugging instructions will be saved as a .txt file in the current working directory. If you run the function multiple times, that file will be appended with all the text.

### Using the command line UI

After installation is complete, you can also use our conversational command line UI to do the same. Activate it simply by doing:
```bash
epsilon.sh
```

## Directory Explanation

### epsilon.sh
The main bash file that redirects you to the appropriate ```.py``` files upon selection in the command line UI.

### code-gen.py
Takes conversational input (code-description) in a chat form and sends it via an API call to the OpenAI API (GPT-3) along with the priming data that is hackable. Receives the completion, formats it and prints it in the command line itself.

### debug.py
Takes conversational input (error message/Traceback) in a chat form and sends it via an API call to the OpenAI API (GPT-3) along with the priming data that is hackable. Receives the completion, formats it and prints it in the command line itself.

### epcode.py
The main Python module that contains the ```getcode()``` & ```getdebug()``` functions.
They are basically wrappers of the previous two files ```code-gen.py``` and ```debug.py``` respectively described in a callable function format.
