import re
import sys

def replace_if_header(match):
    if match.group(1):
        level = len(match.group(2))
        return match.group(1) + "<h" + str(level) + ">" + match.group(3) + "</h" + str(level) + ">"
    elif not match.group(1):
        level = len(match.group(2))
        return "<h" + str(level) + ">" + match.group(3) + "</h" + str(level) + ">"
    else:
        return match.group(0)



def convert_md_to_html(lines_file):
    
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Converted File</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    '''

    list_flag = False
    for line in lines_file:
        converted_line = ""
        converted_line = re.sub("^(\d+)\.( .*)$", "<li>\\2</li>", line)
        converted_line = re.sub("^(.*\s)?(#{1,6})? (.*)$", replace_if_header, converted_line)
        if converted_line==line:
            converted_line = "<p>" + converted_line + "</p>"
        converted_line = re.sub("\*\*(.*)\*\*", "<b>\\1</b>", converted_line)
        converted_line = re.sub("\*(.*)\*", "<i>\\1</i>", converted_line)
        converted_line = re.sub("!\[(.*)\]\((.*)\)", "<img src='\\2' alt='\\1'/>", converted_line)
        converted_line = re.sub("\[(.*)\]\((.*)\)", "<a href='\\2'>\\1</a>", converted_line)

        if converted_line[:4]=="<li>" and not list_flag:
            list_flag = True
            html += "<ul>" + converted_line
        elif converted_line[:4]!="<li>" and list_flag:
            list_flag = False
            html += converted_line + "</ul>"
        else:
            html += converted_line
    
    html += "</body></html>"

    return html


if __name__ == "__main__":

    input_md = sys.stdin.read()
    lines_md = input_md.split('\n')
    html_content = convert_md_to_html(lines_md)

    file = open("converted_file.html", "w", encoding="utf-8")
    file.write(html_content)
    file.close()