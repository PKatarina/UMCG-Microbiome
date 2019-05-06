import csv
import matplotlib.pyplot as plt


TAX_DICT={'kingdom': 'k', 'phylum':'p','class':'c',
'order':'o', 'family':'f', 'genus': 'g', 'species':'s',
'strain':'t'}


class Biom_table:

    """
    Class for biom tables
    """


    def __init__(self,table_name):
        self.table=table_name
        self.rows=[]
        with open(self.table) as csvfile:
            spamreader = csv.reader(csvfile, delimiter='|')
            for line in spamreader:
                self.rows.append(line)

        self.Sample_ID=self.rows.pop(0)[0]
    

    def __str__(self):
        """
        Returns a string representation of the table name
        """
        return str(self.table)


    def get_rows(self):
        """
        Returns the table rows as a list of lists
        """
        return(self.rows)

    def tax_abundance(self,taxonomy):
        """
        Takes a taxonomy group and returns a list of tuples
        witch contains the name of the taxonomy group and the
         respective abundance as a float
        """
        self.abundance=[]
    
        for lines in self.rows:
            if taxonomy == lines[-1][0]:
                #print (lines[-1])
                checker=True
                tax_name=''
                abund_str=''
                for letters in lines[-1][3:]:
                    if letters   == '\t':
                        checker=False
                    if checker:
                        tax_name+=letters
                    elif letters != '\t':
                        abund_str+=letters
                self.abundance.append((tax_name,float(abund_str)))

        return self.abundance


