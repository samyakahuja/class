# A Tensor Based Data Model for Polystore

## What you need to know beforehand

1.  __What is ETL?__

    ETL is short for Extract, Transform, Load.
    -   Data Extraction involves extracting data from homogeneous
        or hetrogeneous data sources.
    -   Data Transformation processes the data by transforming them into
        a proper storage structure for purpose of querying and analysis.
    -   Data Loading loads the final data into a target database such
        as a Data Warehouse

2.  __What is a data model?__

    Data model determines the logical structure of the database, and
    determines how data can be stored, organised and manipulated. Some
    types of data models are : 
    - Relational
    - Hierarchial 
    - Network
    - Document Based

3. __What is Polystore?__
    
    In recent years we have seen the convergence of two different fields,
    namely, High Performance Computing(HPC) and Databases to form a new
    field called Data Intensive HPC. One of the major concerns of Data
    Intensive HPC is to be able to quickly feed the Algorithm with the 
    required data. Now each algorithm might be using a different data model
    so to do that we build a multi-paradigm storage system called Polystore.

    In such systems data can be partitioned and stored in a model that best
    fits the algorithm required for analysis. 

3.  __What is Logical Data Independence?__

    Logical Data Independence is the ability to change the logical
    (conceptual) schema without changing the external (view) schema.
    For expample, the addition of new entities, attributes, or 
    relationships to the conceptual schema should not require any change
    to the user view or programs.

4.  __What is TF-IDF?__
    
    _term frequency - inverse document frequency_ is a numerical statistic
    that is intended to reflect how important a word is to a document in a
    collection or corpus. tf-idf value increases proportionally to the 
    number of times a word appears in a document and is offset by the
    number of documents in the corpus that contain that word, which helps
    adjusting for the fact that some words appear more frequently in
    general and the words we are interested in are those that occur
    infrequently among different documents.

5.  __What is a Hypermatrix?__

    Hypermatrix is how we represent the components of a tensor. For example
    a tensor with rank k can be represented by a hypermatrix of dimension
    k ( i.e n1 x n2 x ... x nk rows). Basically Hypermatrix is a 
    generalization of a matrix in n dimensions.
