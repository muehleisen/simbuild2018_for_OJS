# -*- coding: utf-8 -*-
"""
Created on Mon May  9 23:16:59 2016

@author: rmuehleisen
"""

from lxml import etree, objectify
import pprint


inputxml = 'Simbuild2012.xml'
outputxml = 'simbuild2012_upload.xml'

#baseURL = 'https://github.com/muehleisen/IPBSA-USA-Pubs/raw/master/SB2004_papers/'
#baseURL = 'https://github.com/muehleisen/IPBSA-USA-Pubs/raw/master/mendeley%20files/2006/'
baseURL = 'https://github.com/muehleisen/IPBSA-USA-Pubs/raw/master/mendeley%20files/2012/'

with open(inputxml,'rb') as f:
    xml = f.read()
 
root = objectify.fromstring(xml)

# the root object has the object records as a child
# records has one or more record as a child
# each record has several children with the data we want including
# title, contributors

#for recordsobj in root.getchildren():
#    for record in recordsobj.getchildren():
#        print(record.titles.title)
#        auths=record.contributors.authors
#        for auth in auths.getchildren():
#            print(auth)
#        print(record.abstract)
#    print()
#    

issues = etree.Element('issues')
issue = etree.SubElement(issues,'issue')
issue.set('published',"true")
issue.set('current','false')
issuetitle = etree.SubElement(issue,'title')
issuetitle.set('locale','en_US')
issuetitle.text=('2012: SimBuild 2012')
issuedate = etree.SubElement(issue,'access_date')
issuedate.text = ('01-01-2012')
issueyear = etree.SubElement(issue,'year')
issueyear.text = '2012'
section = etree.SubElement(issue,'section')
sectiontitle = etree.SubElement(section,'title')
sectiontitle.set('locale','en_US')
sectiontitle.text=('Papers')
article=[]



tree = etree.parse(inputxml)
# context=etree.iterparse("subset.xml")
recordlist=tree.find('records').findall('record')
#for record in recordlist:
for record in root.iter('record'):
    title=record.find('titles').find('title').text
    abstract=record.find('abstract').text
    url=record.find('urls').find('pdf-urls').find('url').text
    pages=[]
    # add a new article element for each record
    article.append(etree.SubElement(section,'article'))
    # add a title as subelement to the newly created article element 
    arttitle=etree.SubElement(article[-1],'title')
    arttitle.set('local','en_US')
    arttitle.text=title
    artabstract=etree.SubElement(article[-1],'abstract')
    artabstract.text=abstract

    #titleel.text=title
    
    
    if record.find('pages') is not None:
        pages=record.find('pages').text
        artpages=etree.SubElement(article[-1],'pages')
        artpages.text=pages
		
    authorlist=record.find('contributors').find('authors').findall('author')
    authors=[]

    firstname=[]
    lastname=[]
    artauthors=[]
    for name in authorlist:
        artauthors.append(etree.SubElement(article[-1],'author'))
        #authors.append(name.text)
        # separate the into last and first using the comma as separator
        name2=name.text.partition(',')
       # lastnames.append(name2[0])
       # firstnames.append(name2[2])
        #artauth.append(name.text)
        firstname=etree.SubElement(artauthors[-1],'firstname')
        lastname=etree.SubElement(artauthors[-1],'lastname')
        email=etree.SubElement(artauthors[-1],'email')
        firstname.text=name2[2]
        lastname.text=name2[0]
        email.text=' '

    artgalley = etree.SubElement(article[-1], 'galley')
    galleylabel = etree.SubElement(artgalley,'label')
    galleylabel.text = 'PDF'
    galleyfile = etree.SubElement(artgalley,'file')
    galleyhref = etree.SubElement(galleyfile,'href')

    filename = url.split('//')
    galleyURL = baseURL + filename[1]
   # galleyURL = 'https://github.com/muehleisen/IPBSA-USA-Pubs/raw/master/SB2004_papers/SB04T1A1.pdf'
    
    
    galleyhref.set('src', galleyURL)
    galleyhref.set('mime_type','application/pdf')
    #galleyfile.text = 'href src="http://www.pdf995.com/samples/pdf.pdf" mime_type="application/pdf"/>'
    
        

    
    print("title: %s " % title)
    print("first names: %s" % firstname)
    print("last names: %s" % lastname)
    #print("authors: %s" % authors)
    print("pages: %s" % pages)
    print("abstract: %s" % abstract)
    print("url: %s" % url)
    print("filename: %s" % filename[1])
    print("galleyURL: %s" % galleyURL)
    print("")
    
    
print



#preamble='<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE issues SYSTEM "native.dtd"> \
#<!-- \
#  * plugins/importexport/native/sample.xml \
#  * \
#  * Copyright (c) 2013-2016 Simon Fraser University Library \
#  * Copyright (c) 2003-2016 John Willinsky \
#  * Distributed under the GNU GPL v2. For full terms see the file docs/COPYING.\
#  * \
#  * Sample import document for the OJS 2.x native XML import/export format. \
#  * \
#  --> '
#print preamble

#string1 = etree.tostring(issues, pretty_print = True)
#print("%s" % stringl)
#pprint.pprint(etree.tostring(issues))

#etree.dump(issues)

tree=etree.ElementTree(issues)
tree.write(outputxml, xml_declaration=True,encoding='UTF-8', method="xml" )

#text_file = open("Output.xml", "w")
#text_file.write(stringl)
#text_file.close()