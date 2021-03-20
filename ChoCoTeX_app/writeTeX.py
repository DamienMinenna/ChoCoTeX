
def writeuser_tex(text_tex,env):

    if env == 1:
        text_file = open("latex/user_eq.tex", "w")
        text_file.write(r"\begin{align*}")
        text_file.write("\n")
        text_file.write(r"%s" % text_tex)
        text_file.write("\n")
        text_file.write(r"\end{align*}")
        text_file.close()
    elif env == 2:
        text_file = open("latex/user_eq.tex", "w")
        text_file.write(r"\begin{equation*}")
        text_file.write("\n")
        text_file.write(r"%s" % text_tex)
        text_file.write("\n")
        text_file.write(r"\end{equation*}")
        text_file.close()
    elif env == 3:
        text_file = open("latex/user_eq.tex", "w")
        text_file.write(r"$ %s $" % text_tex)
        text_file.close()
    elif env == 4:
        text_file = open("latex/user_eq.tex", "w")
        text_file.write(r"%s" % text_tex)
        text_file.close()

def writeuser_cmd(fontsize,color):
    text_file = open(r"latex/user_cmd.tex", "w")
    text_file.write(r"\def\myfontsize{%s}" % str(fontsize))
    text_file.write("\n")
    text_file.write(r"\def\myfontsizeplus{%s}" % str(float(fontsize)+5))
    text_file.write("\n")
    text_file.write(r"\definecolor{mycolor}{HTML}{%s}" % color[1:])
    text_file.close()
