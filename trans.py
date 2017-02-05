content = ""

with open('input.txt', 'r') as content_file:
    content = content_file.read()

map = {
'C' : 0,
'D' : 1,
'E' : 2,
'F' : 3,
'G' : 4,
'A' : 5,
'B' : 6
}

#############################

spans = content.split("</span>")
words_notes = [x.split(">") for x in spans]

words = []
notes = []
for xs in words_notes:
    if len(xs) == 1:
        continue

    raw_words = xs[0]
    note = xs[1]

    ys = raw_words.split(' ')

    notes.append(note)
    cnt = 0
    for y in ys:
        if y.isalnum():
            cnt += 1

    words.append(cnt)

cnt = 0
tot = 0
durations = []
for pos in range(len(notes)):
    w = words[pos]

    tot += w
    cnt += 1
    if w != 0:
        length = tot/cnt
        for i in range(cnt):
            durations.append("1/" + str(max(length, 1) + 1))
        tot = 0
        cnt = 0

last = len(notes) - 1
while words[last] == 0:
    last -= 1

notes = [x for x in notes[0:last+1]]
notes = [str(x[0]) for x in notes]
notes = [map[x] for x in notes]

print notes
print durations

#############################

out = ""

def append_array(out, arr):
    out += '['
    for x in arr:
        out += str(x) + ' '
    out += ']'
    return out

out = append_array(out, notes)
out += '\n'
out = append_array(out, durations)

fo = open("notes.txt", "wb")
fo.write(out)
fo.close()
