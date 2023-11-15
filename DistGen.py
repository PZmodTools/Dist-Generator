import argparse
from datetime import datetime

def read_lines_from_file(file_path):
    """Reads lines from a file and returns them as a list."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def generate_lua_code(mod_id, item_names, locations, default_weight=1):
    """Generates Lua code for each item-location combination."""
    lua_lines = []
    for location in locations:
        for item in item_names:
            lua_lines.append(f"table.insert(ProceduralDistributions['list']['{location}'].items, '{mod_id}.{item}');")
            lua_lines.append(f"table.insert(ProceduralDistributions['list']['{location}'].items, {default_weight});")
    return lua_lines

def write_output_file(lua_lines, output_file):
    """Writes the generated Lua code to the specified output file."""
    with open(output_file, 'w') as file:
        file.write("require 'Items/ProceduralDistributions'\n\n")
        for line in lua_lines:
            file.write(line + "\n")

def main():
    parser = argparse.ArgumentParser(description="Generate Lua code for game modding.")
    parser.add_argument("-modid", "--modid", required=True, help="Mod ID")
    parser.add_argument("-items", "--items", help="Comma-separated list of item names")
    parser.add_argument("-itemsFile", "--itemsFile", help="File containing item names")
    parser.add_argument("-loc", "--locations", help="Comma-separated list of location names")
    parser.add_argument("-locFile", "--locationsFile", help="File containing location names")
    parser.add_argument("-out", "--output", help="Output file name")

    args = parser.parse_args()

    # Read items and locations from files or arguments
    item_names = read_lines_from_file(args.itemsFile) if args.itemsFile else args.items.split(',')
    locations = read_lines_from_file(args.locationsFile) if args.locationsFile else args.locations.split(',')

    # Generate Lua code
    lua_code = generate_lua_code(args.modid, item_names, locations)

    # Determine output file name
    output_file = args.output or f"distributions_{datetime.now().strftime('%m%d%H%M')}.txt"

    # Write output file
    write_output_file(lua_code, output_file)

    print(f"Lua code generated and saved to {output_file}")

if __name__ == "__main__":
    main()
