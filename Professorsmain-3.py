'''
cs2420 Project 7 -  HaspMap
Dana Doggett
Dec 9, 2019
'''
from hashmap import HashMap

def clean_line(raw_line):
    '''removes all punctuation from input string and
    returns a list of all words which have a length greater than one '''
    if not isinstance(raw_line, str):
        raise ValueError("Input must be a string")
    line = raw_line.strip().lower()
    line = list(line)
    for index in range(len(line)):  # pylint: disable=C0200
        if line[index] < 'a' or line[index] > 'z':
            line[index] = ' '
    cleaned = "".join(line)
    words = [word for word in cleaned.split() if len(word) > 1]
    return words

def main():
    ''' driver app to open text file and perform a frequency count using
    a Hashmap. The top 15 words, and their frequency are output to console '''
    hash_map = HashMap()
    with open("AliceInWonderland.txt", encoding="utf8") as input_file:
        for raw_line in input_file:
            words = clean_line(raw_line)

            for word in words:
                hash_map.set(word, hash_map.get(word, 0)+1)

    keys = hash_map.keys()
    key_values = [(key, hash_map.get(key)) for key in keys]
    key_values.sort(reverse=True, key=lambda x: x[1])

    print("The most common words are:")
    for element in key_values[:15]:
        print(f"{element[0]}\t\t{element[1]}")
    print()


if __name__ == "__main__":
    main()
