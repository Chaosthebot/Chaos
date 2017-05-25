#!/usr/bin/env bash
cd "$(dirname "$0")"

python -m py_compile $(find . -name '*.py');
if [ "$?" != "0" ]
then
  echo "There is syntax error. This may endanger chaos. Pauses updates."
  exit
fi

for file in startup.d/*; do
  [[ -f "$file" && -x "$file" ]] && "$file"
done
