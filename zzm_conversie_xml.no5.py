
# Vijfde conversie verwijderen tags <skos:Concept> en </skos:Concept>

import re

# Lees het oorspronkelijke XML-bestand
with open('/Users/patrickmout/Downloads/zzm/zzm_aangepast_stap4_xml.rdf', 'r') as file:
    rdf_content = file.read()

# Definieer het patroon voor <sys:Object> tags
sys_object_pattern = r'<skos:Concept>|</skos:Concept>'

# Verwijder de <sys:Object> en </sys:Object> tags
modified_content = re.sub(sys_object_pattern, '', rdf_content)

# Verwijder overgebleven lege regels
modified_content = re.sub(r'\n\s*\n', '\n', modified_content)


# Schrijf het aangepaste XML-bestand
with open('/Users/patrickmout/Downloads/zzm/zzm_aangepast_stap5_xml.rdf', 'w') as file:
    file.write(modified_content)
