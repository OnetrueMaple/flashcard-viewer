# I needed a program to automatically format data into the json data structure used for my flashcard program.

def main():
    num = 0
    userText = "placeholder"
    filename = "flashcards.txt"

    print("Flashcard generator. Enter 'quit' at any point to quit.")
    print("Start from which index?")
    num = int(input())

    while(userText != "quit") :
        with open(filename, "a") as f:
            f.write("{\n")
            f.write("\"id\": " + str(num) + ",\n")

        print("Enter front of card content:")
        with open(filename, "a") as f:
            f.write("\"front_content\": \"")
        userText = input()
        with open(filename, "a") as f:
            f.write(userText)
            f.write("\",\n")

        print("Enter back of card content:")
        with open(filename, "a") as f:
            f.write("\"back_content\": \"")
        userText = input()
        with open(filename, "a") as f:
            f.write(userText)
            f.write("\"\n")
            f.write("},\n")

        num = num + 1

    print("Program ended correctly.")

if __name__ == "__main__":
    main()