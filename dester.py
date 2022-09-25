"""
Entry point for dester-linter
"""
import re
import os
import click


@click.command()
@click.argument("file", type=click.Path(exists=True), required=True)
@click.option("--comment", default=1, type=int, help="How many spaces to insert after %?")
@click.option("--newline", default=True, type=bool, help="Insert a new line after a sentence?")
def main(file, comment, newline):
    """
    the main function to check all the parameters and execute the program
    """
    file_name, file_extension = os.path.splitext(file)
    num_of_spaces = comment * " "
    if file_extension in (".tex", ".bib", ".tikz"):
        with open(file, "r", encoding="utf-8") as _f:
            with open(f"{file_name}-edited{file_extension}", "w", encoding="utf-8") as _f2:
                content = _f.readlines()
                for line in content:
                    current_line_index = content.index(f"{line}")
                    next_line_index = current_line_index + 1
                    if re.search(r"^%{2,}[^ %]", line):
                        match = re.search(r"%{2,}[^\s]", line)
                        end = match.span()[1]
                        _f2.write(f"{line[0:end-1]}{num_of_spaces}{line[end-1:]}")
                    elif re.search(r"^%[^ %]", line):
                        _f2.write(f"{line[0]}{num_of_spaces}{line[1:]}")
                    elif newline and re.search(r"^(?![%]).*[\.!?;:]$", line) and \
                        content[next_line_index] != "\n":
                        _f2.write(f"{line}\n")
                    else:
                        _f2.write(line)
        print(f"Successfully modified the file {file}")
    else:
        print("Wrong file extension")