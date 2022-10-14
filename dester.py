"""
A linter to modify LaTeX files.
"""

__version__ = "0.4"

import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

# pylint: disable=no-value-for-parameter, line-too-long, too-many-arguments

import platform
import click
from src.comment_rule import comment_rule_main
from  src.newline_rule import newline_rule_main
from src.indentation_rule import indentation_rule_main
from src.blank_line_rule import blank_line_rule_main


@click.command()
@click.argument("input_file", type=click.Path(exists=True), required=True)
@click.option("--comment", default=1, type=int, help="How many spaces to insert after %?")
@click.option("--newline", default=True, type=bool, help="Insert a new line after a sentence?")
@click.option("--indent", default=4, type=int, help="Indent content within the block.")
@click.option("--blank_lines", default=1, type=int, help="Number of blank lines to be inserted before section/chapter etc.")
@click.option("--overwrite", default=False, type=bool, help="Overwrite the original input file.")
def main(input_file, comment, newline, indent, blank_lines, overwrite):
    """
    the main function to check all the parameters and execute the program
    """
    file_name, file_extension = os.path.splitext(input_file)
    if platform.system() == "Windows":
        escape_seq = "\r\n"
    else :
        escape_seq = "\n"

    if overwrite:
        output_file = input_file
    else:
        output_file = f"{file_name}-edited{file_extension}"

    if file_extension in (".tex", ".bib", ".tikz"):
        with open(input_file, "r", encoding="utf-8") as _f:
            content = _f.readlines()
            formatted_comments_content = comment_rule_main(content, comment)
            if newline:
                formatted_newline_content = newline_rule_main(formatted_comments_content, escape_seq)
                formatted_indent_content = indentation_rule_main(formatted_newline_content, indent)
                formatted_sections_content = blank_line_rule_main(formatted_indent_content, blank_lines, escape_seq)
            else:
                formatted_indent_content = indentation_rule_main(formatted_comments_content, indent)
                formatted_sections_content = blank_line_rule_main(formatted_indent_content, blank_lines, escape_seq)
        with open(output_file, "w", encoding="utf-8") as output:
            for lines in formatted_sections_content:
                output.write(lines)
        print(f"Successfully modified the file {input_file}")
    else:
        print("Wrong file extension")
        return

if __name__ == "__main__":
    main()
