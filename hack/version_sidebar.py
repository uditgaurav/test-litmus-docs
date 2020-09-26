import json
import sys

with open("version-"+sys.argv[1] +"-sidebars.json",'r') as json_file:
    data = json.load(json_file)

version="version-"+sys.argv[1] +"-"
data['version-'+sys.argv[1] +'-docs'] = data.pop('docs')
docs = data['version-'+sys.argv[1] +'-docs']

val= [] 
# update version in getting started
for values in docs['Getting Started']:
    val.append(version+values)
docs['Getting Started']=val

val= [] 
# update version in litmus demo
for values in docs['Litmus Demo']:
    val.append(version+values)
docs['Litmus Demo']=val

val= [] 
# update version in concepts
for values in docs['Concepts']:
    val.append(version+values)
docs['Concepts']=val

val= [] 
# update version in platform ids
for values in docs['Platforms']:
    for v in values['ids']:
        val.append(version+v)
        values['ids']=val
    val = []
    
val= [] 
# update version in experiment ids
for values in docs['Experiments']:
    for v in values['ids']:
        val.append(version+v)
        values['ids']=val
    val = []

val= [] 
# update version in scheduler
for values in docs['Scheduler']:
    val.append(version+values)
docs['Scheduler']=val

val= [] 
# update version in chaos workflow
for values in docs['Chaos Workflow']:
    val.append(version+values)
docs['Chaos Workflow']=val

val= [] 
# update version in litmus FAQs
for values in docs['Litmus FAQs']:
    val.append(version+values)
docs['Litmus FAQs']=val

val= [] 
# update version in litmus FAQs
for values in docs['Advanced']:
    val.append(version+values)
docs['Advanced']=val

with open("version-1.9.0-sidebars.json",'w') as json_file:
     json.dump(data,json_file,indent=2)

## Add a new version
with open("website/versions.json",'r') as json_file:
    version_data = json.load(json_file)

version_data.insert(0,sys.argv[1])

with open("website/versions.json",'w') as json_file:
     json.dump(version_data,json_file,indent=2)
