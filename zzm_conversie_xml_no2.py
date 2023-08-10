# Twee conversie toevoegen aan tag <skos:Concept> <dcterms:subject...

import re

# Lees het RDF/XML-bestand
with open("/Users/patrickmout/Downloads/zzm/zzm_aangepast_stap1_xml.rdf", 'r') as file:
    rdf_content = file.read()

# Zoek naar alle voorkomens van <skos:Concept>...</skos:Concept> blokken
concept_blocks = re.findall(r'<sys:Object>.*?</sys:Object>', rdf_content, re.DOTALL)

# Lus door de gevonden blokken
for concept_block in concept_blocks:
    # Zoek de inhoud tussen <dc:identifier>...</dc:identifier> binnen elk concept_block
    identifier_match = re.search(r'<dc:identifier>(.*?)</dc:identifier>', concept_block, re.DOTALL)

    if identifier_match:
        identifier_value = identifier_match.group(1)  # Haal de waarde tussen de tags
        new_tag = f'<edm:ProvidedCHO rdf:about="http://data.collectienederland.nl/resource/document/zuiderzeemuseum/{identifier_value}">'  # Maak de nieuwe tag

        # Voeg de nieuwe tag toe aan het concept_block
        modified_block = concept_block.replace('<skos:Concept>', new_tag + "\n" + '<skos:Concept>', 1)

        # Vervang het oorspronkelijke concept_block door het gewijzigde concept_block in rdf_content
        rdf_content = rdf_content.replace(concept_block, modified_block)

# Schrijf het aangepaste XML-bestand
with open('/Users/patrickmout/Downloads/zzm/zzm_aangepast_stap2_xml.rdf', 'w') as file:
    file.write(rdf_content)
