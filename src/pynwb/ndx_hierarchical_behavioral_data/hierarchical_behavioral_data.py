from ndx_icephys_meta.icephys import HierarchicalDynamicTableMixin
from pynwb.core import DynamicTable, DynamicTableRegion, VectorIndex
from pynwb import register_class
from hdmf.utils import docval, get_docval


@register_class('PhonemesTable', 'ndx-hierarchical-behavioral-data')
class PhonemesTable(DynamicTable, HierarchicalDynamicTableMixin):
    """
    'A table to store different phonemes'
    """
    __columns__ = (
        {'name': 'label',
         'description': 'Column with one or more phoneme rows',
         'required': True,
         'index': True,
         'table': True},
    )

    @docval(*get_docval(DynamicTable.__init__, 'id', 'columns', 'colnames'))


@register_class('SyllablesTable', 'ndx-hierarchical-behavioral-data')
class SyllablesTable(DynamicTable, HierarchicalDynamicTableMixin):
    """
    A table to store different syllables
    """
    __columns__ = (
        {'name': 'label',
         'description': 'Column with a references to one or more rows in the PhonemesTable table',
         'required': True,
         'index': True,
         'table': True},
    )

    @docval({'name': 'phonemes_table',
             'type': PhonemesTable,
             'doc': 'the PhonemesTable table that the label column indexes.',
             'default': None},
            *get_docval(DynamicTable.__init__, 'id', 'columns', 'colnames'))


@register_class('WordsTable', 'ndx-hierarchical-behavioral-data')
class WordsTable(DynamicTable, HierarchicalDynamicTableMixin):
    """
    A table to store different words
    """
    __columns__ = (
        {'name': 'label',
         'description': 'Column with a references to one or more rows in the SyllablesTable table',
         'required': True,
         'index': True,
         'table': True},
    )

    @docval({'name': 'syllables_table',
             'type': SyllablesTable,
             'doc': 'the SyllablesTable table that the label column indexes.',
             'default': None},
            *get_docval(DynamicTable.__init__, 'id', 'columns', 'colnames'))


@register_class('SentencesTable', 'ndx-hierarchical-behavioral-data')
class SentencesTable(DynamicTable, HierarchicalDynamicTableMixin):
    """
    A table to store different sentences
    """
    __columns__ = (
        {'name': 'label',
         'description': 'Column with a references to one or more rows in the WordsTable table',
         'required': True,
         'index': True,
         'table': True},
    )

    @docval({'name': 'words_table',
             'type': WordsTable,
             'doc': 'the WordsTable table that the label column indexes.',
             'default': None},
            *get_docval(DynamicTable.__init__, 'id', 'columns', 'colnames'))


@register_class('TranscriptionTable', 'ndx-hierarchical-behavioral-data')
class TranscriptionTable(DynamicTable, HierarchicalDynamicTableMixin):
    """
    This DynamicTable is intended to group together a collection of sub-tables. Each sub-table is a DynamicTable itself.
    This type effectively defines a 2-level table in which the main data is stored in the main table implemented by this
    type and additional columns of the table are grouped into categories, with each category being represented by a
    separate DynamicTable stored within the group. Here, sub-tables are: sentence table which stores different
    sentences; words table which stores constituting words; syllables table for storing syllables of each word; and
    phonemes table for storing consisting of phonemes.
    """
