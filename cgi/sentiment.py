import subprocess

def post_request_string(str):
    """
    Makes a request to get sentiment for a single string.
    """
    
    request_script = subprocess.Popen(['ruby', 'req.rb'], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE)
    out, err = request_script.communicate()
 
    return out

print post_request_string("hi")