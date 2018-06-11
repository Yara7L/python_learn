

current_word=None
current_count=0
word=None

words="cat cat car car car map"
with open('C:/Users/admin/Desktop/123.txt','w') as f:
    wordss=words.split()
    for word in wordss:
        f.write('%s\t%s\n' % (word,1))

with open('C:/Users/admin/Desktop/123.txt','r') as f:
    for line in f:
        line = line.strip()
        word, count = line.split('\t', 1)
        try:
            count = int(count)
        except ValueError:  #count如果不是数字的话，直接忽略掉
            continue
        if current_word == word:
            current_count += count
        else:
            if current_word:
                print("%s\t%s" % (current_word, current_count))
            current_count = count
            current_word = word

    if word == current_word:
        print("%s\t%s" % (current_word, current_count))
