"""
Entry point for dester-linter
"""
import re
import os
import click


@click.command()
@click.argument("input_file", type=click.Path(exists=True), required=True)
@click.option("--comment", default=1, type=int, help="How many spaces to insert after %")
@click.option("--newline", default=True, type=bool, help="Insert a new line after a sentence?")
def main(input_file, comment, newline):
    """
    the main function to check all the parameters and execute the program
    """
    file_name, file_extension = os.path.splitext(input_file)
    if file_extension not in (".tex", ".bib", ".tikz"):
        print("Wrong file extension")
        return
    else:
        with open(input_file, "r", encoding="utf-8") as input:
            with open(f"{file_name}-edited{file_extension}", "w", encoding="utf-8") as output:
                content = input.readlines()
                for line in content:
                    current_line_index = content.index(f"{line}")
                    next_line_index = current_line_index + 1
                    # more than one % sign 
                    if re.search(r"^%{2,}[^ %]", line):
                        result = comment_rule_many_percent_signs(comment, line)
                        output.write(result)
                    # one % sign
                    elif re.search(r"^%[^ %]", line):
                        result = comment_rule_one_percent_sign(comment, line)
                        output.write(result)
                    # newline rule
                    elif newline and re.search(r"^(?![%]).*[\.!?;:]$", line) and \
                        content[next_line_index] != "\n":
                        output.write(f"{line}\n")
                    # indentation rule
                    elif re.search(r"\\begin{(?!document).*}", line):
                        pass
                    else:
                        output.write(line)
        print(f"Successfully modified the file {input_file}")

def comment_rule_one_percent_sign(comment, line):
    num_of_spaces = comment * " "
    modified_line = f"{line[0]}{num_of_spaces}{line[1:]}"
    return modified_line

def comment_rule_many_percent_signs(comment, line):
    num_of_spaces = comment * " "
    match = re.search(r"%{2,}[^\s]", line)
    end = match.span()[1]
    modified_line = f"{line[0:end-1]}{num_of_spaces}{line[end-1:]}"
    return modified_line

def indent_block():
    if re.search(r"\\end{(?!document).*}"):
        pass

if __name__ == "__main__":
    main()