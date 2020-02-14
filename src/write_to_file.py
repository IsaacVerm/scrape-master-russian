import csv

def write_header(type):
    print(f"writing {type} header to tsv")

    with open(f"{type}.tsv", 'w') as out:
        # tsvs use tabs as separators
        tsv_writer = csv.writer(out, delimiter='\t')

        # write header
        tsv_writer.writerow(['russian', 'english'])

def write_to_tsv(type, translations):
    print(f"writing {type} to tsv")

    with open(f'{type}.tsv', 'a') as out:
        # tsvs use tabs as separators
        tsv_writer = csv.writer(out, delimiter='\t')

        # write phrases row by row
        for translation in translations:
            tsv_writer.writerow(translation)

def write_phrases_header_to_tsv():
    print("writing phrases header to tsv")

    with open('phrases.tsv', 'w') as out:
        # tsvs use tabs as separators
        tsv_writer = csv.writer(out, delimiter='\t')

        # write header
        tsv_writer.writerow(['russian', 'english'])


def write_phrases_to_tsv(phrases):
    print("writing phrases to tsv")

    with open('phrases.tsv', 'a') as out:
        # tsvs use tabs as separators
        tsv_writer = csv.writer(out, delimiter='\t')

        # write phrases row by row
        for phrase in phrases:
            tsv_writer.writerow(phrase)
