# libraryGenesis
Library Genesis (Libgen) is a file-sharing based shadow library website for scholarly journal articles, academic and general-interest books, images, comics, audiobooks, and magazines.
The site enables free access to content that is otherwise paywalled or not digitized elsewhere.
Libgen describes itself as a "links aggregator", providing a searchable database of items "collected from publicly available public Internet resources" as well as files uploaded "from users".

To download a book from the website you have to follow these steps:

    1. search for a book in the bar. 
        (here, the search results are limited to 25)
        (the default column is "column set default")
 
    2. after choosing from the list of results, click on one of the 'mirrors'. 

    3. this will redirect you to another page with details of the book. 

    4. click on the GET text to download the e-book. 

I have followed a similiar approach in the code:

    1. enter your book name as input.
        (search results: 25; but I have limited it to 10 in my code. i.e, 25 results are fetched(if available) and the first 10(if available) are shown to you)
        (column set is: title) 

    2. the code does everything mentioned above and provides you with the final link.
        (only provides the link that starts from 'library.lol'; of course you can include more)
 
    3. click on GET to download the file. 

#source: wikipedia

# share with other book_lover-python_coder friends. 
