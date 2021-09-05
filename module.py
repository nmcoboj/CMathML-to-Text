from preprocessor import PreProcessor
from language_generator1 import LanguageGenerator  # nueva función


class TexToES(object):

    def __init__(self, latex, cmathml, filename, verbose):
        """
        :param latex: String containing latex representation of math expression
        :param cmathml: String containing cmathml repr of math expression
        :param filename: Path to tex file
        :param verbose: True or False
        """
        self.latex = latex
        self.cmathml = cmathml
        self.filename = filename
        self.verbose = verbose

    def process_input(self,idioma):
        """
        Procesa el CMathMl.
        :return:
        """
        if self.cmathml:
            return self.__process_cmathml(self.cmathml, idioma)

    def __process_cmathml(self, mathml_string, idioma, logging=False):
        """
        Process cmathml string, It instantiates PreProcessor to generate the stack asociated to the CmathML input
        and then generates the transcripcions for every atomic-math-expression present in stack
        :param mathml_string: Cmathml string representation of math expresion
        :return:

        """
        print(" Proceso CMathMl")
        p = PreProcessor()

        stack_constructor = p.process(mathml_string)
        lg = LanguageGenerator()
        verb_generated = lg.generate_sub_language(stack_constructor, idioma, self.verbose)

        if self.verbose or logging:
            self.__output_logging(verb_generated)
        return verb_generated

    def __output_logging(self, verb_generated):
        pass