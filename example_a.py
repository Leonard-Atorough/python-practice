a = "A B C D E F"
b = "Y B H D A G"


def first_difference(str1, str2):

    difference = ""
    
    set_a = set(a)
    set_b = set(b)
    for word_a in set_a:
        if word_a not in set_b:
            if word_a not in difference:
                difference += word_a
    print(sorted(difference))

first_difference(a, b)
