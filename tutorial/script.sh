echo "(use 'overtone.live)"
m1=$(md5sum "sentimentalert")
cnt=0
while sleep 1; do
 m2=$(md5sum "sentimentalert")
 if [[ $m2 != $m1 ]]; then
  cnt=$((cnt + 1))
  echo "(stop)";
  num=$(cat "sentimentalert" | grep -o -E '[0-9]+' | head -1 | sed -e 's/^0\+//')
  song_name="mysong"
  song_name+=$cnt
  python core_generator.py $song_name $num
  m1=$(md5sum "sentimentalert")
 fi
done
