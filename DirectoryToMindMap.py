import os
import xml.etree.ElementTree as ET


def create_mindmap_from_directory(root_dir, output_file):
    def add_node(parent, name):
        node = ET.SubElement(parent, "node")
        node.set("TEXT", name)
        return node

    def build_tree(current_dir, parent_node):
        entries = os.listdir(current_dir)
        for entry in sorted(entries):
            entry_path = os.path.join(current_dir, entry)
            if os.path.isdir(entry_path):
                sub_node = add_node(parent_node, entry)
                build_tree(entry_path, sub_node)
            elif os.path.isfile(entry_path):
                add_node(parent_node, entry)

    # Create the root of the mindmap
    map_element = ET.Element("map")
    map_element.set("version", "0.9.0")

    root_node = add_node(map_element, os.path.basename(root_dir) or "Root")

    # Build the mindmap tree
    build_tree(root_dir, root_node)

    # Write to file
    tree = ET.ElementTree(map_element)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    root_directory = os.getcwd()  # 当前文件夹
    output_filename = "mindmap_gen.mm"  # 输出文件名

    create_mindmap_from_directory(root_directory, output_filename)
    print(f"Mindmap saved to {output_filename}")