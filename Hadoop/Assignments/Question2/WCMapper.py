#!/usr/bin/env python
import sys,string
STOPWORDS={'a','about','above','after','again','against','all','also','am','an','and','any','are',"aren't",'as','at','b','be','because','been','before','being','below',
 'between','both','but','by','c','can',"can't",'cannot','com','could',"couldn't",'d','did',"didn't",'do','does',"doesn't",'doing',"don't",'down','during','e','each','else','ever','f','few','for','from','further','g','get','h','had',"hadn't",'has',"hasn't",'have',"haven't",'having','he',"he'd","he'll","he's",'her','here',"here's",'hers','herself','him','himself','his','how',"how's",'however','http','i',"i'd","i'll","i'm","i've",'if','in','into','is',"isn't",'it',"it's",'its','itself','j','just','k',"let's",'l','like','m','me','more','most',"mustn't",'my','myself','n','no','nor','not','o','of','off','on','once','only','or','other','otherwise','ought','our','ours','ourselves','out','over','own','p','q','r','s','t','same','shall',"shan't",'she',"she'd","she'll","she's",'should',"shouldn't",'since','so','some','such','than','that',"that's",'the','their','theirs','them','themselves','then','there',"there's",'these','they',"they'd","they'll","they're","they've",'this','those','through','to','too','u','under','until','up','very','v','w','was',"wasn't",'we',"we'd","we'll","we're","we've",'were',"weren't",'what',"what's",'when',"when's",'where',"where's",'which','while','who',"who's",'whom','why',"why's",'with',"won't",'would',"wouldn't",'www','x','y','z','you',"you'd","you'll","you're","you've",'your','yours','yourself','yourselves'}
for line in sys.stdin:
    line=line.strip()
    words=[x.lower().strip(string.punctuation) for x in line.split()]
    words=[x for x in words if x.isalpha() and x not in STOPWORDS]
    for word in words:
        print(word+',1')
