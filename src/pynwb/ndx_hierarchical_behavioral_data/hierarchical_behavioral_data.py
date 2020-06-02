from ndx_icephys_meta.icephys import HierarchicalDynamicTableMixin
from pynwb.core import DynamicTable
from pynwb import register_class

@register_class('SentencesTable', 'ndx-hierarchical-behavioral-data')
class SentencesTable(DynamicTable, HierarchicalDynamicTableMixin):


@register_class('WordsTable', 'ndx-hierarchical-behavioral-data')
class WordsTable(DynamicTable, HierarchicalDynamicTableMixin):


@register_class('SyllablesTable', 'ndx-hierarchical-behavioral-data')
class SyllablesTable(DynamicTable, HierarchicalDynamicTableMixin):


@register_class('PhonemesTable', 'ndx-hierarchical-behavioral-data')
class PhonemesTable(DynamicTable, HierarchicalDynamicTableMixin):


@register_class('TranscriptionTable', 'ndx-hierarchical-behavioral-data')
class TranscriptionTable(DynamicTable, HierarchicalDynamicTableMixin):