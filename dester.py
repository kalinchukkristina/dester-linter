"""
Entry point for dester-linter
"""

# pylint: disable=no-value-for-parameter

import os
import click
import src.comment_rule
import src.newline_rule
import src.indentation_rule


@click.command()
@click.argument("input_file", type=click.Path(exists=True), required=True)
@click.option("--comment", default=1, type=int, help="How many spaces to insert after %")
@click.option("--newline", default=True, type=bool, help="Insert a new line after a sentence?")
@click.option("--indent", default=4, type=int, help="Indent content within the block")
def main(input_file, comment, newline, indent):
    """
    the main function to check all the parameters and execute the program
    """
    file_name, file_extension = os.path.splitext(input_file)
    if file_extension in (".tex", ".bib", ".tikz"):
        with open(input_file, "r", encoding="utf-8") as _f:
            content = _f.readlines()
            formatted_comments_content = src.comment_rule.comment_rule_main(content, comment)
            if newline:
                formatted_newline_content = src.newline_rule.newline_rule_main(formatted_comments_content)
                formatted_indent_content = src.indentation_rule.indentation_rule_main(formatted_newline_content, indent)
            else:
                formatted_indent_content = src.indentation_rule.indentation_rule_main(formatted_comments_content, indent)
        with open(f"{file_name}-edited{file_extension}", "w", encoding="utf-8") as output:
            for lines in formatted_indent_content:
                output.write(lines)
        print(f"Successfully modified the file {input_file}")
    else:
        print("Wrong file extension")
        return

if __name__ == "__main__":
    main()
