import sys
import chardet

def convert_to_utf8(input_file, output_file):
    # Lire le fichier en mode binaire pour détecter l'encodage
    with open(input_file, 'rb') as f:
        raw_data = f.read()

    # Détection automatique de l'encodage (latin-1, windows-1252, etc.)
    result = chardet.detect(raw_data)
    source_encoding = result['encoding']
    print(f"[INFO] Encodage détecté : {source_encoding}")

    if source_encoding is None:
        print("[ERREUR] Impossible de détecter l'encodage.")
        return

    # Lire avec l'encodage détecté et réécrire en UTF-8
    with open(input_file, 'r', encoding=source_encoding, errors='ignore') as f:
        content = f.read()

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"[OK] Fichier converti en UTF-8 : {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_utf8.py <input.csv> <output.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_to_utf8(input_file, output_file)
