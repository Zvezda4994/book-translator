# Book Translator 

Simple Python script to translate large `.txt` books or documents into any language using Google Translate (via the `deep_translator` library). Handles long files by splitting them into safe 4500-character chunks. 

---

## Overview

- Takes any `.txt` file, translates it to the target language.
- Outputs translated text to `book_translated.txt`
- Tweak and reuse as needed

---

## How to Use

1. Install requirements:
   ```bash
   pip install -r requirements.txt
2. Edit translate.py and set:
    input_file to your .txt file path
    targetlangcode to your desired language (eg: en, fr, hi)
3.  Run script
     ```bash
    python translate.py

## Possible troubleshooting
1. If after installing deep-translator it doesn't work in your IDE (eg: module not found, inexplicable path error):
    Open CMD and run it manually
   ```bash
    "[Python interpreter path]" "[Path to where script is stored]"
3. In doing so the file may be saved in the same folder as where your interpreter is (eg: C:/Windows/system32/book_translated.txt)
