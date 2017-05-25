#!/bin/bash

python -m py_compile $(find . -name '*.py');
if [ "$?" != "0" ]
then
  echo "There is syntax error. This may endanger chaos. Pauses updates."
  killall bash
fi
