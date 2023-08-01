""" 
    text = ["deeplearning","d,dll,a,deep,dee,base,lear,learning"]
"""

def word_split(text):
    word = list(text[0])  # I converted the word in the 'text' list to a list of individual letters to distinguish them.

    parse_list = text[1].split(",")  # I split the string in 'text' list to create a list of words.

    results = []  # I created a list to store multiple results, as there could be more than one possible combination.

    for index in range(1, len(word)):
        temp = word[:]
        temp.insert(index, " ")
        parse1, parse2 = "".join(temp).split()

        if parse1 in parse_list and parse2 in parse_list:
            results.append(parse1 + " " + parse2)  # I added the combination to the results list when both parts are found.

    if results:
        return results
    else:
        return "I couldn't find (no way)"

# Tests
print(word_split(["deeplearning", "d,dll,a,deep,dee,base,eeplearning,learning"]))
print(word_split(["deeplea4ning", "d,dll,a,deep,dee,base,lear,learning"]))
