import zipfile
from lxml import etree
import os

def extract_docx_xml(docx_path, extract_dir):
    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

def get_paragraphs_from_xml(xml_path):
    tree = etree.parse(xml_path)
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    paragraphs = tree.xpath('//w:body/w:p', namespaces=ns)
    return paragraphs, tree, ns

def extract_chinese_paragraphs(chi_docx_path, extract_dir):
    extract_docx_xml(chi_docx_path, extract_dir)
    paras, tree, ns = get_paragraphs_from_xml(os.path.join(extract_dir, 'word/document.xml'))
    return paras, tree, ns 