.. _overview:

About Coquery
#############

.. toctree::
    :maxdepth: 2

Features
========

Coquery is a free corpus query tool for linguistis, lexicographers, 
translators, and anybody who wishes to search and analyse a text corpus.

You can either build your own corpus from a collection of text files
or PDF documents in a directory on your computer, or install a corpus 
module for one of the supported corpora (the corpus data files are not
provided by Coquery).

.. raw:: html
    
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6">
                <h2>Corpora</h2>
                <ul>
                    <li>Use the corpus manager to install one of the 
                    supported corpora, or to build your own corpus</li>
                    <li>Filter your query for example by year, genre, or speaker gender</li>
                    <li>Choose which corpus features will be included in your query results</li>
                    <li>View every token that matches your query within its context</li>
                </ul>
            </div>
            <div class="col-md-6">
                <h2>Queries</h2>
                <ul>
                    <li>Query by orthography, phonetic transcription, lemma, or gloss, and restrict your query by part-of-speech</li>
                    <li>Use string functions e.g. to test if a token contains a letter sequence</li>
                    <li>Use the same query syntax for all installed corpora</li>
                    <li>Automate queries by reading them from an input file</li>
                </ul>
            </div>
        </div>
        
        <div class="row">
            <div class="col-md-6">
                <h2>Analysis</h2>
                <ul>
                    <li>Summarize the query results as frequency tables</li>
                    <li>Calculate entropies and relative frequencies</li>
                    <li>Fetch collocations, and calculate association statistics like mutual information scores or conditional probabilities</li>
                </ul>
            </div>
            <div class="col-md-6">
                <h2>Visualizations</h2>
                <ul>
                    <li>Use bar charts, heat maps, or bubble charts to 
                    visualize frequency distributions</li>
                    <li>Illustrate diachronic changes by using time series plots</li>
                    <li>Show the distribution of tokens within a corpus in a barcode or a beeswarm plot</li>
                </ul>
            </div>
        </div>
        
        <div class="row">
            <div class="col-md-3">
            </div>
            <div class="col-md-6">
                <h2>Databases</h2>
                <ul>
                    <li>Either use easy-to-use internal databases, or connect to a powerful MySQL server</li>
                    <li>Access large corpora on a MySQL server over the network</li>
                    <li>Link data tables from different corpora, e.g. to include phonetic transcriptions in a corpus that does not contain them.</li>
                </ul>
            </div>
            <div class="col-md-3">
            </div>
        </div>
    </div>
    

Supported corpora
=================

Coquery already has installers for the following linguistic corpora:

.. raw:: html

    <div class="list-group">
        <a class="list-group-item" href="https://catalog.ldc.upenn.edu/LDC96S36">Bostom University Radio Speech Corpus</a>
        <a class="list-group-item" href="http://www.natcorp.ox.ac.uk/">British National Corpus</a>
        <a class="list-group-item" href="http://corpus.byu.edu/coca/">Corpus of Contemporary American English</a>
        <a class="list-group-item" href="http://corpus.byu.edu/coha/">Corpus of Historical American English</a>
        <a class="list-group-item" href="http://buckeyecorpus.osu.edu/">Buckeye Corpus</a>
        <a class="list-group-item" href="https://catalog.ldc.upenn.edu/LDC96L14">CELEX Lexical Database</a>
        <a class="list-group-item" href="http://sourceforge.net/projects/ice-nigeria/">ICE-Nigeria</a> 
    </div>

Note that in order to use these corpora, you first need to obtain the corpus 
data from the linked websites.

If you are missing a corpus from the list of installed corpora, you can 
either program a custom installer for your corpus, or you can :ref:`contact` 
the Coquery developer whether an installer for your corpus may be included 
in a future release of Coquery. 

License
=======

Coquery is free software released under the terms of the 
:ref:`GNU General Public License (version 3) license`. This license gives you 
the freedom to use Coquery for any purpose. It also allows you to copy, 
modify, and redistribute the software for as long as the modified software is 
also licensed under the GNU GPL. 

Coquery can be :ref:`downloaded download` free of charge. Corpus installers 
that are not contained in the official download packages may be released 
under other licenses.