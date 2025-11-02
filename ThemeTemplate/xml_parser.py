import xml.etree.ElementTree as ET
import argparse
import sys

# Define your color map here.
# The keys are the color names used as placeholders in the XML file,
# and the values are the hex color codes you want to substitute.
STYLE_MAP = {
  "scrollbarTrack": "",
  "scrollbarThumb": "",
  "scrollbarThumbHover": "",
  "htmlTree0": "",
  "htmlTree1": "",
  "htmlTree2": "",
  "htmlTree3": "",
  "htmlTree4": "",
  "htmlTree5": "",
  "vcsAnnotation1": "",
  "vcsAnnotation2": "",
  "vcsAnnotation3": "",
  "vcsAnnotation4": "",
  "vcsAnnotation5": "",
  "mainBackground": "",
  "caretRowBackground": "",
  "selectionBackground": "",
  "highlightBackground": "",
  "hoverBackground": "",
  "imageCheckerboard": "",
  "errorHintBackground": "",
  "warningHintBackground": "",
  "vcsMergeConflict": "",
  "accentColor": "",
  "foreground": "",
  "guideColor": "",
  "borderColor": "",
  "vcsAdded": "",
  "vcsModified": "",
  "vcsDeleted": "",
  "vcsUnknown": "",
  "vcsIgnored": "",
  "errorColor": "",
  "warningColor": "",
  "mainfg": "",
  "builtin": "",
  "keyword": "",
  "string": "",
  "functioNname": "",
  "variable": "",
  "type": "",
  "constant": "",
  "comment": "",
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
  input_file = "./ThemeTemplate.xml"
  output_file = "./theme/Theme.xml"
  replace_color_placeholders(input_file, output_file)