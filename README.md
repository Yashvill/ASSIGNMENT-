# Data integration project(numpy,pandas)-
Overview
Patent Databases: 
Patent_1975-2010.dta: This file contains information on patents, including their number, claims, application year, application date, grant year, and grant date. 
Citations_1975-1999.dta: This file contains information on which patents are cited by each patent. Patents in the right column cite patents in the left column. There are two aspects to this information – backward and forward citations. Backward citations are the citations that a patent cites in the patent document. Forward citations are the citations a patent receives in future patent applications. For example, a patent k cites patents l, m, n, and o. Also, let's say, patent k is cited by patents b, p, and d. In this case, patent k has four backward citations and three forward citations. Information on citations is divided into three files because it is too much to contain in one file. Other file names are - Citations_2000-2010 part 1.dta and Citations_2000-2010 part 2.dta.  
Assignees_1975-2010.dta: This file contains information on assignees and their locations. Assignees are basically the companies that own these patents. 
Class-Subclass_1975-2010.dta: Patents belong to different technologies. This file provides information on which technology class(es) and subclass(es) each patent belongs to. A patent can be a part of one class and one subclass, one class and multiple subclasses, and multiple classes and multiple subclasses. Classes are broad categories, and subclasses are subsets of classes. For example, if a class is 'bird,' subclasses would be different kinds of birds, e.g., doves, seabirds, herons, ducks, etc. 
Inventors_1975-2010 part 1.dta: This file contains information about people who created these patents. There can be one person who created a patent or a team of people who collaborated to create a patent. These people are referred to as inventors. This file contains information on the names and location of these inventors. This file has two parts due to a large number of rows. The name of the second file is Inventors_1975-2010 part 2.dta. 



Work Overview
The work typically involves processing large raw data, ranging from a few thousand to a few million observations. The final goal is to create a dataset that contains entities or units and a set of information for these entities/units in different columns. The information in columns is calculated based on predefined logic or formulas. To understand it better, I am including two tables below that you can try to fill in based on the data provided to you. The tables are in increasing order of difficulty. Please finish Table 1 first, and we can have a meeting to discuss it before you work on the second table. If you like, feel free to finish both tables.
Table 1
Patent
Year
# of citations
# of unique classes
# of unique subclasses
p1
y1
c1
k1
s1
p2
y3
c2
k2
s2
p3
y4
c3
k3
s3
p4
y6
c4
k4
s4


Table 2
Patent
Year
Originality
Familiarity
p1
y1
x1
y1
p2
y3
x2
y2
p3
y4
x3
y3
p4
y6
x4
y4


The tables above give an example of four patents (p1-p4) that were granted in years mentioned in the column 'Year.' For Table 1, you need to count the number of citations, unique classes, and unique subclasses for all patents in the patent_1975-2010.dta file. For Table 2, you need to calculate the originality and familiarity of all patents based on specific formulas (please see below in the document).
To create measures in both tables, you will have to combine data from different datasets. You have access to all datasets in the shared drive. Please note that the unique identifier across files is the patent number. You can use the patent number as a key to combining different datasets. Also, for convenience, inventor names can be converted to unique ids based on their first, middle, and last names. 
Patent Originality: This is a citation-based measure. You will have to see the subclasses to which citations of each patent are assigned. For example, if patent a cites three patents j,  k,  l then you need to find the subclasses attached to j, k, and l. Then, use the formula below to calculate originality: 

Patent familiarity: a subclass-based measure. This involves two steps. First, the calculation of the familiarity of each subclass of the patent. Second, the average familiarity of all subclasses for the same patent. Please see the formula below.
