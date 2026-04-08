import json
from pathlib import Path

def fix_pua(text):
    if not text: return ""
    pua_map = {
        0xF700: 0x0E31, 0xF701: 0x0E34, 0xF702: 0x0E35, 0xF703: 0x0E36, 0xF704: 0x0E37,
        0xF705: 0x0E48, 0xF706: 0x0E49, 0xF707: 0x0E4A, 0xF708: 0x0E4B, 0xF709: 0x0E4C,
        0xF70A: 0x0E48, 0xF70B: 0x0E49, 0xF70C: 0x0E4A, 0xF70D: 0x0E4B, 0xF70E: 0x0E4C,
        0xF70F: 0x0E47, 0xF710: 0x0E31, 0xF711: 0x0E47, 0xF712: 0x0E47, 0xF713: 0x0E48,
        0xF714: 0x0E49, 0xF715: 0x0E4A, 0xF716: 0x0E4B, 0xF717: 0x0E4C, 0xF718: 0x0E38,
        0xF719: 0x0E39, 0xF71A: 0x0E3A,
    }
    return text.translate(pua_map)

processed_dir = Path("data/processed")
for file in processed_dir.glob("*.json"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        modified = False
        
        # Merge text fields into one clean "text" and fix PUA
        for page in data.get("pages", []):
            if "cleaned_text" in page or "raw_text" in page or "raw_markdown" in page:
                modified = True
                # Get the best available text
                t = page.get("cleaned_text", page.get("raw_text", page.get("raw_markdown", "")))
                
                # Clean up old keys
                page.pop("cleaned_text", None)
                page.pop("raw_text", None)
                page.pop("raw_markdown", None)
                
                # Apply PUA fix
                page["text"] = fix_pua(t)
                
        # Also clean up the full text
        if "full_text" in data:
            data["full_text"] = fix_pua(data["full_text"])
            modified = True
                
        if modified:
            with open(file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Fixed formatting and characters: {file.name}")
            
    except Exception as e:
        print(f"Error processing {file.name}: {e}")

print("Done processing existing JSON files.")
