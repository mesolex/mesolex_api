from query_api.transformations.utils import transformation
from lexicon.models import PlantThesaurus


@transformation(data_field='plant_thesaurus')
def plant_thesaurus(query_string):
    res = PlantThesaurus.objects.filter(genus_species__exact=query_string)
    new_str = "|".join([query_string] + [r.synonym for r in res])
    return new_str
