#!/usr/bin/env python3

import sys
if not sys.version_info.major == 3 and not sys.version_info >= 3:
    sys.exit("Please use Python 3.3 or higher for this script")

import re, os, argparse
try:
    import bibtexparser
    import yaml
    from scholar.scholar import *
except ImportError as error:
    sys.exit("FAIL: " + error.name)

#   Opena  document and turn it into a dictionary
l = yaml.load_all(open('_publications/2016-Environmental-Association.md', 'r')).__next__()

#   Search for and get stuff
querier = ScholarQuerier()
query = ClusterScholarQuery(8363220939686393422)
settings = ScholarSettings()
settings.set_citation_format(settings.CITFORM_NONE)
querier.apply_settings(settings)
querier.send_query(query)
querier.articles[0].attrs['num_citations'][0]
querier.articles[0].attrs['url_citations'][0]

