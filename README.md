# TEXIT

<p align="center">
    <a>
        <img src="assets/images/texit-logo-9380b138.jpg" alt="TEXIT" width="256">
    </a>
    <br>
    <b>Write LaTeX in Python with Ease</b>
    <br>
    <a href="https://github.com/MohammadrezaAmani/TEXIT">
        GitHub
    </a>
    •
    <a href="#">
        Documentation
    </a>
    •
    <a href="https://t.me/Mohammadreza_Amani">
        Channel
    </a>
    •
    <a href="mailto:more.amani@yahoo.com">
        Support
    </a>
</p>

<br>

## Introduction

**TEXIT** is a Python module that simplifies writing LaTeX code in Python scripts. It provides a convenient way to generate LaTeX documents programmatically, making it easier to incorporate LaTeX functionality into Python projects.

## Requirements

### **Python Compatibility**

TEXIT is compatible with Python 3.x. While older versions may work, it's recommended to use Python 3 for full compatibility and support.

## How to Use?

> For detailed usage instructions, refer to the [documentation](https://github.com/MohammadrezaAmani/TEXIT).

### Installation

You can install TEXIT via pip:

```bash
pip install texit
```

### Syntax

The syntax of TEXIT module is straightforward. You can create LaTeX documents using Python code, similar to the way you would construct HTML with libraries like BeautifulSoup. Here's a simple example:

```python
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
```

output:

```tex
    \documentclass{article}
    \usepackage{geometry}
    \begin{document}
    \section{Hello World}
    \subsection{Hello World}
    \subsubsection{Hello World}
    \paragraph{Hello World}
    \subparagraph{Hello World}
    \newpage
    \hspace{1cm}
    \vspace{1cm}
    \hline
    hello world
    \end{document}
```

## Supported Features

TEXIT supports various LaTeX elements and features, allowing you to create complex documents easily. Some of the supported features include:

* Equations
* Sections and Subsections
* Tables
* Figures
* Lists
* References
* And more...

For a full list of supported features and usage examples, please refer to the documentation.

## License

TEXIT is distributed under the MIT License. See `LICENSE` for more information.
