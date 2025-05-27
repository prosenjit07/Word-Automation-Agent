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

def find_tracked_changes(paragraphs, ns):
    changes = []
    for idx, p in enumerate(paragraphs):
        # Check for direct ins/del tags
        for ins in p.xpath('.//w:ins', namespaces=ns):
            changes.append({'type': 'ins', 'para_idx': idx, 'xml': etree.tostring(ins)})
        for dele in p.xpath('.//w:del', namespaces=ns):
            changes.append({'type': 'del', 'para_idx': idx, 'xml': etree.tostring(dele)})
            
        # Check for revision markup
        for run in p.xpath('.//w:r', namespaces=ns):
            revision = run.xpath('.//w:revision', namespaces=ns)
            if revision:
                rev_type = revision[0].get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}type')
                if rev_type in ['ins', 'del']:
                    changes.append({
                        'type': rev_type,
                        'para_idx': idx,
                        'xml': etree.tostring(run)
                    })
    return changes

def extract_changes(eng_docx_path, extract_dir):
    extract_docx_xml(eng_docx_path, extract_dir)
    paras, tree, ns = get_paragraphs_from_xml(os.path.join(extract_dir, 'word/document.xml'))
    return find_tracked_changes(paras, ns) 