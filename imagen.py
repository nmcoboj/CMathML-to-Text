import os
from lxml import etree
from sympy import preview


def mathml2latex_yarosh(equation):
    """ MathML to LaTeX conversion with XSLT from Vasil Yaroshevich """
    xslt_file = os.path.join('mathconverter', 'xsl_yarosh', 'mmltex.xsl')
    dom = etree.fromstring(equation)
    xslt = etree.parse(xslt_file)
    transform = etree.XSLT(xslt)
    newdom = transform(dom)
    return str(newdom)


def mathmltopgn(archivo):
    aux = ''
    au= ''
    with open(archivo, 'r+') as f:
        for line in f.readlines():
            aux = aux + line.rstrip('\n')
        au=aux.replace('<math>','<math xmlns="http://www.w3.org/1998/Math/MathML">')

    tex = mathml2latex_yarosh(au)
    """print(tex)"""
    preview(r'%s' % tex, viewer='file', filename='Imagen.png', euler=False)
    return tex