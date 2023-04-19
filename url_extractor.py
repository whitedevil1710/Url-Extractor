import re
import os
import sys
from termcolor import colored
import subprocess
import requests


def banner():
	print("")
	print(colored("██╗   ██╗██████╗ ██╗         ███████╗██╗  ██╗████████╗██████╗  █████╗  ██████╗████████╗ ██████╗ ██████╗ ","blue"))
	print(colored("██║   ██║██╔══██╗██║         ██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗","blue"))
	print(colored("██║   ██║██████╔╝██║         █████╗   ╚███╔╝    ██║   ██████╔╝███████║██║        ██║   ██║   ██║██████╔╝","green"))
	print(colored("██║   ██║██╔══██╗██║         ██╔══╝   ██╔██╗    ██║   ██╔══██╗██╔══██║██║        ██║   ██║   ██║██╔══██╗","yellow"))
	print(colored("╚██████╔╝██║  ██║███████╗    ███████╗██╔╝ ██╗   ██║   ██║  ██║██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║","yellow"))
	print(colored(" ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝","red"))
	print(colored("-----------------------c̲o̲d̲e̲d̲ b̲y̲ w̲h̲i̲t̲e̲d̲e̲v̲i̲l̲--------------------------------------------------------------","blue"))
banner()

class UrlExtractor:
    def __init__(self):
        self.file_path = None
        self.urls = []

    def set_url(self, url):
        self.file_path = None
        self.url=url
        self.urls = []
        print(colored(f"[*] URL set to {url}", "green"))
        self.extract(url)

    def set_path(self, file_path):
        self.file_path = file_path
        self.urls = []
        print(colored(f"[*] File path set to {file_path}", "green"))
        self.extract()

    def extract(self, url=None):
        if url is None:
            if self.file_path is None:
                print(colored("[!] Error: File path is not set", "red"))
                return

            if not os.path.exists(self.file_path):
                print(colored(f"[!] Error: File {self.file_path} not found", "red"))
                return

            with open(self.file_path) as file:
                content = file.read()
        else:
            try:
                response = requests.get(url)
                response.raise_for_status()
                content = response.text
            except requests.exceptions.RequestException as e:
                print(colored(f"[!] Error: Could not fetch URL {url}: {e}", "red"))
                return

        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\-\.]*(?:\?[\w\-\.\%]+=[\w\-\.\%]+)*(?:#[\w\-]+)*', content)
        self.urls.extend(urls)

        if url is None:
            print(colored(f"[*] Successfully extracted URLs from {self.file_path}", "green"))
        else:
            print(colored(f"[*] Successfully extracted URLs from {url}", "green"))

    def save(self, file_name):
        if not self.urls:
            print(colored("[!] Error: No URLs to save", "red"))
            return

        with open(file_name, 'a') as f:
            for u in self.urls:
                f.write(u + '\n')

        print(colored(f"[*] Successfully saved URLs to {file_name}", "green"))

    def print_urls(self):
        if not self.urls:
            print(colored("[!] Error: No URLs to print", "red"))
            return

        print(colored("[*] URLs extracted:", "green"))
        for url in self.urls:
            print(colored(url, "yellow"))

    def help(self):
        print(colored("""
        Description: Extracts all URLs available from a text file or URL.
        setpath: Set the file path to extract URLs from.
        seturl: Set the URL to extract URLs from.
        extract: Extract URLs from the file or URL.
        save: Save the extracted URLs to a file.
        print: Print all extracted URLs.
        help: Show this help message.
        exit: Exit the program.
        """, "green"))

    def clear(self):
    	subprocess.call('clear', shell=True)
    	banner()

def main():
	url_extractor = UrlExtractor()

	while True:
	    command = input(colored("\nEnter a command: ", "cyan"))

	    if command == "setpath":
	    	file_path = input(colored("Enter file path: ", "cyan"))
	    	url_extractor.set_path(file_path)

	    elif command == "extract":
	    	url_extractor.extract()

	    elif command == "seturl":
	    	url = input(colored("Enter the url: ","cyan"))
	    	url_extractor.set_url(url)
		
	    elif command == "save":
	    	file_name = input(colored("Enter file name [Default: urls.txt]: ", "cyan")) or "urls.txt"
	    	url_extractor.save(file_name)

	    elif command == "print":
	    	url_extractor.print_urls()

	    elif command == "help":
	    	url_extractor.help()

	    elif command == "exit":
	    	print(colored("Bye Bye...... \U0001F44B","red"))
	    	break
		
	    elif command == "clear":
	    	url_extractor.clear()
		
	    else:
	    	print(colored("[!] Error: Invalid command. Type 'help' to see available commands", "red"))
try:
	main()
except Exception as e:
	print(colored(f"Error: {e}","red"))
except KeyboardInterrupt:
	print(colored("\n[!] User Interrupted.","red"))
	sys.exit(0)
