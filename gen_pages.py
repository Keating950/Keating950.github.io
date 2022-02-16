#!/usr/bin/env python3
from dataclasses import dataclass
import yaml
from typing import Optional, List
import re
from pathlib import Path
import sys
import argparse
from jinja2 import Environment, FileSystemLoader, StrictUndefined

TEMPLATE = "template.j2"


@dataclass(init=False)
class Page:
    title: str
    filename: str
    bar_title: str
    bar_exclude: bool
    bar_order: Optional[int]
    image_html: Optional[str]
    text: str

    def __init__(self, filepath: str):
        pattern = re.compile("---(.*)---", re.DOTALL)
        with open(filepath) as f:
            file_text = f.read()
        yaml_text = pattern.match(file_text)
        if not yaml_text or len(yaml_text.groups()) < 1:
            raise ValueError(f"No YAML header found for file {filepath}")
        try:
            header = yaml.load(yaml_text.group(1), Loader=yaml.Loader)
            self.title = header["title"]
            self.filename = Path(filepath).with_suffix(".html").name
            if exclude := header.get("bar_exclude"):
                if type(exclude) != bool:
                    raise ValueError(f"{exclude} is not a boolean value")
                self.bar_exclude = exclude
            else:
                self.bar_exclude = False
            if order := header.get("bar_order"):
                if self.bar_exclude:
                    raise ValueError("bar_order and bar_exclude are mutually exclusive")
                else:
                    self.bar_order = order
            else:
                self.bar_order = None
            if bar_title := header.get("bar_title"):
                if self.bar_exclude:
                    raise ValueError("bar_exclude is incompatible with bar_title")
                self.bar_title = bar_title
            else:
                self.bar_title = self.title
            if img := header.get("image_html"):
                self.image_html = img.strip()
            else:
                self.image_html = None
        except (yaml.scanner.ScannerError, ValueError) as e:
            e.args = f"Error parsing {filepath}", e.args[1:]
            raise
        except KeyError as e:
            e.args = f"{filepath} is missing a required field", e.args[1:]
            raise
        self.text = file_text[yaml_text.span()[1] :].strip()


def parse_args(arg_list):
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=False, default=None, type=Path)
    args = parser.parse_args(arg_list)
    if not args.files:
        args.files = list(Path("src").glob("*.md"))
    return args


def sort_pages(pages: List[Page]):
    homepage, rest = [], []
    for pg in pages:
        (rest, homepage)[pg.bar_title == "Home"].append(pg)
    if len(homepage) == 0:
        raise ValueError("No homepage provided")
    return homepage + sorted(
        rest,
        key=lambda pg: float(pg.bar_order)
        if pg.bar_order is not None
        else float("Inf"),
    )


def main():
    args = parse_args(sys.argv[1:])
    j2_env = Environment(
        loader=FileSystemLoader("."), autoescape=False, undefined=StrictUndefined
    )
    template = j2_env.get_template(TEMPLATE)
    pages = sort_pages([Page(fp) for fp in args.files])
    for pg in pages:
        with open(pg.filename, "w") as f:
            rendered = template.render(page=pg, pages=pages)
            f.write(rendered)


if __name__ == "__main__":
    main()
