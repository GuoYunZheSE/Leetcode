def strip_punctuation(x):
    for i in punctuation_chars:
        x=x.replace(i,"")
    return x
def get_pos(x):
    x=x.lower()
    x=strip_punctuation(x)
    x=x.split(" ")
    ct = 0
    for i in x:
        if i in positive_words:
            ct+=1
    return ct
def get_neg(x):
    x=x.lower()
    x=strip_punctuation(x)
    x=x.split(" ")
    ct = 0
    for i in x:
        if i in negative_words:
            ct+=1
    return ct

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

resulting_f=open("resulting_data.csv",'w')
resulting_f.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")

with open("project_twitter_data.csv","r") as data_f:
    data_f.readline()
    for line in data_f.readlines():
        tweet,retweet_count,reply_count=line.split(',')
        pos_score=get_pos(tweet)
        neg_score=get_neg(tweet)
        net_score=pos_score+neg_score
        resulting_f.write("{},{},{},{},{}\n".format(retweet_count,reply_count,pos_score,neg_score,net_score))
resulting_f.close()
s=0
a=0
for i in range(1,1001):
    for j in range(1,i):
        if i%j==0:
            s=s+j
    if s==i:
        a=a+1
        s=0
    else:
        s=0
print(a)
