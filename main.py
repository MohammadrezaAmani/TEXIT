from texit import startex
from texit.elements import *

tex = startex(
    documentclass("article",args=["a4paper","12pt"]),
    usepackage("geometry"),
    begin("document"),
    section("Hello World"),
    subsection("Hello World"),
    subsubsection("Hello World"),
    paragraph("Hello World"),
    subparagraph("Hello World"),
    newpage(),
    hspace("1cm"),
    vspace("1cm"),
    hline(),
    "hello world",
    end("document"),
)

print(tex)
