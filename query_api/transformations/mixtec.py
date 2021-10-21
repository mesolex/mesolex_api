from query_api.transformations.utils import transformation
import re

VOW_PATTERN = re.compile("(([aeiou])[¹²³⁴1234']{0,2})")
FLEX_ORTH_PATTERN = "(n[td])"


@transformation(data_field='mixtec_tone_neutralization')
def mixtec_tone_neutralization(query_string):
    return re.sub(VOW_PATTERN, "\g<2>[¹²³⁴1-4']{0,2}", query_string)


@transformation(data_field='mixtec_flex_orthography')
def mixtec_flex_orthography(query_str):
    return re.sub(FLEX_ORTH_PATTERN, "n(d|t)", query_str)

