"""
Convert notebooks to slides
"""
import argparse
import sys
from pathlib import Path
from textwrap import dedent

from lxml import html
import nbformat
from pypandoc import convert_text
from nbconvert.exporters.markdown import MarkdownExporter
from traitlets import default


def parse_args(args=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebook", type=Path)
    return parser.parse_args(args)


class HeaderExporter(MarkdownExporter):
    @default('template_file')
    def _template_file_default(self):
        return 'headers_template'

    @property
    def template_path(self):
        return super().template_path + ['.']


def exercise(src):
    # import pdb; pdb.set_trace()
    d, p, *_ = html.fragments_fromstring(src)

    # title = d.attrib['data-title']
    title = d.find('h1').text_content().strip().replace("Exercise: ", "")
    question = convert_text(p.text, "latex", format="markdown")
    tpl = dedent('''\

    ---

    \\begin{{Exercise}}[title={{{title}}}]
    {question}
    \\end{{Exercise}}
    ''').format(title=title, question=question)

    return tpl


def convert(notebook):
    nb = nbformat.read(str(notebook), 4)
    exporter = HeaderExporter()
    exporter.environment.filters['exercise'] = exercise
    body, resc = exporter.from_notebook_node(nb)
    out = Path("markdown").joinpath(notebook.with_suffix(".md").name)
    with open(out, 'w') as f:
        f.write(body)


def main(args=None):
    args = parse_args(args)
    convert(args.notebook)


if __name__ == '__main__':
    sys.exit(main())
