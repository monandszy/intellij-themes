import xml.etree.ElementTree as ET
import argparse
import sys

# Define your color map here.
# The keys are the color names used as placeholders in the XML file,
# and the values are the hex color codes you want to substitute.
STYLE_MAP = {
  "scrollbarTrack": "000000",
  "scrollbarThumb": "252525",
  "scrollbarThumbHover": "252525",
  "htmlTree0": "ed6b88",
  "htmlTree1": "f9d778",
  "htmlTree2": "b4da82",
  "htmlTree3": "57d1eb",
  "htmlTree4": "78dce8",
  "htmlTree5": "b6b3eb",
  "vcsAnnotation1": "232d28",
  "vcsAnnotation2": "2d2323",
  "vcsAnnotation3": "23282d",
  "vcsAnnotation4": "2d232d",
  "vcsAnnotation5": "2d2d23",
  "mainBackground": "000000",
  "caretRowBackground": "151515",
  "selectionBackground": "252500",
  "highlightBackground": "252525",
  "hoverBackground": "151515",
  "imageCheckerboard": "353535",
  "errorHintBackground": "400000",
  "warningHintBackground": "404000",
  "accentColor": "b4b400",
  "foreground": "c1c100",
  "guideColor": "6c6c00",
  "borderColor": "6c6c00",
  "vcsAdded": "b4b400",
  "vcsModified": "de7400",
  "vcsDeleted": "aa0000",
  "vcsUnknown": "bc2500",
  "vcsIgnored": "6c6c00",
  "vcsMergeConflict": "aa0000",
  "linesAdded": "b4b400",    
  "linesModified": "de7400", 
  "linesDeleted": "aa0000",  
  "errorColor": "e8100",
  "warningColor": "de7400",
  "mainfg": "bbbbbb",
  "builtin": "AD00DE",
  "keyword": "FF8800",
  "string": "7B4019",
  "functioNname": "AD00DE",
  "variable": "FFC900",
  "type": "FF8800",
  "constant": "FFC900",
  "comment": "5C120E  ",
}

def replace_color_placeholders(input_file, output_file):
  try:
    tree = ET.parse(input_file)
    root = tree.getroot()

    replacements_made = 0

    for option_element in root.findall('.//option[@value]'):
      original_value = option_element.get('value', '')

      if original_value.startswith('{') and original_value.endswith('}'):
        color_name = original_value.strip('{}')

        if color_name in STYLE_MAP:
          hex_value = STYLE_MAP[color_name]
          option_element.set('value', hex_value)
          replacements_made += 1
          print(f"Replaced '{original_value}' with '{hex_value}'")
        else:
          print(f"Warning: Color name '{color_name}' not found in the color map. Skipping.", file=sys.stderr)

    tree.write(output_file, encoding='UTF-8', xml_declaration=True)

    print(f"\nSuccessfully processed the file.")
    print(f"Total replacements made: {replacements_made}")
    print(f"Modified XML saved to: {output_file}")

  except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.", file=sys.stderr)
    sys.exit(1)
  except ET.ParseError:
    print(f"Error: The file '{input_file}' is not a valid XML file.", file=sys.stderr)
    sys.exit(1)
  except Exception as e:
    print(f"An unexpected error occurred: {e}", file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
  input_file = "./SunLikeTemplate.xml"
  output_file = "./theme/SunLike.xml"
  replace_color_placeholders(input_file, output_file)