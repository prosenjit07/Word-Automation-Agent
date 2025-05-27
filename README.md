# Word Document Automation

This application helps synchronize changes between English and Chinese Word documents.

## Setup

1. Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Input Requirements

Place your input files in the `input_docs` directory:

1. `english_updated.docx`: The English document with tracked changes
   - Must be a Word document (.docx)
   - Should contain tracked changes (revisions) that you want to apply to the Chinese version

2. `chinese_original.docx`: The original Chinese document
   - Must be a Word document (.docx)
   - Should be the base document that will be updated with changes

## Running the Application

1. Ensure your input files are in place:
   ```
   input_docs/
   ├── english_updated.docx
   └── chinese_original.docx
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. The updated Chinese document will be generated in:
   ```
   output_docs/chinese_updated.docx
   ```

## Directory Structure

- `input_docs/`: Place your input Word documents here
- `output_docs/`: Generated output files will appear here
- `eng_xml/`: Temporary directory for English document XML (automatically created)
- `chi_xml/`: Temporary directory for Chinese document XML (automatically created)

## Notes

- Make sure to enable "Track Changes" in your English document before making edits
- The application uses fuzzy matching to align segments between English and Chinese
- Temporary XML files are generated during processing and can be safely deleted

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

## How It Works
- Extracts tracked changes from the English document using XML parsing
- Extracts paragraphs from the Chinese document
- Aligns paragraphs (by index)
- Applies the same tracked changes to the Chinese document by inserting `<w:ins>` and `<w:del>` tags
- Repackages the modified XML as a new DOCX

## Tracking
![image](https://github.com/user-attachments/assets/3e4e19ee-c818-4a3a-94e8-a8a2b42449e8)


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
