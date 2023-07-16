#!/usr/bin/python3
import sys
import os
import markdown

def convert_markdown_to_html(inputmd, outputhtml):
   
    
    if not os.path.isfile(inputmd):
        sys.stderr.write('Missing {}\n'.format(inputmd))
        sys.exit(1)

    with open(inputmd, 'r') as f:
        markdown_text = f.read()


    html_text = markdown.markdown(markdown_text)

    with open(outputhtml, 'w') as f:
        f.write(html_text)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        sys.exit(1)
    if len(sys.argv) > 3:
        sys.exit(1)

    inputmd = sys.argv[1]
    outputhtml = sys.argv[2]

    convert_markdown_to_html(inputmd, outputhtml)

    sys.exit(0)
