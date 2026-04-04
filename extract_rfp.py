import zipfile
import xml.etree.ElementTree as ET
import sys

def extract_text_from_docx(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as zf:
            xml_content = zf.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            
            # The namespace dictionary
            namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            # Find all <w:p> elements (paragraphs)
            paragraphs = tree.findall('.//w:p', namespaces)
            
            text_lines = []
            for p in paragraphs:
                # Find all <w:t> elements (text runs) within the paragraph
                texts = [node.text for node in p.findall('.//w:t', namespaces) if node.text]
                if texts:
                    text_lines.append(''.join(texts))
            
            return '\n'.join(text_lines)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    text = extract_text_from_docx(r'c:\commandcenter\07_Product Academy\02_Course_Hub\Mobio_course_AI3day\drive-download-20260402T031340Z-3-001\PD - Use case Phản hồi RFP.docx')
    with open(r'c:\commandcenter\07_Product Academy\02_Course_Hub\Mobio_course_AI3day\tmp_rfp.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Done")
