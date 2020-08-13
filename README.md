# simbuild2018_for_OJS
Simbuild 2018 papers in endnote XML format and python scripts for uploading to OJS

The python script reads the endnote XML format and generates an OJS XML file that can be used with OJS bulk journal upload.

The OJS bulk upload will create a new "journal", add the papers with the metadata in the OJSXML file and will download the PDF file from a web site and add to the OJS archive

Here is a link to the instructions for importing bulk data to OJS
https://docs.pkp.sfu.ca/importing-exporting/en/

General instructions:

1) Use a citation manager to create the main entries for the paper.  Zotero and Mendeley seem to work better than endnote at autopopulating title, authors, abstracts, etc

2) Export as an endnote XML format database with the PDFs

3) Do bulk editing of endnote XML file using search and replace with the XML tags as desired

4) Put the directory of the PDFs in a publicly accessible location (I use a public github repository)

5) Edit the convert_to_OJSXML.py file to the proper URL were the papers are found and can be downloaded directly and filename of the endnote XML file

6) run the convert_to_OJSXML.py file to generate the OJS format XML

7) log into OJS and feed the OJS XML file to the bulk journal upload module
