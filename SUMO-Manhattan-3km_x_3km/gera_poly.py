import xml.etree.ElementTree as ET

def gerar_poly_a_partir_da_rede(net_path, output_path, tamanho_poly=200):
    tree = ET.parse(net_path)
    root = tree.getroot()

    poly_root = ET.Element("additional")
    half = tamanho_poly / 2
    id_count = 0

    for junction in root.findall("junction"):
        if junction.get("type") == "internal":
            continue  # Ignora nós internos

        x = float(junction.get("x"))
        y = float(junction.get("y"))

        # Define os 4 vértices do polígono 200x200 centrado no nó
        x0 = x - half
        y0 = y - half
        x1 = x + half
        y1 = y + half

        shape = f"{x0},{y0} {x1},{y0} {x1},{y1} {x0},{y1}"
        ET.SubElement(poly_root, "poly", {
            "id": f"j{id_count}",
            "type": "nodeBox",
            "color": "255,0,0",
            "layer": "0",
            "shape": shape
        })
        id_count += 1

    poly_tree = ET.ElementTree(poly_root)
    poly_tree.write(output_path, encoding="UTF-8", xml_declaration=True)
    print(f"Gerado {id_count} polígonos no arquivo '{output_path}'.")

# Exemplo de uso
gerar_poly_a_partir_da_rede("grid3000.net.xml", "grid3000.poly.xml")

