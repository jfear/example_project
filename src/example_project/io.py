"""Collection of io related items."""
import os
import shelve
from collections import namedtuple
import pickle

import numpy as np
import pandas as pd
import re
import scipy.sparse as sp_sparse
import tables


def safe_gene_name(symbol):
    """Normalize gene symbols for use as file names."""
    return (
        symbol.replace("(", "")
        .replace(")", "")
        .replace(":", "")
        .replace("&", "")
        .replace("|", "")
        .replace(".", "")
        .replace(" ", "")
    )


class GffRow(object):
    def __init__(self, row):
        self.seqid, self.source, self.type, self.start, self.end, self.score, self.strand, self.phase, self.attributes = row.strip().split(
            "\t"
        )
        self.is_gene = self.type == "gene"
        self.parsed_attributes = self.parse_attributes()

    def parse_attributes(self):
        parsed_attributes = {}
        for attr in self.attributes.split(";"):
            mm = re.search('(?P<key>.*?)\s+"(?P<value>.*?)"', attr)
            if mm:
                parsed_attributes[mm.group("key").strip()] = mm.group("value").strip()
        return parsed_attributes

    def __getitem__(self, key):
        return self.parsed_attributes[key]


if __name__ == "__main__":
    main()
