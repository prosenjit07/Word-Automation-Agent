# WordAutomation

Automatically transfer tracked changes from an English Word document to its Chinese translation, preserving Microsoft Word's Track Changes formatting.

## Features
- Extracts insertions and deletions (tracked changes) from an English `.docx` file
- Aligns English and Chinese paragraphs (1-to-1 by default)
- Applies the same tracked changes to the Chinese `.docx`, preserving revision marks
- Fully automated and modular workflow

## Folder Structure
```
word_automation_app/
├── main.py
├── requirements.txt
├── extract_changes.py
├── extract_chinese.py
├── match_segments.py
├── apply_changes.py
├── utils/
│   └── xml_helpers.py
├── input_docs/
│   ├── english_updated.docx
│   └── chinese_original.docx
├── output_docs/
│   └── chinese_updated.docx
```

## Setup
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Prepare input files:**
   - Place your English DOCX with tracked changes in `input_docs/english_updated.docx`
   - Place the original Chinese translation in `input_docs/chinese_original.docx`

## Usage
Run the main script:
```bash
python main.py
```
- The output will be saved as `output_docs/chinese_updated.docx` with visible tracked changes.

## How It Works
- Extracts tracked changes from the English document using XML parsing
- Extracts paragraphs from the Chinese document
- Aligns paragraphs (by index)
- Applies the same tracked changes to the Chinese document by inserting `<w:ins>` and `<w:del>` tags
- Repackages the modified XML as a new DOCX

## Limitations
- Only supports 1-to-1 paragraph alignment (no fuzzy matching yet)
- Inserts placeholder text for changes in Chinese (not the actual translated content)
- Does not handle complex formatting or nested changes

## Future Improvements
- Fuzzy matching for better segment alignment
- Copy actual changed content (not just placeholders)
- Improved error handling and logging
- User interface (CLI or web)

## License
MIT 