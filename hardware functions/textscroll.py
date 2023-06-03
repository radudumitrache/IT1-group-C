import time

name = "Dumitrache, Marian"
#availableSpace could just be a constant and not be passed into the function
availableSpace = 15

#this function is not usable for multiple pieces of text, concurrent processing is currently not possible
def displayText(text: str, screenLength: int):

    if len(text) > screenLength:

        index = 0
        while index + screenLength <= len(text):

            # determines where to start displaying the string from
            charIndex = 0 + index
            stringBuild = ""

            while (charIndex < screenLength + index) & (charIndex < len(text)):
                #add current string character to the stringBuild, this could be done with substrings
                stringBuild = stringBuild + text[charIndex]

                #next character
                charIndex += 1

            # replace with screen output command
            print(stringBuild)
            index += 1
            time.sleep(0.5)

        # delay, modify as necessary
        time.sleep(1)

    else:
        print(text)

displayText(name, availableSpace)
displayText(name, availableSpace)