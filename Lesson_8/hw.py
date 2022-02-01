from pprint import pprint

s = 'Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. ' \
    'students at Stanford University in California. Together they own about 14 percent of its ' \
    'shares and control 56 percent of the stockholder voting power through supervoting stock. ' \
    'They incorporated Google as a California privately held company on September 4, 1998, ' \
    'in California. Google was then reincorporated in Delaware on October 22, 2002.[13] An initial ' \
    'public offering (IPO) took place on August 19, 2004, and Google moved to its headquarters in ' \
    'Mountain View, California, nicknamed the Googleplex. In August 2015, Google announced plans to ' \
    'reorganize its various interests as a conglomerate called Alphabet Inc. Google is Alphabet\'s ' \
    'leading subsidiary and will continue to be the umbrella company for Alphabet\'s Internet interests. ' \
    'Sundar Pichai was appointed CEO of Google, replacing Larry Page who became the CEO of Alphabet.'

d = {}
lst = s.split()

for word in lst:
    d[word] = d.get(word, 0) + 1

pprint(d)

maximu = max(d.values())
word = ''
for key, values in d.items():
    if values == maximu:
        word = key

print(word, d[word])
