"""
logic for the newline after a sentence rule
"""

import re

def newline_rule_main(content, escape_seq):
    """
    identifies a sentence and inserts a newline after it
    """
    content_formatted_newlines = []
    for original_line in content:
        current_line_index = content.index(f"{original_line}")
        next_line_index = current_line_index + 1
        if re.search(r"^(?![%]).*[\.!?;:]$", original_line) and content[next_line_index] != "\n":
            content_formatted_newlines.append(f"{original_line}{escape_seq}")
        else:
            content_formatted_newlines.append(original_line)
    return content_formatted_newlines
