import Biom_table
import math

class Diversity(Biom_table.Biom_table):

    """
    To initialize class input a biom_table class
    """

    
    def __init__(self,a_biom_table):
        Biom_table.Biom_table.__init__(self,a_biom_table)
        #self.abundance=a_biom_table.tax_abundance('p')
        self.abundance=self.tax_abundance()

    def __str__(self):
        return ("This is a diversity class")

    def richness(self,taxonomy='s'):
        """
        Returns the number of different species in the sample
        """
        return len(self.tax_abundance(taxonomy))

    def shannon_index(self,taxonomy='s'):
        """
        Calculates shannon index (H) of sample
        H=-SUM(pi*ln(pi))
        """
        H=0
        for data in self.tax_abundance(taxonomy):
            H+=data[1]/100*math.log(data[1]/100)
        return round(-H,2)

    def simpson_index(self,taxonomy='s'):
        """
        Calculates simpson index (D) of sample
        D= 1-SUM(pi^2)
        """
        D=0
        for data in self.tax_abundance(taxonomy):
            D+=math.pow(data[1]/100,2)
        
        return round(1-D,2)

    def jaccard_index(self,abundance_2,taxonomy='s'):
        """
        Takes a list of species abundances for another sample and calculates the jaccard index
        for both samples. Jaccard index represents the similarity of species and their abundance
         present in two samples. 
         J = U*V/(U+V-UV)
         U = sum of abundances of shared species from sample 1
         V = sum of abundances of shared species from sample 2
        """

        U=0
        V=0

        for species_1 in self.tax_abundance(taxonomy):
            for species_2 in abundance_2:
                if species_1[0]==species_2[0]:
                    U+=species_1[1]/100
                    V+=species_2[1]/100
        if U==0 or V==0:
            raise Exception("There are no shared species from these two samples")
            # print("There are no shared species from these two samples")
            # return 
        
        return round((U*V)/(U+V-U*V),2)

    def top_x_abundance(self,list_lenght,taxonomy):
        """

        list_lenght: Lenght of the list
        taxonomy: taxonomy level
        Returns a list of input lenght of top taxonomy level sorted by abundance

        """
        counter=0
        a_list=[]
        for species in self.tax_abundance(taxonomy):
            a_list.append(species)
            counter+=1
            if counter == list_lenght:
                break

        return a_list




a_name= "example1_metaphlan.txt"

#mytable = Diversity(Biom_table.Biom_table(a_name)
mytable = Diversity(a_name)

print (mytable,'\n',"Richness: ",mytable.richness(), "Shannon index: ", mytable.shannon_index(), "Simpson index: ", mytable.simpson_index())

sample2_abundance=[("Bacteroidetes", 50.00),("Proteobacteria",20.00),("Firmicutes",20.00),("Dummy",10.00)]

print("Jaccard index: ",mytable.jaccard_index(sample2_abundance, 'p'))

print('List of top 5 species sored by abundance ', mytable.top_x_abundance(5,'s'))
