import sys, os, re

def check_extension(file) :
    if not (str(file).endswith(".template")) :
        raise Exception("file must be a file of \".template\"")
    return True

def parse_file_data(file) :
    dic = globals()
    line = open(file, 'r').read()
    for key, value in dic.items() :
        word = "".join(["{", key,"}"])
        line = line.replace(word, str(value))
    return line

def export_to_html(file, line) :

    head_template = '''<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <meta http-equiv="X-UA-Compatible" content="IE=edge">    <meta name="viewport" content="width=device-width, initial-scale=1.0">    <title>myCV</title></head><body>    <h1>My CV</h1>'''
    footer = '''</body></html>'''
    new_line = "".join([head_template, line, footer])
    new_file = open(str(file).replace(".template", ".html"), 'w')
    new_file.write(new_line)
    new_file.close()

def file_handler(file) :
    try :
        check_extension(file)
        line = parse_file_data(file)
        export_to_html(file, line)
    except Exception as e :
        print (e)

if __name__ == '__main__' :

    exec(open("settings.py", 'r').read())
    if (len(sys.argv) == 2) :
        file_handler(sys.argv[1])
    else:
        print ("Please send one template file only")
        
 