import csv


class PathwayTable:

    """
    A class for opening pathway files
    """

    def __init__(self, table_name):
        self.table = table_name
        self.rows = []
        self.total_abundance = 0
        with open(self.table) as csvfile:
            spamreader = csv.reader(csvfile, delimiter='\t')
            for line in spamreader:
                if "PWY" in line[0] and '|' not in line[0]:
                    self.rows.append(line)
                    self.total_abundance += float(line[1])

        self.UNSORTED_LIST = list(self.rows)

    def __str__(self):
        """
        Returns a string representation of the table name
        """
        return str(self.table)

    def get_total_abundance(self):
        """
        :return: sum of the abundance
        """
        return round(self.total_abundance, 2)

    def get_top_pathways(self, list_lenght):
        """
        :param list_lenght: int
        :return:  list of top pathways lenght of list_lenght param
        """

        top_pathways = []
        for idx in range(list_lenght):
            top_pathways.append(self.rows[idx])

        return top_pathways

    def get_rows(self):
        """
        Returns the table rows as a list of lists
        """
        return self.rows
