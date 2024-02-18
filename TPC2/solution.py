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



def convert_md_to_html(file_name):
    
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>''' + file_name[:-3] + '''</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    '''

    file = open("origin.md")
    list_flag = False
    for line in file.readlines():
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
    file.close()

    return html


if __name__ == "__main__":
    html_content = convert_md_to_html(sys.argv[1])

    file = open("converted_file.html", "w", encoding="utf-8")
    file.write(html_content)
    file.close()