import json
import re
data = []
with open('AI2-8thGr-NDMC-Feb2016-Train.jsonl') as f:
    for line in f:
        question=json.loads(line)
        q_dict={}
        temp_str=question['question']['stem'].encode('utf-8').strip()
        q_dict['Q']=re.sub("[^\w]", " ",  temp_str).split()
        q_dict['Q'] = stopWordRemoval(q_dict['Q'])
        for opt in question['question']['choices']:
            temp_str=opt['text'].encode('utf-8').strip()
            q_dict[opt['label'].encode('utf-8').strip()]=re.sub("[^\w]", " ",  temp_str).split()
        data.append(q_dict)
