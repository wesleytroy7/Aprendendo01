# from xml.dom import minidom # importa o modulo para leitura de arquivos xml
# nome_do_arquivo_xml='ar.xml' # nome do arquivo importado
# documento_xml=minidom.parse(nome_do_arquivo_xml)# instancia o obj
from xml.etree import ElementTree as ELMT
XML01='ar.xml'
doc=ELMT.parse(XML01)
doc