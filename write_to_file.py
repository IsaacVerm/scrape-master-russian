import csv


def write_phrases_to_tsv(phrases):
    print("writing phrases to tsv")

    with open('phrases.tsv', 'a') as out:
        # tsvs use tabs as separators
        tsv_writer = csv.writer(out, delimiter='\t')

        # write header
        tsv_writer.writerow(['russian', 'english'])

        # write phrases row by row
        for phrase in phrases:
            tsv_writer.writerow(phrase)
