import click
import re

@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.option("--comment", default=1, help="How many spaces do you want to insert after %?")
def main(filename, comment):
    num_of_spaces = comment * " "
    with open(filename, "r") as _f:
        with open(f"{filename[0:-4]}-edited.tex", "w") as _f2:
            content = _f.readlines()
            for line in content:
                if re.search(r"^%{2,}[^ %]", line):
                    match = re.search(r"%{2,}[^\s]", line)
                    end = match.span()[1]
                    print(match.span())
                    _f2.write(f"{line[0:end-1]}{num_of_spaces}{line[end-1:]}")
                elif re.search(r"^%[^ %]", line):
                    _f2.write(f"{line[0]}{num_of_spaces}{line[1:]}")
                else:
                    _f2.write(line)
