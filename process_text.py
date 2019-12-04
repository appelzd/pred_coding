# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:20:46 2019

@author:  Scott Schafer
@date:    8/5/2019
@purpose: fundamental text mining functions
"""

import gensim
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
import re
import string

from db import Db as dbrepo
from blobRepo import BlobRepo as blobs

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
    
class pred_coding_poc:

    def get_wordnet_pos(self, treebank_tag):
        # Convert the naming scheme to that recognized by WordNet
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN
        
    def create_lemmas_from_file(self, datafile, encoding='latin-1'):
  
        #Normalize
        text = datafile.lower()

        #Strip punctuation
        text = text.replace("'",'').replace("\n",' ')
        text = re.sub('[%s]' % re.escape(string.punctuation  + '£' + 'ï' + '»' + '¿'), ' ', text)
        
        # Tokenize
        # need to run commented line the first time you do this
        tokens = word_tokenize(text)

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        stop_lambda = lambda x: [y for y in x if y not in stop_words]
        tokens = stop_lambda(tokens)

        #Part of Speech
        # need to run commented line the first time you do this
        pos_lambda = lambda x: nltk.pos_tag(x)
        pos_wordnet = lambda x: [(y[0], self.get_wordnet_pos(y[1])) for y in x]
        speech_parts = pos_wordnet(pos_lambda(tokens))
        
        #Lemmatization
        lemmatizer = WordNetLemmatizer()
        lemmatizer_fun = lambda x: lemmatizer.lemmatize(*x)
        lemmas = [lemmatizer_fun(x) for x in speech_parts]
        
        return(lemmas)
        
    def identify_topics(self, datafiles, num_topics=5, no_below=3, no_above=.34, passes=50):
        #create topics based on lemma lists created from whole files
        
        lemmas = [self.create_lemmas_from_file(datafile) for datafile in datafiles]
        
        #create and filter dictionary
        dictionary = gensim.corpora.Dictionary(lemmas)
        dictionary.filter_extremes(no_below=no_below, 
                                no_above=no_above)
    
       #Use dictionary to form bag of words
        bow_corpus = [dictionary.doc2bow(doc) for doc in lemmas]
        
        #Fit tfidf model
        tfidf = gensim.models.TfidfModel(bow_corpus)
        corpus_tfidf = tfidf[bow_corpus]
        lda_model_tfidf = gensim.models.LdaModel(corpus_tfidf, 
                                                num_topics=num_topics, 
                                                id2word = dictionary, 
                                                passes = passes)
        return(lda_model_tfidf, dictionary)
        
    def fit_new_doc(self, docfile, lda_model, dictionary):
        lemmas = self.create_lemmas_from_file(docfile)
        bow_corpus = dictionary.doc2bow(lemmas) 
        topic_prediction = lda_model.get_document_topics(bow_corpus)
        return(topic_prediction)
        

    def process_docids_for_similarity(self, search_uid, docids):

        db = dbrepo()
        blob_repo = blobs()

        datafiles = list(blob_repo.GetBlobs(db.get_documentnames_by_docid(docids)))    
        
        lda_model, dictionary = self.identify_topics(datafiles, num_topics=4, no_above=.75, no_below=3)
        
        
        for idx, topic in lda_model.print_topics(-1):
            print("Topic: {} Word: {}".format(idx, topic))
            print("\n")
        
        for testfile in datafiles:
            topic_prediction = self.fit_new_doc(testfile, lda_model, dictionary)
            print('Test file likely to be topic {}, probability = {:.4f}'.format(topic_prediction[0][0], topic_prediction[0][1]))
    
    
















