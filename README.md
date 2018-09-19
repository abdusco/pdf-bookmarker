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
+ `-i, --input <source.pdf>` Source PDF file path
+ `-o, --output <save.pdf>` Destination PDF file path
+ `-b, --bookmark <bookmarks.txt>` Bookmark list file path
+ `--skip <5>` Skip this many pages until the numeration starts.  
  Use this to adjust page numbers given in TOC to actual pages in PDF.  
  For instance giving `--skip 5` creates a bookmark entry for `Chapter 1__9` at page 14.
+ `--separator <__>` Separator sequence to distinguish bookmark titles from page numbers. Defaults to `\t` (tab character)

### Bookmarks file format
Bookmarks should be formatted as `<title><separator><page #>`.

```text
Cover__1
Table Of Contents__3
Foreword__4
Chapter 1__6
```

