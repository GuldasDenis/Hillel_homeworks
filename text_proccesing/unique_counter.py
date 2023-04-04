story = 'DOWN THE RABBIT HOLE. Alice had sat on the bank by her sis-ter till she was tired.' \
        'Once or twice she had looked at the book her sis-ter held in her hand,' \
        'but there were no pict-ures in it, "and what is the use of a book," thought Alice,' \
        '"with-out pict-ures?" She asked her-self as well as she could,' \
        'for the hot day made her feel quite dull, if it would be worth while' \
        'to get up and pick some dai-sies to make a chain.' \
        'Just then a white rab-bit with pink eyes ran close by her.'


def count_words(story):
    word_counts = {}
    for word in story.lower().split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


storyes = count_words(story)
print(storyes)
