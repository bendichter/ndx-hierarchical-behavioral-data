# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import (
    NWBNamespaceBuilder,
    export_spec,
    NWBGroupSpec,
    NWBAttributeSpec
)


def main():
    ns_builder = NWBNamespaceBuilder(
        doc='NWB extension for hierarchical behavioral data',
        name='ndx-hierarchical-behavioral-data',
        version='0.1.0',
        author=['Ben Dichter',
                'Armin Najarpour Foroushani'],
        contact=['ben.dichter@catalystneuro.com']
    )

    # Add the type we want to include from core to this list
    include_core_types = ['Container',
                          'DynamicTable',
                          'DynamicTableRegion',
                          'VectorData',
                          'VectorIndex',
                          'NWBFile']
    # Include the types that are used by the extension and their namespaces (where to find them)
    for type_name in include_core_types:
        ns_builder.include_type(type_name, namespace='core')

    # Create a generic compound datatype

    sentences_table_spec = NWBGroupSpec(
        name='sentences',
        neurodata_type_def='SentencesTable',
        neurodata_type_inc='DynamicTable',
        doc='A table for sentences'
    )
    words_table_spec = NWBGroupSpec(
        name='words',
        neurodata_type_def='WordsTable',
        neurodata_type_inc='DynamicTable',
        doc='A table for words'
    )
    syllables_table_spec = NWBGroupSpec(
        name='syllables',
        neurodata_type_def='SyllablesTable',
        neurodata_type_inc='DynamicTable',
        doc='A table for syllables'
    )
    phonemes_table_spec = NWBGroupSpec(
        name='phonemes',
        neurodata_type_def='PhonemesTable',
        neurodata_type_inc='DynamicTable',
        doc='A table for phonemes'
    )
    transcription_table_spec = NWBGroupSpec(
        name='transcription',
        neurodata_type_def='TranscriptionTable',
        neurodata_type_inc='DynamicTable',
        doc='A table for transcription'
    )

    # Add all of our new data types to this list
    new_data_types = [sentences_table_spec,
                      words_table_spec,
                      syllables_table_spec,
                      phonemes_table_spec,
                      transcription_table_spec]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    main()
