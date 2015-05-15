content = open('output.txt').read()
content = content.split('\n\n')
content = [ line.strip('\n\n') for line in content if len(line) ]
tweets = []
for line in content:
    try:
        time,text = line.split('\n')
        d = dict(time=time,text = text)
        tweets.append(d)
    except:
        continue
