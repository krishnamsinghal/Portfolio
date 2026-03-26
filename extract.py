import zipfile
import xml.etree.ElementTree as ET

def get_docx_text(path):
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = ET.XML(xml_content)
    paragraphs = []
    for node in tree.iter():
        if node.tag.endswith('}p'):
            texts = [t.text for t in node.iter() if t.tag.endswith('}t') and t.text]
            if texts:
                paragraphs.append(''.join(texts))
    return '\n'.join(paragraphs)

text = get_docx_text("Specialized CV Krishnam.docx")
with open("cv_extracted.txt", "w", encoding="utf-8") as f:
    f.write(text)
print("Extracted successfully.")
