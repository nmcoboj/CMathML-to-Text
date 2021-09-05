from module import TexToES
from win32com.client import Dispatch


class CMathML2Txt(object):

    def __init__(self):
        self.msg = 'Inicio del proceso'  # Inicializa impresión (1)
        self.input = ''                  # Inicializa entrada
        self.output = ''                 # Inicializa salida

    def runcmath2txt(self, idioma):

        """
        :param idioma:
        :param input: Representación en cadena de una expresión matemática en CMathMl

        """
        print(self.msg)  # Imprime inicializacion anterior (1)
        a = TexToES(latex=None, cmathml=self.input, verbose=False, filename=None)  # Guarda función de otro programa en una variable
        self.output = a.process_input(idioma)
        print("Proceso Finalizado")
        print("salida=" + self.output)

        """
        Generación de audio

        """
        s = Dispatch("SAPI.SpVoice")
        s.Speak(self.output)

    def read_file_Mathml(self, filename):
        """
        Leer el archivo que contiene el código de la fórmula en CMathML

        """
        self.__input_logging("Archivo", filename)
        aux = ''
        with open(filename, 'r+') as f:
            for line in f.readlines():
                aux = aux + line.rstrip('\n')
        self.input = aux
        print(aux)

    def __input_logging(self, msg, input):
        print("++++++++++ Procesando %s ++++++++++" % msg)
        print("%s recibido:\n%s\n" % (msg, input))


if __name__ == '__main__':
    b = CMathML2Txt()
    filein = 'ejemplo6.html'
    b.read_file_Mathml(filein)
    idioma = 'Español.template'
    b.runcmath2txt(idioma)