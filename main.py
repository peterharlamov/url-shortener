import pyshorteners;
import validators;

while True:
    # Get the long url from the user input.
    long_url = str(input("Enter the long url: "));

    # Check if the long url is valid.
    validate_url = validators.url(long_url); # type: ignore

    if validate_url:  
        # Shorten the long url.
        print("URL is valid");
        type_tiny = pyshorteners.Shortener();
        short_url = type_tiny.tinyurl.short(long_url);
        print("Your short url is: ", short_url);
    else:
        print("URL is invalid");
    
    # Close the program if user wants to exit.
    close = str(input("Do you want to close the program? (y/n): "));
    if close == "y" or close == "Y" or close == "yes" or close == "Yes":
        pass;
    else:
        break;