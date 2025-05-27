def match_segments(eng_paras, chi_paras):
    # Simple 1-to-1 index-based alignment
    return [(i, i) for i in range(min(len(eng_paras), len(chi_paras)))] 