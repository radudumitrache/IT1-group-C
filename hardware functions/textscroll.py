import time

names = ["Dumitrache Marian", "Schuepbach Alex", "Nefeli Chrysostomou"]
#availableSpace could just be a constant and not be passed into the function
availableSpace = 15


def displayText(texts: list, screenLength: int):

    counter = 0
    index = 0
    index1 = 0
    index2 = 0
    index3 = 0

    while True:

        for text in texts:

            match counter:
                case 0:
                    index = index1
                case 1:
                    index = index2
                case 2:
                    index = index3

            if len(text) > screenLength:
                print(index + screenLength)
                print(len(text))
                if index + screenLength <= len(text):

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
                    index = index + 1
                    match counter:
                        case 0:
                            index1 = index
                        case 1:
                            index2 = index
                        case 2:
                            index3 = index
                    time.sleep(0.5)

                else:
                    match counter:
                        case 0:
                            index1 = 0
                        case 1:
                            index2 = 0
                        case 2:
                            index3 = 0

                # delay, modify as necessary
                time.sleep(1)

            else:
                print(text)
                time.sleep(0.5)

            if counter >= 2:
                counter = 0
            else:
                counter = counter + 1
        print()

displayText(names, availableSpace)
