# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

def clean_processed_dir():
    base_dir = Path(r"C:\Users\DealnotWise5470\Documents\GitHub\cpe232-datamodel-2025\project\data_preparation\data\processed")
    
    # regex for headers
    # Example 2554:
    # หน้า ๑ \nเล่ม ๑๒๘ ตอนที่ ๑๓ ก \nราชกิจจานุเบกษา \n๔ มีนาคม ๒๕๕๔
    # Example 2564: 
    # ้หนา ๑\n่เลม ๑๓๘ ตอนที่ ๗๖ ก\nราชกิจจานุเบกษา\n๒๑ พฤศจิกายน ๒๕๖๔
    # Or const_2550: 
    # หน้า ๑\nเล่ม ๑๒๔ ตอนที่ ๔๗ ก\nราชกิจจานุเบกษา\n๒๔ สิงหาคม ๒๕๕๐
    
    header_pattern1 = re.compile(r"(?:หน้า|้หนา).*?\n.*?(?:เล่ม|่เลม).*?\n.*?ราชกิจจานุเบกษา.*?\n.*?๒๕\d{2}", re.MULTILINE)
    
    # Pattern for images or older docs:
    # `... ราชกิจจานุเบกษา เล่ม ...`
    header_pattern2 = re.compile(r"^.*?ราชกิจจานุเบกษา.*?$", re.MULTILINE)

    def _fix_sara_am(text):
        if not text: return text
        p = re.compile(r'([\u0E01-\u0E2E][\u0E48-\u0E4B]?)\s+(า)')
        return p.sub(lambda m: m.group(1) + '\u0E33', text)

    for p in base_dir.glob("const_*.json"):
        data = json.loads(p.read_text(encoding="utf-8"))
        changed = False
        
        # fix pages
        if "pages" in data:
            for page in data["pages"]:
                for key in ["cleaned_text", "raw_markdown", "raw_text"]:
                    if key in page and page[key]:
                        original = page[key]
                        
                        # Fix sara am
                        text = _fix_sara_am(original)
                        # Fix words split by spaces (from buggy font) completely
                        text = text.replace("จ านวน", "จำนวน")
                        text = text.replace("ส าหรับ", "สำหรับ")
                        text = text.replace("อ านาจ", "อำนาจ")
                        text = text.replace("ก าหนด", "กำหนด")
                        text = text.replace("ส าคัญ", "สำคัญ")
                        text = text.replace("ต าแหน่ง", "ตำแหน่ง")
                        text = text.replace("ค านวณ", "คำนวณ")
                        text = text.replace("ด าเนินการ", "ดำเนินการ")
                        
                        # Remove header
                        text = header_pattern1.sub("", text)
                        
                        # Also strip leading newlines/spaces
                        text = text.strip()
                        
                        if text != original:
                            page[key] = text
                            changed = True

        if "full_text" in data and data["full_text"]:
            original = data["full_text"]
            text = _fix_sara_am(original)
            text = text.replace("จ านวน", "จำนวน")
            text = text.replace("ส าหรับ", "สำหรับ")
            text = text.replace("อ านาจ", "อำนาจ")
            text = text.replace("ก าหนด", "กำหนด")
            text = text.replace("ส าคัญ", "สำคัญ")
            text = text.replace("ต าแหน่ง", "ตำแหน่ง")
            text = text.replace("ค านวณ", "คำนวณ")
            text = text.replace("ด าเนินการ", "ดำเนินการ")
            
            text = header_pattern1.sub("", text)
            
            if text != original:
                data["full_text"] = text
                changed = True
                
        if changed:
            p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"Fixed {p.name}")

if __name__ == '__main__':
    clean_processed_dir()
