%timeit spell("I'm not sleapy and tehre is no place I'm giong to.")
373 µs ± 2.09 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
%timeit spell("There is no comin to consiousnes without pain.")
150 ms ± 2.02 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)import json
import re
from collections import Counter, OrderedDict

from autocorrect.constants import word_regexes


def get_words(filename, lang, encd):
    word_regex = word_regexes[lang]
    capitalized_regex = r'(\.|^|<|"|\'|\(|\[|\{)\s*' + word_regexes[lang]
    with open(filename, encoding=encd) as file:
        for line in file:
            line = re.sub(capitalized_regex, "", line)
            yield from re.findall(word_regex, line)


def count_words(src_filename, lang, encd="utf-8", out_filename="word_count.json"):
    words = get_words(src_filename, lang, encd)
    counts = Counter(words)
    # make output file human readable
    counts_list = list(counts.items())
    counts_list.sort(key=lambda i: i[1], reverse=True)
    counts_ord_dict = OrderedDict(counts_list)
    with open(out_filename, "w") as outfile:
        json.dump(counts_ord_dict, outfile, indent=4)
