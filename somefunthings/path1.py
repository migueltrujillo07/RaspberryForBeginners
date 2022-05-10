from pathlib import Path
myfile = ['accounts.txt', 'details.cvs', 'invite.docx']
for filename in myfile:
    print(Path(r'c:/users/Al', filename))
