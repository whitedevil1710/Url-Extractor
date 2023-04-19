import re
import os
import sys
from termcolor import colored
import subprocess


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
    def clear(self):
    	subprocess.call('clear', shell=True)
    	banner()
	    
	    
    def set_path(self, file_path):
        self.file_path = file_path
        print(colored(f"[*] File path set to {file_path}", "green"))

    def extract(self):
        if self.file_path is None:
            print(colored("[!] Error: File path is not set", "red"))
            return

        if not os.path.exists(self.file_path):
            print(colored(f"[!] Error: File {self.file_path} not found", "red"))
            return

        with open(self.file_path) as file:
            for line in file:
                urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\-\.]*(?:\?[\w\-\.\%]+=[\w\-\.\%]+)*(?:#[\w\-]+)*', line)
                self.urls.extend(urls)

        print(colored(f"[*] Successfully extracted URLs from {self.file_path}", "green"))

    def save(self, file_name="urls.txt"):
        if not self.urls:
            print(colored("[!] Error: No URLs to save", "red"))
            return

        with open(file_name, 'a') as f:
            for u in self.urls:
                f.write(u + '\n')

        print(colored(f"[*] Successfully saved URLs to {file_name}", "green"))
    def help(self):
    	print(colored("""
	Discription: Extracrts all url available from a text file 
	setpath :	Set the file path
	extract :	Extract URLs from the file
	save	: 	Save the extracted URLs to a file
	print 	:	Print all extracted URLs
	help	:	Show this help message
	exit	: 	Exit the program
	clear	: 	Clears the terminal.
		""", "green"))
    def print_urls(self):
        if not self.urls:
            print(colored("[!] Error: No URLs to print", "red"))
            return

        print(colored("[*] URLs extracted:", "green"))
        for url in self.urls:
            print(colored(url, "yellow"))


def main():
	url_extractor = UrlExtractor()

	while True:
	    command = input(colored("\nEnter a command: ", "cyan"))

	    if command == "setpath":
	    	file_path = input(colored("Enter file path: ", "cyan"))
	    	url_extractor.set_path(file_path)

	    elif command == "extract":
	    	url_extractor.extract()

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
