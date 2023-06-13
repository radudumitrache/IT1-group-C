import time

names = ["Dumitrache, Marian", "Schuepbach, Alex", "Chrysostomou, Nefeli"]
# availableSpace could just be a constant and not be passed into the function
availableSpace = 15


def display_text(text: str, screen_length: int, screen_row: int, index: int):

    if len(text) > screen_length:

        if index + screen_length <= len(text):

            # determines where to start displaying the string from
            char_index = 0 + index
            string_build = ""

            while (char_index < screen_length + index) & (char_index < len(text)):
                # add current string character to the stringBuild, this could be done with substrings
                string_build = string_build + text[char_index]

                # next character
                char_index += 1

            # replace with screen output command
            print(string_build)
            index = index + 1

        else:

            string_build = ""
            char_index = index - 1

            while (char_index < screen_length + index) & (char_index < len(text)):
                string_build = string_build + text[char_index]
                char_index += 1

            print(string_build)
            index = 0

        # delay, modify as necessary
        time.sleep(1)

    else:
        print(text)
        time.sleep(1)

    return index


index1 = 0
index2 = 0
index3 = 0

while True:

    for i in range(3):

        match i:
            case 0:
                index1 = display_text(names[i], availableSpace, counter, index1)
            case 1:
                index2 = display_text(names[i], availableSpace, counter, index2)
            case 2:
                index3 = display_text(names[i], availableSpace, counter, index3)

    print()
