import os
from extract_changes import extract_changes
from extract_chinese import extract_chinese_paragraphs
from match_segments import match_segments
from apply_changes import apply_changes_to_chinese
from lxml import etree
import zipfile

def repack_docx(xml_dir, output_docx):
    with zipfile.ZipFile(output_docx, 'w') as docx:
        for foldername, subfolders, filenames in os.walk(xml_dir):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, xml_dir)
                docx.write(file_path, arcname)

def main():
    eng_docx = 'input_docs/english_updated.docx'
    chi_docx = 'input_docs/chinese_original.docx'
    output_docx = 'output_docs/chinese_updated.docx'
    eng_xml_dir = 'eng_xml'
    chi_xml_dir = 'chi_xml'

    # 1. Extract tracked changes from English
    changes = extract_changes(eng_docx, eng_xml_dir)

    # 2. Extract Chinese paragraphs
    chi_paras, chi_tree, ns = extract_chinese_paragraphs(chi_docx, chi_xml_dir)

    # 3. Align segments
    alignment = match_segments([c['para_idx'] for c in changes], list(range(len(chi_paras))))

    # 4. Apply changes to Chinese XML
    apply_changes_to_chinese(changes, chi_paras, alignment)

    # 5. Save and repack Chinese DOCX
    chi_tree.write(os.path.join(chi_xml_dir, 'word/document.xml'), xml_declaration=True, encoding='utf-8')
    repack_docx(chi_xml_dir, output_docx)

if __name__ == '__main__':
    main()
