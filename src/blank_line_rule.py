"""
logic module for the blank line rule
"""
# pylint: disable=line-too-long

import re

def blank_line_rule_main(content, number_of_blank_lines):
    """
    indentifies section\\subsection\\subsubsection\\chapter\\paragraph\\subparagraph
    and insertes a blank line before it
    """
    content_formatted_sections = []
    blank_lines = "\n" * number_of_blank_lines
    for line in content:
        current_line_index = content.index(line)
        prev_line_index = current_line_index - 1
        if re.search(r"^\\section|\\subsection|\\chapter|\\subsubsection|\\paragraph|\\subparagraph", line) \
           and content[prev_line_index] != "\n":
            content_formatted_sections.append(f"{blank_lines}{line}")
        else:
            content_formatted_sections.append(line)
    return content_formatted_sections
