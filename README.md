# PDF Bookmarker
Creates bookmarks for PDFs from a list of bookmarks.

## Install
Run `pipenv update` to install requirements and set up a virtual environment

## Usage
```commandline
# enable virtualenv
pipenv shell
# launch GUI
python bookmarks.py
# Or use CLI instead
# python bookmarks.py --ignore-gooey <ARGUMENTS>
python bookmarks.py --ignore-gooey -i input.pdf -o output.pdf -b bookmarks.txt --skip 1 --separator __
```


## Arguments
+ `-i, --input <source.pdf>` Source PDF file path. Required
+ `-b, --bookmark <bookmarks.txt>` Bookmark list file path. Required
+ `-o, --output <save.pdf>` Destination PDF file path. Optional.  
  If not specified, input filename suffixed with `__bookmarked` will be used as output filename.
+ `--skip <5>` Skip this many pages until the numeration starts. Optional    
  Use this to adjust page numbers given in TOC to actual pages in PDF.  
  For instance giving `--skip 5` creates a bookmark entry for `Chapter 1__9` at page 14.
+ `--separator <__>` Separator sequence to distinguish bookmark titles from page numbers. Optional.  
  Defaults to `\t` (tab character)

### Bookmarks file format
Bookmarks should be formatted as `<title><separator><page #>`.

```text
Cover__1
Table Of Contents__3
Foreword__4
Chapter 1__6
```

