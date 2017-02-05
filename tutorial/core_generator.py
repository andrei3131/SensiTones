from trans import get_notes, get_durations
import time
import subprocess
import sys

def create_clojure(name):
    notes = get_notes()
    durations = get_durations()

    buffer = ""

    str1 ="""
    (def """

    str2 = """
        (let [pitches
        """

    str3 = notes

    str4 = """
              durations
            """

    str5 = durations

    str6 = """
              times (reductions + 0 durations)]
            (map note times pitches)))
    """

    buffer += str1
    buffer += name
    buffer += str2
    buffer += str3
    buffer += str4
    buffer += str5
    buffer += str6

    return buffer

def play_song(name, type="major"):
    return create_clojure(name) + """            (->> """ + name + """
                      (where :time (bpm 90))
                      (where :pitch (comp C sharp """ + type + """))
                      play)"""

def open_close():
    with open('sentimentalert', 'r') as content_file:
        content = content_file.read()
        content_file.close()
    val = int(content)
    fo = open("sentimentalert", "wb")
    fo.write("5")
    fo.close()
    fo = open("sentimentalert", "wb")
    fo.write(str(val))
    fo.close()

# def get_sentiment():
#     open_close()
#     with open('sentimentalert', 'r') as content_file:
#         content = content_file.read()
#         content_file.close()
#     return int(content)

# def get_sentiment():
#     out = subprocess.Popen("""echo $(cat "sentimentalert" | grep -o -E '[0-9]+' | head -1 | sed -e 's/^0\+//')""",
#       shell=True,
#       stdout=subprocess.PIPE).stdout.read()
#     return out

def main():
    song_name = sys.argv[1]
    sentiment = int(sys.argv[2])

    if sentiment >= 0 and sentiment <= 30:
        print play_song(song_name, "major")
    if sentiment > 30 and sentiment <= 50:
        print play_song(song_name, "chromatic")
    if sentiment > 50 and sentiment <= 70:
        print play_song(song_name, "blues")
    if sentiment > 70 and sentiment <= 100:
        print play_song(song_name, "pentatonic")

if __name__ == "__main__":
    main()

# old_sentiment = 101
#
# while True:
#     sentiment = get_sentiment()
#     if old_sentiment != sentiment:
#         old_sentiment = sentiment
#         print "(stop)"
#         if sentiment < 30:
#             print play_song("song", "major")
#         elif sentiment < 50:
#             print play_song("song", "chromatic")
#         elif sentiment < 70:
#             print play_song("song", "blues")
#         else:
#             print play_song("song", "pentatonic")
#         time.sleep(60)
