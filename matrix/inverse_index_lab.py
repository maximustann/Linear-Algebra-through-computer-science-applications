# version code d345910f07ae
coursera = 1
# Please fill out this stencil and submit using the provided submission script.
import random



## 1: (Task 1) Movie Review
## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    return name[random.randint(0, len(name) - 1)]



## 2: (Task 2) Make Inverse Index
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.
    Distinguish between an occurence of a string (e.g. "use") in the document as a word
    (surrounded by spaces), and an occurence of the string as a substring of a word (e.g. "because").
    Only the former should be represented in the inverse index.
    Feel free to use a loop instead of a comprehension.

    Example:
    >>> makeInverseIndex(['hello world','hello','hello cat','hellolot of cats']) == {'hello': {0, 1, 2}, 'cat': {2}, 'of': {3}, 'world': {0}, 'cats': {3}, 'hellolot': {3}}
    True
    """
    wordlist = [item.split() for item in strlist]
    unpack_wordlist = []
    for words in wordlist:
        for word in words:
            unpack_wordlist.append(word)
    wordset = set(unpack_wordlist)
    dict_item = []
    for word in wordset:
        count_set = set()
        for (i, item) in enumerate(strlist):
            for k in item.split():
                if word == k:
                    count_set.add(i)
                    break
        dict_item.append(count_set)

    return {x:y for (x, y) in list(zip(wordset, dict_item))}

## 3: (Task 3) Or Search
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    Feel free to use a loop instead of a comprehension.
    
    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> orSearch(idx, ['Bach','the'])
    {0, 2, 3, 4, 5}
    >>> orSearch(idx, ['Johann', 'Carl'])
    {0, 2, 3, 4, 5}
    """
    index_list = []
    result = set()
    for item in query:
        index_list.append(inverseIndex[item])
    result = index_list[0]
    for i in range(len(index_list)):
        result = index_list[i] | result
    return result



## 4: (Task 4) And Search
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    Feel free to use a loop instead of a comprehension.

    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> andSearch(idx, ['Johann', 'the'])
    {2, 3}
    >>> andSearch(idx, ['Johann', 'Bach'])
    {0, 4}
    """
    index_list = []
    result = set()
    for item in query:
        index_list.append(inverseIndex[item])
    result = index_list[0]
    for i in range(len(index_list)):
        result = index_list[i] & result
    return result

