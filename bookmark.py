from PyPDF2 import PdfFileReader, PdfFileWriter
from gooey import Gooey, GooeyParser
from os import path


def parse_bookmarks(raw: str, skip: int = 0, separator: str = '\t') -> dict:
    parsed = {}

    for i, line in enumerate(raw.splitlines()):
        line = line.strip()
        # skip empty lines and comments
        if not line or line.startswith('#'):
            continue

        title, _, page_num = line.partition(separator)

        if not (title or page_num):
            raise SyntaxError(f'Invalid entry at line #{i + 1}')

        try:
            page_num = int(page_num)
        except ValueError:
            raise SyntaxError(f'Invalid page number at line #{i + 1}')

        parsed[page_num + skip] = title
    return parsed


def get_parser() -> GooeyParser:
    parser = GooeyParser(description='Creates bookmarks for PDFs')
    parser.add_argument('-i', '--input',
                        metavar='Input path',
                        help='Path for the input file',
                        required=True,
                        widget='FileChooser')
    parser.add_argument('-o', '--output',
                        metavar='Save path',
                        widget='FileSaver',
                        help='Path for the output file')
    parser.add_argument('-b', '--bookmark',
                        metavar='Bookmarks path',
                        help='Path for the bookmark list',
                        required=True,
                        widget='FileChooser')
    option_group = parser.add_argument_group('Options')
    option_group.add_argument('--skip',
                              metavar='Skip pages',
                              help='How many pages should be skipped until page #s start?',
                              type=int,
                              default=0,
                              gooey_options={'columns': 2})
    option_group.add_argument('--separator',
                              metavar='Separator',
                              help='Separator between titles and page #s',
                              type=str,
                              default='\t',
                              gooey_options={'columns': 2})
    return parser


@Gooey(program_name='PDF Bookmarker')
def main():
    args = get_parser().parse_args()
    input_path, output_path = args.input, args.output
    bookmarks_path, separator, skip = args.bookmark, args.separator, args.skip

    with open(bookmarks_path, mode='r', encoding='utf-8') as bs:
        bookmarks_raw = bs.read()
    try:
        # allow escaped sequences in separator argument
        # https://stackoverflow.com/a/4020824/5298150
        separator = bytes(separator, encoding='utf-8').decode('unicode_escape')
        bookmarks = parse_bookmarks(bookmarks_raw,
                                    separator=separator,
                                    skip=skip)
    except SyntaxError:
        print(f'Error occurred while parsing bookmarks.')
        raise

    input_pdf = PdfFileReader(open(input_path, 'rb'))
    bookmarked_pdf = add_bookmarks(input_pdf, bookmarks)

    if not output_path:
        # append '__bookmarked' to filename
        output_path = '{0}__bookmarked{1}'.format(*path.splitext(input_path))
    with open(output_path, 'wb') as pdf_out:
        bookmarked_pdf.write(pdf_out)

    print('Done.')


def add_bookmarks(input_pdf: PdfFileReader, bookmarks: dict) -> PdfFileWriter:
    bookmarked_pdf = PdfFileWriter()
    for i, page in enumerate(input_pdf.pages):
        bookmarked_pdf.addPage(page)
        curr_page = i + 1
        try:
            title = bookmarks[curr_page]
            bookmarked_pdf.addBookmark(title=title, pagenum=i)
        except KeyError:
            pass
    return bookmarked_pdf


if __name__ == '__main__':
    main()
