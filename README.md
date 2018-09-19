# PDF Bookmarker
Parses given bookmark list and inserts bookmarks to given PDF.

## Install
Run `pipenv update` to install

## Usage
Run directly to launch GUI.  
`pipenv run python bookmarks.py`

Or specify `--ignore-gooey` to use it from commandline
`pipenv run python bookmarks.py --ignore-gooey <ARGUMENTS>`


## Arguments
+ `-i, --input <source.pdf>` Source PDF file path
+ `-o, --output <save.pdf>` Destination PDF file path
+ `-b, --bookmark <bookmarks.txt>` Bookmark list file path
+ `--skip <5>` Skip this many pages until the numeration starts.  
  Use this to adjust page numbers given in TOC to actual pages in PDF.  
  For instance giving `--skip 5` creates a bookmark entry for `Chapter 1__9` at page 14 
+ `--separator <__>` Separator sequence to distinguish bookmark titles from page numbers 

### Bookmarks file format
Bookmarks should be formatted as `<title><separator><page #>`

```text
Cover__1
Table Of Contents__3
Foreword__4
Chapter 1__6
```

