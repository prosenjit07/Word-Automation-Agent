from utils.xml_helpers import insert_ins_tag, insert_del_tag

def apply_changes_to_chinese(changes, chi_paras, alignment):
    for change in changes:
        eng_idx = change['para_idx']
        # Find corresponding Chinese paragraph index
        chi_idx = next((c for e, c in alignment if e == eng_idx), None)
        if chi_idx is not None and chi_idx < len(chi_paras):
            if change['type'] == 'ins':
                insert_ins_tag(chi_paras[chi_idx])
            elif change['type'] == 'del':
                insert_del_tag(chi_paras[chi_idx]) 