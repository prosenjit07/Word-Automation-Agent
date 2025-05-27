from fuzzywuzzy import fuzz
from lxml import etree

def match_segments(eng_paras, chi_paras, threshold=60):
    """
    Align English and Chinese paragraphs using fuzzy matching.
    Returns a list of (eng_idx, chi_idx) tuples.
    """
    eng_texts = [etree.tostring(p, encoding='unicode', method='text') for p in eng_paras]
    chi_texts = [etree.tostring(p, encoding='unicode', method='text') for p in chi_paras]
    matches = []
    used_chi = set()
    for i, eng in enumerate(eng_texts):
        best_score = 0
        best_j = None
        for j, chi in enumerate(chi_texts):
            if j in used_chi:
                continue
            score = fuzz.partial_ratio(eng, chi)
            if score > best_score:
                best_score = score
                best_j = j
        if best_j is not None and best_score >= threshold:
            matches.append((i, best_j))
            used_chi.add(best_j)
    return matches 