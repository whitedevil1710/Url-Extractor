# URL Extractor Script

The URL Extractor is a Python script that extracts all URLs available from a text file or URL. This interactive script can be executed in a terminal, allowing users to enter commands and extract URLs from text files or URLs. The extracted URLs are then saved to a separate file for easy access and management. With its ability to extract all URLs from a given source, the URL Extractor is a useful tool for anyone who needs to gather and organize a large amount of URL data.

## Usage

To use the script, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using the command 
``` 
python url_extractor.py
```
3. Enter commands when prompted to interact with the script.

### Commands

The following commands are available:

- `setpath`: Sets the file path to the input text file.
- `seturl`: Sets URL to extract
- `extract`: Extracts URLs from the input text file.
- `save`: Saves the extracted URLs to a new file.
- `print`: Prints all extracted URLs to the terminal.
- `help`: Shows a help message with all available commands.
- `exit`: Exits the script.
- `clear`: Clears the terminal screen.

### Example Usage

1. Run the script using the command 
``` 
python url_extractor.py
```
2. Enter the command `setpath` and provide the path to the input text file.This command will ask prompt an input to enter the file path.
3. Enter the command `seturl` and provide the url from which it to be extracted.This command will ask prompt an input to enter the url.
4. Enter the command `extract` to extract the URLs from the input file.
5. Enter the command `save` to save the extracted URLs to a new file.
6. Enter the command `print` to print the extracted URLs to the terminal.

## Requirements

This script requires the following Python modules:

- `re`
- `os`
- `sys`
- `termcolor`
- `subprocess`

## Author

This script was created by [white_devil](https://github.com/whitedevil1710).

