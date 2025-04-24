
from deep_translator import GoogleTranslator
from pathlib import Path

# input file path
input_file = r"C:\Users\[YOURNAME]\path\to\your\file.txt"  # Change this to where your file is stored

output_file = "book_translated.txt"
chunk_size = 4500  # Google Translate maxes out around 5000 characters per 

# read the text type shi 
text = Path(input_file).read_text(encoding="utf-8")

# split into chunks (Google usually only translate around 5000 characters at a time)
# but we will use 4500 to be safe
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Translate each chunk
translated_chunks = []
for i, chunk in enumerate(chunks):
    print(f"Translating chunk {i+1}/{len(chunks)}...")
    translated = GoogleTranslator(source='auto', target='[targetlangcode (eg: en, fr, hi)]').translate(chunk)
    translated_chunks.append(translated)

# write to file
with open(output_file, "w", encoding="utf-8") as f:
    for part in translated_chunks:
        f.write(part + "\n\n")

print("✅ Translation complete! Check the file:", output_file)
