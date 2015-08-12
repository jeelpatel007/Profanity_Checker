#import urllib
import requests

# read_text parse the text file to be used for profanity check.

def read_text():
# Replace below location with the location of text file on your machine
	file_reader = open("C:\Users\Jeel\Desktop\Python\adventure.txt")
	contents_of_file = file_reader.read()
	print (contents_of_file)
	file_reader.close()
	check_profanity(contents_of_file)

# check_profanity sends the text to wdyl and returns the profanity results

def check_profanity(text_to_check):
		#connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
		#output = connection.read()
		#print (output)
		#connection.close()
		r = requests.get('http://www.wdyl.com/profanity', params={'q': text_to_check})

# display the result of our test and print a warning message if foul words are found

		if "true" in r.text:
			print("Profanity Alert!!")
		elif "false" in r.text:
			print ("No Profanity Found")
		else:
			print("Could not scan the document properly")
		
if __name__ == "__main__":
	read_text()
