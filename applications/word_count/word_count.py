def word_count(s):
    c = ['\r', '\t', '\n']
    for i in c:
        s = s.replace(i, ' ')
    punc = {'"', ':', ';', ',', '.', '-', '+', '=', '/', "\\",
            '|', '[', ']', '{', '}', '(', ')', '*', '^', '&'}
    t = ''
    word_dict = {}
    for i in s:
        if i not in punc:
            t += i
    if t == s:
        return word_dict
    t = t.lower().split(' ')
    for i in t:
        if i == ' ':
            continue
        elif i in word_dict:
            word_dict[i] += 1
        elif i != '':
            word_dict[i] = 1
    return word_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
