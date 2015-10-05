from __future__ import unicode_literals
from __future__ import print_function

from corpusbuilder import *
import codecs

class CMUdictBuilder(BaseCorpusBuilder):
    encoding = "latin-1"
    file_filter = "cmudict*"
    
    def __init__(self, gui=False, *args):
        # all corpus builders have to call the inherited __init__ function:
        super(CMUdictBuilder, self).__init__(gui, *args)
        
        # Add table descriptions for the table used in this database.
        #
        # Every table has a primary key that uniquely identifies each entry
        # in the table. This primary key is used to link an entry from one
        # table to an entry from another table. The name of the primary key
        # stored in a string is given as the second argument to the function
        # add_table_description().
        #
        # A table description is a dictionary with at least a 'CREATE' key
        # which takes a list of strings as its value. Each of these strings
        # represents a MySQL instruction that is used to create the table.
        # Typically, this instruction is a column specification, but you can
        # also add other table options for this table. Note that the primary
        # key cannot be set manually.
        # 
        # Add the dictionary table. Each row in this table represents a 
        # dictionary entry. Internally, it double-functions both as the
        # corpus table (which is required to run queries in the first place)
        # and the lexicon table (which is required for word look-up). It
        # has the following columns:
        # 
        # WordId
        # An int value containing the unique identifier of the lexicon
        # entry associated with this token.
        #
        # Text
        # A string value containing the orthographic form of the token.
        # Transcript
        # A string value containing the phonological transcription using
        # ARPAbet.

        
        self.corpus_table = "dict"
        self.corpus_id = "WordId"
        self.corpus_word_id = "WordId"
        self.word_table = "dict"
        self.word_id = "WordId"
        self.word_label = "Text"
        self.word_transcript = "Transcript"
        
        self.create_table_description(self.word_table,
            [Primary(self.corpus_id, "MEDIUMINT(6) UNSIGNED NOT NULL"),
             Column(self.word_label, "VARCHAR(50) NOT NULL"),
             Column(self.word_transcript, "VARCHAR(100) NOT NULL")])

    def build_load_files(self):
        files = self.get_file_list(self.arguments.path)
        if len(files) > 1:
            raise RuntimeError("<p><b>There is more than one file in the selected directory.</b></p><p>{}</p><p>Please remove the unneeded files, and try again to install.".format("<br/>".join(files)))
        if len(files) == 0:
            raise RuntimeError("<p><b>No dictionary file could be found in the selected directory.</p><p>{}</p><p>The file name of dictionary files has to start with the sequence <code>cmudict</code>. If you have saved the CMUdict file under a different name, rename it so that its file name matches this sequence.</p><p>If you have not downloaded andictionary file yet, please go to the CMUdict website and follow the download instructions there.</p> ".format("<br/>".join(files)))
        with codecs.open(files[0], "r", encoding = self.arguments.encoding) as input_file:
            content = input_file.readlines()
        if self._widget:
            self._widget.progressSet.emit(len(content) // 100, "Reading dictionary file...")
            self._widget.progressUpdate.emit(0)

        for i, current_line in enumerate(content):
            current_line = current_line.strip()
            if current_line and not current_line.startswith (";;;"):
                word, transcript = current_line.split ("  ")
                self.table(self.word_table).add(
                    {self.word_label: word, 
                    self.word_transcript: transcript})
            if self._widget and not i % 100:
                self._widget.progressUpdate.emit(i // 100)
        self.commit_data()

    @staticmethod
    def get_title():
        return "Carnegie Mellon Pronouncing Dictionary"

    @staticmethod
    def get_url():
        return 'http://www.speech.cs.cmu.edu/cgi-bin/cmudict'
    
    @staticmethod
    def get_name():
        return "CMUdict"
    
    @staticmethod
    def get_license():
        return "CMUdict is licensed under a modified FreeBSD license."
    
    @staticmethod
    def get_description():
        return ["The Carnegie Mellon Pronouncing Dictionary (CMUdict) is a dictionary containing approximately 135.000 English word-forms and their phonemic transcriptions, using a variant of the ARPAbet transcription system."]

BuilderClass = CMUdictBuilder

if __name__ == "__main__":
    BuilderClass().build()
    