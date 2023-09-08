#mutability - zmienność
filenames = ["1.Raw data.txt", "2.Reports.txt", "3.Presentations.txt"]
for filename in filenames:
    new_file = filename.replace(".","").replace("1","").replace("2","").replace("3","").replace("txt","")
    print(new_file)