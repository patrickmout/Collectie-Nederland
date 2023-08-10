# Derde conversie toevoegen aan tag </skos:Concept> </dcterms:subject>

import re

# Lees het RDF/XML-bestand
with open("/Users/patrickmout/Downloads/zzm/zzm_aangepast_stap2_xml.rdf", 'r') as file:
    rdf_content = file.read()

# Zoek naar alle voorkomens van <sys:Object>...</sys:Object> blokken
object_blocks = re.findall(r'<sys:Object>.*?</sys:Object>', rdf_content, re.DOTALL)

# Lus door de gevonden blokken
for object_block in object_blocks:
    # Zoek de laatste </skos:Concept> tag binnen elk object_block
    last_skos_concept_index = object_block.rfind('</skos:Concept>')

    if last_skos_concept_index != -1:
        # Vervang de laatste </skos:Concept> tag door </skos:Concept></dcterms:subject>
        modified_block = object_block[:last_skos_concept_index] + '</skos:Concept>' + '\n' + '</edm:ProvidedCHO>' + object_block[last_skos_concept_index+len('</skos:Concept>'):]

        # Vervang het oorspronkelijke object_block door het gewijzigde object_block in rdf_content
        rdf_content = rdf_content.replace(object_block, modified_block)

# Schrijf het aangepaste XML-bestand
with open('/Users/patrickmout/Downloads/zzm/zzm_aangepast_stap3_xml.rdf', 'w') as file:
    file.write(rdf_content)
