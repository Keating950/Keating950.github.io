#!/usr/bin/env python3

import argparse
from typing import List
import urllib.parse
from jinja2 import Environment, FileSystemLoader, select_autoescape


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "page_title",
            metavar="page_title",
            type=str,
            nargs=1,
            help="Title of page to be created.",
        )
    parser.add_argument(
            "text",
            metavar="text",
            type=str,
            nargs=1,
            help="Path to file containing the page's text content.",
         )
    parser.add_argument(
            "--url",
            metavar="url",
            type=str,
            nargs=1,
            default=None,
            help="Page url. Defaults to keating950.github.io/[post_title].html.",
        )
    parser.add_argument(
            "--navbar_title",
            metavar="navbar_title",
            type=str,
            nargs=1,
            default=None,
            help="Title to be displayed in the navbar.",
        )
    parser.add_argument(
            "--img_url",
            metavar='img_title',
            type=str,
            nargs=1,
            default=None,
            help="URL of main image to be displayed on the page.",
        )
    arg_namespace = parser.parse_args()
    arg_dict = dict(vars(args))
    if arg_dict["navbar_title"] is None:
        arg_dict["navbar_title"] = arg_dict["page_title"]
    if arg_dict["url"] is None:
        arg_dict["url"] = urllib.parse.quote(f"Keating950.github.io/{arg_dict['page_title']}.html")
    else:
        arg_dict["url"] = urllib.parse.quote(arg_dict["url"])
    return arg_dict

def load_paragraphs(fp) -> List[List[str]]:
    f = open(fp, "r")
    paragraphs = []
    tmp_p =[]
    for line in f.readlines():
        if line.endswith("\n"):
            paragraphs.append(tmp_p)
            tmp_p = [line]
        else:
            tmp_p.append(line)
    f.close()
    return paragraphs

if __name__ == "__main__":
    args = parse_args()
    paragraphs = load_paragraphs(args["text"])
    env = Environment(
        loader=FileSystemLoader("templates/"),
        autoescape=select_autoescape(["html", "xml"])
    )
    template = env.get_template("post_template.html")
    page = template.render(args)
    with open(f"args['page_title'].html", "wb") as f:
        f.write(output_from_parsed_template)

