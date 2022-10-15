"""
logic module for the indentation rule
"""

import re

def indentation_rule_main(content, number_of_spaces):
    """
    identifies the block and inserts indentation within that block
    """
    content_formatted_indentation = []
    marker = False
    number_of_spaces = number_of_spaces * " "
    for index, line in enumerate(content):
        # finds where the block starts
        if re.search(r"^\\begin{(?!document).*}", line):
            content_formatted_indentation.append(line)
            # loops through the lines within the block
            for line_within_the_block in content[index+1:]:
                # finds where the block stops,
                # sets marker to False to help the main for loop skip already indented block
                if re.search(r"^\\end{(?!document).*}", line_within_the_block):
                    marker = True
                    break
                # indents the line within the block
                if not re.search(r"^\s", line_within_the_block):
                    index +=1
                    content_formatted_indentation.append(number_of_spaces + line_within_the_block)
                else:
                    index +=1
                    content_formatted_indentation.append(line_within_the_block)
        # reverses marker to start appending the lines outside of the block
        elif re.search(r"^\\end{(?!document).*}", line):
            content_formatted_indentation.append(line)
            marker = False
        else:
            if marker:
                pass
            else:
                content_formatted_indentation.append(line) # appends lines outside of the block
    return content_formatted_indentation
