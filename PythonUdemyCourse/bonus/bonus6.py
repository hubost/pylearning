contents = ["Text to document.txt","Text to report.txt", "Text to presentation.txt"]

filenames = ["doc.txt","report.txt","presentation.txt"]

for content, filename in  zip(contents,filenames):
    file = open(f"{filename}", 'w')
    file.write(content)