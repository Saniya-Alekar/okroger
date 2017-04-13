import re
fp=  open('input1.1.txt', 'r')
lines=fp.read().lower()
words=re.findall('\w+',lines)
wordcount={}
words = [w for w in words if not w.isdigit()]
for w in words:
    if len(w)==1:
        words.remove(w)
for w in words:
    if len(w)==1:
        words.remove(w)
for w in words:
    wordcount[w]=words.count(w)
new_words=re.findall(r'\bpo\w*', lines)
new_words=list(set(new_words))
print new_words
for w in new_words:
    print w,",",wordcount[w],"\n"
