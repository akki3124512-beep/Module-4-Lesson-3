student_id = {'id 1' : {'name' : 'Sara', 'class' : 'V', 'subjects' : 'english, maths, science'}
              , 'id 2' : {'name' : 'Jake', 'class' : 'V', 'subjects' : 'art, maths, music'}, 
              'id 3' : {'name' : 'Sara', 'class' : 'V', 'subjects' : 'english, maths, science'}
              , 'id 4' : {'name' : 'John', 'class' : 'V', 'subjects' : 'drama, cooking, science'}}

emptylist = []
emptydict = {}

for x , y in student_id.items():
    uniqueKey = (y['name'], y['class'], y['subjects'])

    if uniqueKey not in emptylist:
        emptylist.append(uniqueKey)
        emptydict[x] = y

for k, v in emptydict.items():
    print(k, ":", v)
