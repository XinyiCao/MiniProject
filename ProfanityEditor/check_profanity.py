import urllib.request


def read_text():
    quotes = open("/Users/CAO/Pythonia/Udacity_PythonFundamental/ProfanityEditor/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

def accumulate_text():
    with open("/Users/CAO/Pythonia/Udacity_PythonFundamental/ProfanityEditor/movie_quotes.txt",
            "r") as f:
        accumulate = ""
        for line in f:
            cleanedLine = line.strip()
            if cleanedLine: # is not empty
                accumulate = accumulate + cleanedLine
                print(cleanedLine)
        cleanedText = accumulate.replace(' ', '%20')
            # for space in cleanedLine:
                # cleanedText = cleanedText.writelines("\n".join(cleanedText))
    print(cleanedText)
    check_profanity(cleanedText)

def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=" + text_to_check)
    output = connection.read()
    output = output.decode()
    print(output)
    # bytes_text = bytes(output, encoding='utf-8')
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This text has no curse word!")
    else:
        print("Could not get proper response.")

accumulate_text()