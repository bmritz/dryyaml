# -*- coding: utf-8 -*-

"""Main module."""

from io import StringIO
from jinja2 import Template
import yaml


def render(fil, context=None):
    """Render the DryYAML file as vanilla YAML.

    Args:
        fil (file-like): DryYAML file to render.

    """
    prev_lines_rendered = ''
    context = context if context is not None else {}

    for line in fil:
        prev_lines = prev_lines_rendered + line
        prev_lines_rendered = Template(prev_lines, keep_trailing_newline=True).render(context)
        context = yaml.load(prev_lines_rendered)
    return prev_lines_rendered
