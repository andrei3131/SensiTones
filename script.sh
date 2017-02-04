echo "(use 'overtone.live)"
m1=$(md5sum "$sentimentalert")
while sleep 1; do 
 m2=$(md5sum "$sentimentalert")
 if [[ $m2 != $m1 ]]; then 
  echo "(stop)";
  num=$(cat "$sentimentalert" | grep -o -E '[0-9]+' | head -1 | sed -e 's/^0\+//')
  echo $num
  echo "(demo 7 (lpf (mix (saw [50 (line 100 1600 5) 101 100.5])) (lin-lin (lf-tri (line 2 20 5)) -1 1 400 4000)))";
  m1=$(md5sum "$sentimentalert")
 fi
done
echo "(demo 7 (lpf (mix (saw [50 (line 100 1600 5) 101 100.5])) (lin-lin (lf-tri (line 2 20 5)) -1 1 400 4000)))"
echo "(demo 7 (lpf (mix (saw [50 (line 100 1600 5) 101 100.5])) (lin-lin (lf-tri (line 2 20 5)) -1 1 400 4000)))"
echo








