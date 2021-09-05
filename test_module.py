import unittest
from mathml_client import SnuggleTexClient


def suite():

    snuggletex = SnuggleTexClient()
    tex_form = ' x + y + \cot z'
    mathml = snuggletex.latex_to_mathml(tex_form)
    print(mathml)



if __name__ == '__main__':
    suite()
