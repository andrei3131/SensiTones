import sentiment as sen

print "(stop)"

sentiment = sen.post_request('Hello')
if sentiment > 0.5:
        print "(demo (sin-osc))"
