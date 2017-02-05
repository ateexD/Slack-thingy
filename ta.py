from pprint import pprint
from slacker import Slacker

name='somebot'

#ID Of somebot
#slack=Slacker('xoxb-127663738195-Le4BIufQzqADh6eC2pKIdVEJ')

#Test ID of AcceleroTeam
#slack=Slacker('xoxp-109406689664-110788867926-127737250370-d01039ce30fad5d82e8aaeb8ff4580f0')
#Test ID of SF
slack=Slacker('xoxp-111399271671-111408077911-128780231495-a35ef316f291cea3401b6909a06438c0')
a=list()
flag=0
ch_name="botbot"
ch_id=slack.channels.get_channel_id(ch_name)
s=slack.channels.history(channel=ch_id)
for e in s.body.items()[1]:
    for x in e:
        if type(x)==type(dict()):
            if "attachments" in x:
                d=dict(x["attachments"][0])
                #pprint(d)
                if (unicode("title") in d and "Availabilit" in d["title"]):
                    votes=x["attachments"][0]["fields"]
                    for v in votes:
                        a.append(v["value"])
                    break


b={}
co=0
for x in a:
    co+=1
    t=x.split("\n")
    b[co]=t[1]
#pprint(b)

for k in b:
    b[k]=[x for x in b[k].strip().split(",")]
    for i in xrange(len(b[k])):
        b[k][i]=str(b[k][i].strip())
pprint(b)
ta=dict()
for k in b:
    for x in b[k]:
        if x not in ta:
            ta[x]=1
        else:
            ta[x]+=1
print ta
sxb=[]
for k in ta:
    sxb.append([k,ta[k]])
sxb= (sxb[::-1])
sxb=sorted(sxb,key=lambda x:x[1])

name=[]
for x in sxb:
    if x[0]!='' and x[1]<=2:
        name.append(x[0])
print name
d={1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
for k in b:
    for e in b[k]:
        if e in name:
            d[k].append(e)
pprint (d)


'''
slack.chat.post_message("#nightout","Results of the Latest Poll")
#slack.chat.post_message("#general","Results")
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for k in b.keys():
    if not b[k]:
        pass
        slack.chat.post_message("#nightout",days[k-1]+" : No TA hours")
        #slack.chat.post_message("#general",days[k-1]+" : No TA hours")
    else:
        l=b[k].split(",")
        #slack.chat.post_message("#general",days[k-1]+" : 6 PM to 8 PM")

        if(len(l)<=1):
            pass
            slack.chat.post_message("#nightout", days[k-1]+" : "+"<@"+slack.users.get_user_id(str(b[k]))+">")
        if(len(l)>=2):
            text=""
            for i in xrange(len(l)):
                if(i>=2):
                    break
                text+="<@"+slack.users.get_user_id(str(l[i]).strip())+ ">" + ","

            slack.chat.post_message("#nightout", days[k-1]+" : "+text)
'''