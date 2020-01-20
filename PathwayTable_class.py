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

        for lines in self.rows:
            lines.append(round(float(line[1]) / self.total_abundance, 6))

        self.UNSORTED_LIST = list(self.rows)

    def __str__(self):
        """
        Returns a string representation of the table name
        """
        return str(self.table)

    @staticmethod
    def merge(list1, list2):
        """
        Merge two sorted lists.

        Returns a new sorted list containing those elements that are in
        either list1 or list2.

        This function is iterative.

        Helper function for merge_sort
        """
        new_list = []
        while list1 != [] or list2 != []:
            if not list1:
                new_list.extend(list2)
                return new_list
            if not list2:
                new_list.extend(list1)
                return new_list
            elif list1[0][1] <= list2[0][1]:
                new_list.append(list1.pop(0))
            else:
                new_list.append(list2.pop(0))

        return new_list

    def merge_sort(self, list1):
        """
        Sort the elements of list1.

        Return a new sorted list with the same elements as list1.

        This function is recursive.
        """

        # base case
        if len(list1) <= 1:
            return list1
        else:
            return self.merge(self.merge_sort(list1[0:int(len(list1)/2)]), self.merge_sort(list1[int(len(list1) / 2):]))

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
        for idx in range(1, list_lenght+1):
            top_pathways.append(self.merge_sort(self.UNSORTED_LIST)[-idx])

        return top_pathways

    def get_rows(self):
        """
        Returns the table rows as a list of lists
        """
        return self.rows
