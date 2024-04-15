import re

def parse_latex(latex_text):
    # Define regular expressions for various LaTeX constructs
    regexes = {
        'command': r'\\([a-zA-Z]+)(?:\[([^\[\]]*)\])?(?:\{([^\{\}]*)\})?',
        'math_env': r'(\$[^\$]*\$)',
        'comment': r'(%.*?\n)',
        'escaped_char': r'(\\.?)',
        'text': r'([^\\\$%\{\}\[\]]+|\\[\s\S])',
    }

    parsed_latex = []

    # Iterate over matches in the text
    for match in re.finditer('|'.join(regexes.values()), latex_text):
        for group_name, group in zip(regexes.keys(), match.groups()):
            if group is not None:
                parsed_latex.append((group_name, group))

    return parsed_latex

def convert_to_texit(parsed_latex):
    texit_commands = []
    current_command = None
    current_args = []

    for token_type, token_value in parsed_latex:
        if token_type == 'command':
            if current_command is not None:
                if current_args:
                    texit_commands.append((current_command, tuple(current_args)))
                else:
                    texit_commands.append((current_command, ()))
            current_command = token_value
            current_args = []
        elif token_type in ['braces', 'square_brackets']:
            current_args.append(token_value)
        elif token_type == 'text':
            current_args.append(token_value)

    if current_command is not None:
        if current_args:
            texit_commands.append((current_command, tuple(current_args)))
        else:
            texit_commands.append((current_command, ()))

    return texit_commands

# Example usage
latex_text = r'''
\documentclass[a4paper,12pt]{article}
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
hello world121212123123123123
\end{document}
'''

parsed = parse_latex(latex_text)
converted = convert_to_texit(parsed)
for item in converted:
    print(item)
