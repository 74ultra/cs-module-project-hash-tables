# Your code here
with open("robin.txt") as f:
    words = f.read()


def histo(s):
    # remove escape sequences
    c = ['\r', '\t', '\n']
    for i in c:
        s = s.replace(i, ' ')

    punc = {'"', ':', ';', ',', '.', '-', '+', '=', '/', "\\",
            '|', '[', ']', '{', '}', '(', ')', '*', '^', '&'}
    t = ''
    word_dict = {}
    # remove punctuation
    for i in s:
        if i not in punc:
            t += i
    # compare 't' to original string, if no puncuation in original string, return empty dict
    if t == s:
        return word_dict
    t = t.lower().split(' ')
    # count occurances of words and add to dict
    for i in t:
        if i in word_dict:
            word_dict[i] += '#'
        elif i != '':
            word_dict[i] = '#'
    # find longest word for spacing purposes on output
    longest_word = 0
    for i in word_dict.keys():
        if len(i) > longest_word:
            longest_word = len(i)
    # sort 'word_dict' into a list based on length of values
    dict_words = [(k, v) for k, v in sorted(
        word_dict.items(), key=lambda item: len(item[1]))]
    dict_words.reverse()
    # print out list items
    for i in dict_words:
        a = longest_word - len(i[0]) + 2
        b = " " * a
        print(f'{i[0]}{b}{i[1]}')
    return


histo(words)
