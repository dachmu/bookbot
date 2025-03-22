def get_num_words(content):
    content_splited = content.split()
    return len(content_splited)


def char_count_summary(content):
    count_d = {}
    for c in content:
        if c.lower() in count_d.keys():
            count_d[c.lower()] += 1
        else:
            count_d[c.lower()] = 1
    return dict(count_d)

def sort_on(chars):
    return chars["count"]

def sort_chars_by_count(chars):
    chars = dict(chars)
    chars_list = []

    for char, val in chars.items():
        chars_list.append({"character": char, "count": val})


    # print(chars_list)
    chars_list.sort(reverse=True, key=sort_on)
    # print(chars_list)

    return list(chars_list)

def gen_report(chars, num_words, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char in chars:
        key, valk = char
        if char[key].isalpha():
            print(f"{char[key]}: {char[valk]}")

    print("============= END ===============")



