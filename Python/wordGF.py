def countWords(string):
    # Remove any leading or trailing spaces to make counting easier.
    string = string.strip()

    # Handle the empty string as a special case.
    if string == "":
        return 0

    # Count the spaces to count the number of words.
    count = 1
    for ch in string:
        if ch == " ":
            count += 1
    return count

def main():
    inputStr = input("Enter a string: ")
    inputStrWordCount = countWords(inputStr)
    print("The string contains", inputStrWordCount, "words")

# Call the main function.
main()

input("Press Enter to exit...")    