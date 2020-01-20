import BiomTable_class
import math


class Diversity(BiomTable_class.BiomTable):
    """
    To initialize class input filename of a table
    """

    def __init__(self, a_biom_table):
        BiomTable_class.BiomTable.__init__(self, a_biom_table)
        self.abundance = self.tax_abundance()

    def __str__(self):
        return "This is a diversity class"

    def richness(self, taxonomy='s'):
        """
        Returns the number of different species in the sample
        """
        return len(self.tax_abundance(taxonomy))

    def shannon_index(self, taxonomy='s'):
        """
        Calculates shannon index (H) of sample
        H=-SUM(pi*ln(pi))
        """
        h = 0
        for data in self.tax_abundance(taxonomy):
            h += data[1] / 100 * math.log(data[1] / 100)
        return round(-h, 2)

    def simpson_index(self, taxonomy='s'):
        """
        Calculates simpson index (d) of sample
        d= 1-SUM(pi^2)
        """
        d = 0
        for data in self.tax_abundance(taxonomy):
            d += math.pow(data[1] / 100, 2)

        return round(1 - d, 2)

    def jaccard_index(self, abundance_2, taxonomy='s'):
        """
        Takes a list of species abundances for another sample and calculates the jaccard index
        for both samples. Jaccard index represents the similarity of species and their abundance
         present in two samples. 
         J = u*v/(u+v-uv)
         u = sum of abundances of shared species from sample 1
         v = sum of abundances of shared species from sample 2
        """

        u = 0
        v = 0

        for species_1 in self.tax_abundance(taxonomy):
            for species_2 in abundance_2:
                if species_1[0] == species_2[0]:
                    u += species_1[1] / 100
                    v += species_2[1] / 100
        if u == 0 or v == 0:
            raise Exception("There are no shared species from these two samples")

        return round((u * v) / (u + v - u * v), 2)

    def top_x_abundance(self, list_lenght, taxonomy = 's'):
        """
        list_lenght: Lenght of the list
        taxonomy: taxonomy level
        Returns a list of input lenght of top taxonomy level sorted by abundance

        """
        counter = 0
        a_list = []
        for species in self.tax_abundance(taxonomy):
            a_list.append(species)
            counter += 1
            if counter == list_lenght:
                break

        return a_list
