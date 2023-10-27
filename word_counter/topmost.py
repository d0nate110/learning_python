import wordfreq
import sys
import urllib.request

def main():

    tokenized_stop_words = []
    tokenized_normal_words = []

    stop_words_file = open(sys.argv[1])
    for line in stop_words_file:
        tokenized_stop_words.append(line.strip())
    stop_words_file.close()

    if sys.argv[2].startswith("https://") or sys.argv[2].startswith("http://"):
        response = urllib.request.urlopen(sys.argv[2])
        lines = response.read().decode("utf8").splitlines() 
        tokenized_normal_words = wordfreq.tokenize(lines)
    else:
        normal_words_file = open(sys.argv[2])
        tokenized_normal_words = wordfreq.tokenize(normal_words_file)
        normal_words_file.close()

    frequencies =  wordfreq.countWords(tokenized_normal_words, tokenized_stop_words)

    wordfreq.printTopMost(frequencies, int(sys.argv[3]))
main() 

