# Kegg_Scrap
Web scrapper for Kegg (py)


option B:
  www.genome.jp/kegg/pathway.html
    {skip Global and Overview maps}
    select saccharomyces cerevisiae
    Go (select each green box?)
    
#example entry: https://www.genome.jp/dbget-bin/www_bget?sce:YKL127W+sce:YMR105C+sce:YMR278W

---------

##Print:
entry#-pathwayID-name- Module INFO(description in English)


Ensembl BioMart
    Ensembl Genes 99
    Sarcomycees Cereviseia 
    Attributes
        Gene dropdown (uncheck transcipt stable ID) (see what we need off that list)
        External References
            Kegg pathway and enzyme ID

    Kegg Pathway & Enzyme ID dropdown
    Gene Stable ID

    need to split kegg pathway and gene ID on the "+"

Consider TSV for export (python+commas=?)

... use only the ones with Kegg values. (consider using Kegg directly because it may not shoe none metabolic pathways)
    some (like a recpetor) do not have EC numbers 
   !!!! entry#-pathwayID-name- Module INFO(description in English)

   START WITH WEB SCRAPPER!

Download htext vvv
https://www.kegg.jp/kegg-bin/get_htext?ko00001.keg
    lists all
  
