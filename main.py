import collections

def getFileAsString(pathToFile):
    fileContents = ""
    with open(pathToFile) as f:
        fileContents = f.read()
    return fileContents

def numWordsInFile(fileContents):
    numWords = fileContents.split()
    return len(numWords)

def occurancesOfLetters(fileContents):
    counts = collections.Counter(char for char in fileContents.lower() if char.isalpha())
    return counts

def printReport(pathToFile, numWords, sortCounts):
    print(f"--- Begin report of {pathToFile} ---")
    print(f"{numWords} words found in the document\n")
    for letter, count in sortCounts:
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

def main():
    pathToFile = "books/frankenstein.txt"
    fileContents = getFileAsString(pathToFile)
    numWords = numWordsInFile(fileContents)
    counts = occurancesOfLetters(fileContents)
    sortCounts = sorted(counts.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    printReport(pathToFile, numWords, sortCounts)

main()