 #!/bin/bash 
date=$(stat -c %y "$1")
while sleep 1; do date2=$(stat -c %y "$1")
  if [[ $date2 != $date ]]; 
  then echo "changed!"; 
  date=$(stat -c %y "$1");
  contents=$(< $1);
  value=$(echo $contents | grep -o -E '[0-9]+' | head -1 | sed -e 's/^0\+//');
  echo $value
  fi
  # possibly exit [status] instead of break
  # or if you want to watch for another change, date=$date2
done
