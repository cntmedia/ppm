#!/usr/bin/env python
import subprocess
import os

def applescript_subprocess(applescript_code):
	"Run the given AppleScript and return the standard output and error."
	osa = subprocess.Popen(['osascript', '-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=None,shell=True)
	return str(osa.communicate(applescript_code)[0])

prompt_dialog_for_short_code_number = '''
tell application (path to frontmost application as text)
set short_code_number to the text returned of (display dialog "!!!!!?" default answer "")
end tell
return short_code_number
'''

prompt_dialog_for_file_path_location = '''
tell application (path to frontmost application as text)
set file_path_location to choose file with prompt "Open file to be edited"
tell application "System Events"
return POSIX path of file_path_location
end tell
end tell
return file_path_location
'''


get_short_code_number = applescript_subprocess(prompt_dialog_for_short_code_number)
short_code_number = str(get_short_code_number).rstrip()

get_file_path_location = applescript_subprocess(prompt_dialog_for_file_path_location)
file_path_location = str(get_file_path_location).rstrip()

with open(file_path_location) as file_data:
	for number_of_lines_in_file_data in file_data:
		file_data_as_string = number_of_lines_in_file_data

file_password = ''
file_password = file_data_as_string[-int(short_code_number):]

set_file_password_to_clipboard = '''
set the clipboard to ("%s" as text)
'''%(file_password)

applescript_subprocess(set_file_password_to_clipboard)

print file_password