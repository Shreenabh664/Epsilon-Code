#!/bin/sh


i="0"

while [ $i -lt 1 ]
do
  printf '
    _/_/_/_/                      _/  _/                            _/_/_/                  _/
   _/        _/_/_/      _/_/_/      _/    _/_/    _/_/_/        _/          _/_/      _/_/_/    _/_/
  _/_/_/    _/    _/  _/_/      _/  _/  _/    _/  _/    _/      _/        _/    _/  _/    _/  _/_/_/_/
 _/        _/    _/      _/_/  _/  _/  _/    _/  _/    _/      _/        _/    _/  _/    _/  _/
_/_/_/_/  _/_/_/    _/_/_/    _/  _/    _/_/    _/    _/        _/_/_/    _/_/      _/_/_/    _/_/_/
         _/
        _/                                                                                               '
  printf '\n__________________________________________________'
  printf '\n\nWelcome to Epsilon-Code!\n__________________________________________________\n\nPlease select the utility that you want to use. Enter "code-gen" for generating code. Enter "debug" to get help in debugging your code. Enter "q" to exit: '
  read REPLY
  case $REPLY in
    (code-gen)        python3 $(python3 -c "import site; print(site.getsitepackages()[0])")/epsilon_code/code-gen.py || python3 $(python3 -m site --user-site)/epsilon_code/code-gen.py
        ;;
    (debug)     python3 $(python3 -c "import site; print(site.getsitepackages()[0])")/epsilon_code/debug.py || python3 $(python3 -m site --user-site)/epsilon_code/debug.py
        ;;
    (q)         break
        ;;
    (*)         echo Unknown option
        ;;
  esac
i=$[$i+1]
done

