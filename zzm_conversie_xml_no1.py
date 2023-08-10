# Eerste conversie toevoegen tags <sys:Object> en </sys:Object>
import re

# Lees het RDF/XML-bestand
with open('/Users/patrickmout/Downloads/zzm/zzm_conversie_test_file.xml', 'r') as file:
    rdf_content = file.read()

# Definieer de begintag die je wilt toevoegen
new_begintag = "<sys:Object>"

# Zoek naar de begintag waar je na wilt toevoegen
target_begintag = "</ore:Aggregation>"

# Vervang de target_begintag met de target_begintag gevolgd door de nieuwe begintag
modified_content_begin = re.sub(target_begintag, lambda x: x.group(0) + "\n" + new_begintag, rdf_content)

# Definieer de endtag die je wilt toevoegen
new_endtag = "</sys:Object>"

# Zoek naar de endtag waar je na wilt toevoegen
target_endtag = "</nave:DelvingResource>"

# Vervang de target_endtag met de target_endtag gevolgd door de nieuwe endtag
modified_content_end = modified_content_begin.replace(target_endtag, target_endtag + "\n" + new_endtag)

# Schrijf het aangepaste XML-bestand
with open('/Users/patrickmout/Downloads/zzm/zzm_aangepast_stap1_xml.rdf', 'w') as file:
    file.write(modified_content_end)

