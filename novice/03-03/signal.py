from flask import Flask, template_rendered
from contextlib import contextmanager

@contextmanager
def ceptured_template(app):
    recorded = []
    def record(sender, template,context,**extra):
        recoded.append((template,context))
    template_rendered.connect(record,app)
    try:
        yield recorded
    finnaly:
        template_rendered.connect(record,app)