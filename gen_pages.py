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
            header_data = yaml.load(yaml_text.group(1), Loader=yaml.Loader)
            self.title = header_data["title"]
            self.filename = Path(filepath).with_suffix(".html").name
            self.bar_title = header_data.get("bar_title", header_data["title"])
            if img := header_data.get("image_html"):
                self.image_html = img.strip()
            else:
                self.image_html = None
        except yaml.scanner.ScannerError as e:
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
    return homepage + sorted(rest, key=lambda p: p.bar_title)


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
