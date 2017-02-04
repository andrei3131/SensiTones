import subprocess

def post_request_string(str):
    """
    Makes a request to get sentiment for a single string.
    """

    fo = open("reqbuffer.txt", "wb")
    fo.write(str)
    fo.close()    
    
    request_script = subprocess.Popen(['ruby', 'req.rb'], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE)
    out, err = request_script.communicate()

    return out

{"documents":[{"score":0.981552,"id":"ruby_req"}],"errors":[]}

def post_request(str):
    #resp = str
    resp = post_request_string(str)

    start = 0
    pos = 0
    for chr in resp:
        if start != 0:
            break
        if chr >= '0' and chr <= '9':
            start = pos 
        pos += 1

    ln = len(resp)
    pos = start
    out = ""
    while (resp[pos] == '.' or (resp[pos] >= '0' and resp[pos] <= '9')):
        out += resp[pos]
        pos += 1
        if pos == ln:
            break

    return float(out)

