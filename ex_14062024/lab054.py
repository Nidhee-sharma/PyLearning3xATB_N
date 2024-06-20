#match case

browser = input("Enter a broswer or select/n")
browser =browser.lower() #converting to lower case
match browser:
    case "Edge":
        print("You have got the Edge!")
    case "edge":
        print("You have got the Edge!")
    case "safari":
        print("You have got the Safari!")
    case "chrome" | "Chrome" | "CHROME":
        print("You have got the Chrome!")
    case _:
        print("Sorry, not sure!")