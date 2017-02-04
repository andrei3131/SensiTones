echo "(use 'overtone.live)"
date=$(stat -f "%z" input.txt)
while sleep 1; do 
 date2=$(stat -f "%z" input.txt)
 if [[ $date2 != $date ]]; then 
  echo "(stop)";
  num=$(cat input.txt | grep -o -E '[0-9]+' | head -1 | sed -e 's/^0\+//')
  echo $num
  echo "(demo 7 (lpf (mix (saw [50 (line 100 1600 5) 101 100.5])) (lin-lin (lf-tri (line 2 20 5)) -1 1 400 4000)))";
  date=$(stat -f "%z" input.txt)
 fi
done
echo "(demo 7 (lpf (mix (saw [50 (line 100 1600 5) 101 100.5])) (lin-lin (lf-tri (line 2 20 5)) -1 1 400 4000)))"
echo "(demo 7 (lpf (mix (saw [50 (line 100 1600 5) 101 100.5])) (lin-lin (lf-tri (line 2 20 5)) -1 1 400 4000)))"
echo








