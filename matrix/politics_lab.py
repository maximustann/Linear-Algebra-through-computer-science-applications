# version code d357d7b38bcc+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# Be sure that the file voting_record_dump109.txt is in the matrix/ directory.





## 1: (Task 1) Create Voting Dict
def create_voting_dict(strlist):
    """
    Input: a list of strings.  Each string represents the voting record of a senator.
           The string consists of 
              - the senator's last name, 
              - a letter indicating the senator's party,
              - a couple of letters indicating the senator's home state, and
              - a sequence of numbers (0's, 1's, and negative 1's) indicating the senator's
                votes on bills
              all separated by spaces.
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting record.
    Example: 
        >>> vd = create_voting_dict(['Kennedy D MA -1 -1 1 1', 'Snowe R ME 1 1 1 1'])
        >>> vd == {'Snowe': [1, 1, 1, 1], 'Kennedy': [-1, -1, 1, 1]}
        True

    You can use the .split() method to split each string in the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.

    You can use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    The lists for each senator should preserve the order listed in voting data.
    In case you're feeling clever, this can be done in one line.
    """
    result = {}
    for string in strlist:
        temp = string.split()[0]
        result[temp] = []
        for i, word in enumerate(string.split()):
            if i > 2:
                result[temp].append(int(word))
    return result



## 2: (Task 2) Policy Compare
def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    
    The code should correct compute dot-product even if the numbers are not all in {0,1,-1}.
        >>> policy_compare('A', 'B', {'A':[100,10,1], 'B':[2,5,3]})
        253
        
    You should definitely try to write this in one line.
    """
    result = 0
    for i in range(len(voting_dict[sen_a])):
        result = result + voting_dict[sen_a][i] * voting_dict[sen_b][i]
    return result



## 3: (Task 3) Most Similar
def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    privous = None
    name = None
    for i, s in enumerate(voting_dict.keys()):
        current = None
        new_dict = {sen:voting_dict[sen], s:voting_dict[s]}
        if s != sen:
            if privous == None:
                name = s
                privous = policy_compare(sen, s, new_dict)
            current = policy_compare(sen, s, new_dict)
            if current > privous:
                privous = current
                name = s
    return name


## 4: (Task 4) Least Similar
def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        >>> least_similar('a', vd)
        'c'
    """
    privous = None
    name = None
    for i, s in enumerate(voting_dict.keys()):
        current = None
        new_dict = {sen:voting_dict[sen], s:voting_dict[s]}
        if s != sen:
            if not privous:
                privous = policy_compare(sen, s, new_dict)
                name = s
            current = policy_compare(sen, s, new_dict)
            if current < privous:
                privous = current
                name = s
    return name

## 5: (Task 5) Chafee, Santorum
most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold' 



## 6: (Task 6) Most Average Democrat
def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        >>> sens = {'Fox-Epstein','Ravella','Oyakawa','Loery'}
        >>> find_average_similarity('Klein', sens, vd)
        -0.5
        >>> sens == {'Fox-Epstein','Ravella', 'Oyakawa', 'Loery'}
        True
        >>> vd == {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        True
    """
    result = 0
    for s in sen_set:
        if sen != s:
            new_dict = {sen:voting_dict[sen], s:voting_dict[s]}
            result = result + policy_compare(sen, s, new_dict)
    return result / (len(voting_dict) - 1)

most_average_Democrat = "Biden" # give the last name (or code that computes the last name)



## 7: (Task 7) Average Record
def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> senators = {'Fox-Epstein','Ravella'}
        >>> find_average_record(senators, voting_dict)
        [-0.5, -0.5, 0.0]
        >>> voting_dict == {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        True
        >>> senators
        {'Fox-Epstein','Ravella'}
        >>> d = {'c': [-1,-1,0], 'b': [0,1,1], 'a': [0,1,1], 'e': [-1,-1,1], 'd': [-1,1,1]}
        >>> find_average_record({'a','c','e'}, d)
        [-0.6666666666666666, -0.3333333333333333, 0.6666666666666666]
        >>> find_average_record({'a','c','e','b'}, d)
        [-0.5, 0.0, 0.75]
        >>> find_average_record({'a'}, d)
        [0.0, 1.0, 1.0]
    """
    result = [0 for x in range(len(list(voting_dict.values())[0]))]
    for sen_name in sen_set:
        for i, record in enumerate(voting_dict[sen_name]):
            result[i] = result[i] + record
    for i in range(len(result)):
        result[i] = result[i] / len(sen_set)
    return result

average_Democrat_record = [] # give the vector as a list



## 8: (Task 8) Bitter Rivals
def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> br = bitter_rivals(voting_dict)
        >>> br == ('Fox-Epstein', 'Ravella') or br == ('Ravella', 'Fox-Epstein')
        True
    """
    pre_record = None
    key_name = None
    rival_name = None
    for key in voting_dict.keys():
        rival = least_similar(key, voting_dict)
        new_dict = {key:voting_dict[key], least_similar:voting_dict[rival]}
        if pre_record == None:
            key_name = key
            rival_name = rival
            pre_record = policy_compare(key, least_similar, new_dict)
        current_record = policy_compare(key, least_similar, new_dict)
        if pre_record > current_record:
            pre_record = current_record
            key_name = key
            rival_name = rival

    return (rival_name, key_name)

