"""
logic module for the comment rule
"""
import re

def comment_rule_main(content, number_of_space):
    """
    the main function which identifies the lines with comments
    """
    content_formatted_comments = []
    for line in content:
        # if there are more than one % sign as a comment
        if re.search(r"^%{2,}[^ %]", line):
            result = comment_rule_many_percent_signs(number_of_space, line)
            content_formatted_comments.append(result)
        # one % sign as a comment
        elif re.search(r"^%[^ %]", line):
            result = comment_rule_one_percent_sign(number_of_space, line)
            content_formatted_comments.append(result)
        else:
            content_formatted_comments.append(line)
    return content_formatted_comments

def comment_rule_one_percent_sign(comment, line):
    """
    modifies the line with one % sign as a comment
    """
    num_of_spaces = comment * " "
    modified_line = f"{line[0]}{num_of_spaces}{line[1:]}"
    return modified_line

def comment_rule_many_percent_signs(comment, line):
    """
    modifies the line where there are more than one % sign
    """
    num_of_spaces = comment * " "
    match = re.search(r"%{2,}[^\s]", line)
    end = match.span()[1]
    modified_line = f"{line[0:end-1]}{num_of_spaces}{line[end-1:]}"
    return modified_line
