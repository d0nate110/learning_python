def tokenize(document):
    words = []
    for line in document:
        word = ''
        digit = ''
        # This for loop iterates over each letter in the line. 
        # The variable isSymbol is there to return true only if all of the conditions that are assigned to it are false.
        # If the letter is not a letter, a digit and a space, then it must be a symbol.
        # If the letter is a letter, then it is added to the word variable in lower case and is stored there. 
        # If it is a digit, then it is added to digit variable in the same way as word variable.
        # Else, if digit is not empty, then it is added to words list, and likewise id word is not empty then it is added to words array. 
        for letter in line:
            isSymbol = letter.isalpha() == False and letter.isdigit() == False and letter.isspace() == False

            if letter.isalpha():
                word += letter.lower()
            elif letter.isdigit():
                digit += letter
            else:
                if digit:
                    words.append(digit)
                    digit = ''
                if word:
                    words.append(word)
                    word = ''
            if isSymbol:
                words.append(letter)

        if digit:
            words.append(digit) 
        if word:
            words.append(word)
    return words

def countWords(words, stopWords):
    frequencies = {}
    for word in words:
        # The for loop goes over each word in words list.
        # If word is in stop words, then iteration is skipped.
        # If the word is in frequencies, then the count is incremented.
        # Otherwise, set the first occurence of a word to 1. 
        if word in stopWords:
            continue
        elif word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

def printTopMost(frequencies, n):
    # Sort all the items in frequencies list in reverse order(highest first), and print until the loop reaches nth index. 
     sorted_frequencies = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))
     count = 0
     for key, value in sorted_frequencies.items():
         if count < n:
             print(f"{key.ljust(20)}{str(value).rjust(5)}") 
             count += 1
         else:
             break
