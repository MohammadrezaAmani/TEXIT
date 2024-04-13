from texit import startex
from texit.elements import (Begin, Documentclass, End, Hline, Hspace, Newpage,
                            Paragraph, Section, Subparagraph, Subsection,
                            Subsubsection, Usepackage, Vspace)

tex = startex(
    Documentclass("article"),
    Usepackage("geometry"),
    Begin("document"),
    Section("Hello World"),
    Subsection("Hello World"),
    Subsubsection("Hello World"),
    Paragraph("Hello World"),
    Subparagraph("Hello World"),
    Newpage(),
    Hspace("1cm"),
    Vspace("1cm"),
    Hline(),
    "hello world",
    End("document"),
)

print(tex)
