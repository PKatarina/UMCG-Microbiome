import csv

TAX_DICT = {"kingdom": 'k', 'phylum': 'p', 'class': 'c', 'order': 'o',
            'family': 'f', 'genus': 'g', 'species': 's', 'strain': 't'}

TAX_NUM_DICT = {'k': 1, 'p': 2, 'c': 3, 'o': 4, 'f': 5, 'g': 6, 's': 7}


class BiomTable:
    """
    Class for biom tables
    """
    global TAX_DICT, TAX_NUM_DICT

    def __init__(self, table_name):
        self.abundance = []
        self.table_name = table_name
        self.table = []
        self.richness = []
        with open(self.table_name) as csvfile:
            spamreader = csv.reader(csvfile, delimiter='|')
            for line in spamreader:
                self.table.append(line)

        self.Sample_ID = self.table.pop(0)[0]

    def __str__(self):
        """
        Returns a string representation of the table name
        """
        return "Table name" + str(self.table_name)

    def get_table(self):
        """
        Returns the table rows as a list of lists
        """
        return self.table

    def tax_abundance(self, taxonomy='phylum'):
        """
        Takes a taxonomy group and returns a list of tuples
        witch contains the name of the taxonomy group and the
         respective abundance as a float
        """
        taxonomy_shortcode = ''
        if taxonomy in TAX_DICT or taxonomy in TAX_DICT.values():
            if len(taxonomy) > 1:
                taxonomy_shortcode = TAX_DICT[taxonomy]
            elif len(taxonomy) == 1:
                taxonomy_shortcode = taxonomy
        else:
            raise NameError("Invalid taxonomy level name input")

        self.abundance = []
        for lines in self.table:
            if taxonomy_shortcode == lines[-1][0]:
                # print (lines[-1])
                checker = True
                tax_name = ''
                abundance_str = ''
                for letters in lines[-1][3:]:
                    if letters == '\t':
                        checker = False
                    if checker:
                        tax_name += letters
                    elif letters != '\t':
                        abundance_str += letters
                self.abundance.append((tax_name, float(abundance_str)))

        return self.abundance

    def tax_richness(self, taxonomy='phylum'):
        """
        :param taxonomy: level of taxa
        :return: list of tuples with taxa lvl and respective number
        of species in that taxa
        """

        taxonomy_shortcode = ''
        if taxonomy in TAX_DICT or taxonomy in TAX_DICT.values():
            if len(taxonomy) > 1:
                taxonomy_shortcode = TAX_DICT[taxonomy]
            elif len(taxonomy) == 1:
                taxonomy_shortcode = taxonomy
        else:
            raise NameError("Invalid taxonomy level name input")

        if taxonomy_shortcode == 's':
            raise Exception("Can't calculate species richness")

        richness = []
        self.richness = []

        for row in self.table:
            if len(row) == TAX_NUM_DICT[taxonomy_shortcode]:
                temp = row[-1].index('\t')
                richness.append([row[-1][3:temp], 0])

        for row in self.table:
            if len(row) == TAX_NUM_DICT['s']:
                for idx in richness:
                    if row[TAX_NUM_DICT[taxonomy_shortcode]-1][3:] == idx[0]:
                        idx[1] += 1

        for data in richness:
            self.richness.append((data[0], data[1]))

        return self.richness
