# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import (
    NWBNamespaceBuilder,
    export_spec,
    NWBGroupSpec,
    NWBAttributeSpec,
    NWBDatasetSpec
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

    # Create a collection of dynamic tables
    transcription_table_spec = NWBGroupSpec(
        name='transcription',
        neurodata_type_def='TranscriptionTable',
        neurodata_type_inc='DynamicTable',
        doc='DynamicTable container that supports storing a collection of sub-tables. Each sub-table is a '
            'DynamicTable itself. This type effectively defines a 2-level table in which the main data is stored in '
            'the main table implemented by this type and additional columns of the table are grouped into categories, '
            'with each category being represented by a separate DynamicTable stored within the group.'
            'This table is intended to group together a sentence, with its constituting words, syllables, and phonemes '
            'Each row in the table represents a single sentence consisting typically of a number of words, and '
            'each word is made of a few syllables, and it is also consisting of phonemes. ',
        attributes=[NWBAttributeSpec(name='categories',
                                     dtype='text',
                                     dims=['num_categories'],
                                     doc='The names of the categories in this TranscriptionTable. Each '
                                         'category is represented by one DynamicTable stored in the parent group.'
                                         'This attribute should be used to specify an order of categories.',
                                     shape=[None])
                    ],
        groups=[NWBGroupSpec(neurodata_type_inc='DynamicTable',
                             doc='A DynamicTable representing a particular category for columns in the '
                                 'TranscriptionTable parent container. The name of the category is given by '
                                 'the name of the DynamicTable and its description by the description attribute '
                                 'of the DynamicTable.',
                             quantity='*')
                ]
    )

    # Create our table to store sentences
    sentences_table_spec = NWBGroupSpec(
        name='sentences',
        neurodata_type_def='SentencesTable',
        neurodata_type_inc='DynamicTable',
        doc='A table to store different sentences.',
        attributes=[NWBAttributeSpec(name='description',
                                     dtype='text',
                                     doc='Description of what is in this dynamic table.',
                                     value='Table for storing sentence related data')],
        datasets=[NWBDatasetSpec(name='label',
                                 neurodata_type_inc='DynamicTableRegion',
                                 doc='Column for storing sentences. Each row in this DynamicTableRegion is a sentence '
                                     'consisting of words.',
                                 dims=('num_sentences',),
                                 shape=(None,),
                                 dtype='text'
                                 ),
                  NWBDatasetSpec(name='words',
                                 neurodata_type_inc='VectorIndex',
                                 doc='Column for storing a link to the constituting words (rows)',
                                 dims=('num_sentences',),
                                 shape=(None,),
                                 dtype='list'
                                 )
                  ]
    )

    # Create our table to store words
    words_table_spec = NWBGroupSpec(
        name='words',
        neurodata_type_def='WordsTable',
        neurodata_type_inc='DynamicTable',
        doc='A table to store different words',
        attributes=[NWBAttributeSpec(name='description',
                                     dtype='text',
                                     doc='Description of what is in this dynamic table.',
                                     value='Table for storing word related data')],
        datasets=[NWBDatasetSpec(name='label',
                                 neurodata_type_inc='DynamicTableRegion',
                                 doc='Column for storing words. Each row in this DynamicTableRegion is a word '
                                     'consisting of syllables.',
                                 dims=('num_words',),
                                 shape=(None,),
                                 dtype='text'
                                 ),
                  NWBDatasetSpec(name='syllables',
                                 neurodata_type_inc='VectorIndex',
                                 doc='Column for storing a link to the constituting syllables (rows)',
                                 dims=('num_words',),
                                 shape=(None,),
                                 dtype='list'
                                 )
                  ]
    )

    # Create our table to store syllables
    syllables_table_spec = NWBGroupSpec(
        name='syllables',
        neurodata_type_def='SyllablesTable',
        neurodata_type_inc='DynamicTable',
        doc='A table to store different syllables',
        attributes=[NWBAttributeSpec(name='description',
                                     dtype='text',
                                     doc='Description of what is in this dynamic table.',
                                     value='Table for storing syllables related data')],
        datasets=[NWBDatasetSpec(name='label',
                                 neurodata_type_inc='DynamicTableRegion',
                                 doc='Column for storing syllables. Each row in this DynamicTableRegion is a syllable '
                                     'consisting of phonemes.',
                                 dims=('num_syllables',),
                                 shape=(None,),
                                 dtype='text'
                                 ),
                  NWBDatasetSpec(name='phonemes',
                                 neurodata_type_inc='VectorIndex',
                                 doc='Column for storing a link to the constituting phonemes (rows)',
                                 dims=('num_syllables',),
                                 shape=(None,),
                                 dtype='list'
                                 )
                  ]
    )

    # Create our table to store phonemes
    phonemes_table_spec = NWBGroupSpec(
        name='phonemes',
        neurodata_type_def='PhonemesTable',
        neurodata_type_inc='DynamicTable',
        doc='A table to store different phonemes',
        attributes=[NWBAttributeSpec(name='description',
                                     dtype='text',
                                     doc='Description of what is in this dynamic table.',
                                     value='Table for storing phonemes related data')],
        datasets=[NWBDatasetSpec(name='label',
                                 neurodata_type_inc='DynamicTableRegion',
                                 doc='Column for storing phonemes. Each row in this DynamicTableRegion is a phoneme.',
                                 dims=('num_phonemes',),
                                 shape=(None,),
                                 dtype='text')
                  ]
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
