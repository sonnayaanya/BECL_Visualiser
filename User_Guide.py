import streamlit as st

st.markdown('# Instruction and Additional Information')
st.header('About the Bochum English Countability Lexicon')
st.markdown('''
            This web page is dedicated to providing essential information on Bochum English Countability Lexicon.
            The Bochum English Countability Lexicon (Kiss et al., 2014, 2016) is a lexical resource
            which contains countability classes for English noun-sense pairs. The classes were
            developed on the basis of a large annotation process conducted by four native speakers of Canadian English. 
            The six annotation questions designed for the identification of countability classes are test_I_1, test_I_2, test_II_1, test_II_2,
            test_III_1 and test_III_2. Please refer to the [Column Information](#column-information) section for more.
            The current release, BECL 2.1, contains 11,869 noun-sense pairs (out of 7,050 distinct nouns). 
            The whole lexicon is presented in a CSV file (available for download on the main page) with a line for each noun-sense pair. 
            Besides the countability class, several other lexical features are provided in separate columns. 
            These columns contain information on their singular and plural occurrences in the Open American National Corpus, 
            the description of the individual senses from WordNet (Miller, 1995), total number of other senses 
            for the respective noun and their synsets; other annotations regarding the nature of the sense, 
            e.g. result, state, nominalization or idiomatic expression and meta information on the annotation process.
''')
st.divider()

st.header('Column Information')
st.markdown('''
            * **lemma**: the noun form.
            * **senseindex**: sense number in WordNet.
            * **description**: definition of the noun sense.
            * **wordnet_total_senses**: total number of senses in WordNet.
            * **sense_synset**: synset for the sense. A synset is identified with a 3-part name of the form: *word.pos.sense number*.
            * **similar_senses**: set of similar synsets measured according to the Leacock and Chodorow (LCH) score.
            * **oanc_total**: frequency distribution of the lemma in the Open American National Corpus (OANC).
            * **oanc_sg**: frequency distribution of the lemma's singular form in OANC.
            * **oanc_pl**: frequency distribution of the lemma's singular form in OANC.
            * **test_I_1**: can the noun-sense pair in its singular form appear with more? For more information, please refer to the following papers:

                1. Kiss, Tibor; Pelletier, F. Jeffry; Husic, Halima. (2021). Polysemy and the Count-Mass Distinction. What can we derive from a lexicon of count and mass senses?
                2. Kiss, Tibor; Pelletier, F. Jeffry; Husic, Halima; Poppek, Johanna Marie; Simunic, R. Nino. (2016). A Sense-Based Lexicon for Count and Mass Expressions: The Bochum English Countability Lexicon.
            * **test_I_2**: if the answer to test_I_1 is *yes*, is the comparison made on number of entities, or a different mode of measurement?
            * **test_II_1**: can the noun-sense pair in its plural form appear with more?
            * **test_II_2**: if the answer to test_II_1 is *yes*, is the sentence equivalent to one with an explicit classifier?
            * **test_III_1**: can the noun-sense pair in its singular form and combined *with* the indefinite determiner be the subject 
            of a definition of characterization?
            * **test_III_2**: can the noun-sense pair in its singular form but *without* the indefinite determiner be the subject of a
            definition of characterization?
            * **idiomatic**: indicator of (parts of) idioms.
            * **nominalization**: indicator of nominalization.
            * **result_state**: indicator of whether the noun sense represents the result of an action.
            * **process**: indicator of whether the noun sense represents a process.
            * **act_event**: indicator of whether the noun sense represents an action or event.
            * **proper_name**: indicator of proper names.
            * **major_class**: major countability class, i.e. one of the following: regular count, regular mass, both mass and count, neither mass nor count. 
            * **minor_class**: minor countability class. Minor countability classes, 18 in number, stem from the answers to the test questions. They are represented
            as integers due to being artifacts of the analysis conducted in R. Besides, it is unfeasible to describe each class succinctly but accurately with words.
            * **complete**: indicator of whether all senses of the noun listed in WordNet have been annotated.
            * **variation_in_writing**: indicator of whether the noun occurs in more than one orthographic form.
            * **multiple**: indicator of whether all senses of the given noun occur in the same minor countability class.
            * **unit_letter**: indicator of whether the noun is a letter or a unit of measurement.
            ''')
st.divider()

st.header('Using the Website')
st.markdown('''
            This website offers several functionalities to assist with working with the Bochum English Countability Lexicon (BECL). 
            These features can be used independently or in combination:

            - **Word search:** find exact matches for word(s) in the "lemma" column. 
            To search the entire lexicon (i.e. across all columns), use the magnifying glass button located in the upper right corner of the lexicon dataframe.

            - **Filtering by columns**: select one or more columns to display. You can also filter by unique values within these columns. 
            To do this, select the column and click on the 'filter' button, then choose the desired values from the drop-down list.

            - **Adjusting Output Length**: change the number of rows displayed by specifying the desired number of rows.

            - **Saving the Resulting Table**: click on the download icon located in the upper right corner of the lexicon dataframe to save it to your device. 
            To save the original version of the lexicon use the "Download as CSV" button at the bottom of the Interactive Viewer.

            ''')