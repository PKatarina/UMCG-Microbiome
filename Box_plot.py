import Biom_table
import os
import matplotlib.pyplot as plt


def box_plot_drawer(sample_dir,sample_number,tax_group='s'):
    """
    The function opens a directory with metaphlan data. 
    First function argument is directory name.
        Metaphlan files have to be named eg. example1_metaphlan.txt with the changeing indecies.
    Second argument is the sample number.


    sample_dir: directory name
    sample_number: contains the number of samples
    tax_group: shortcode for taxonomy level
    """
    col=[]

    for idx in range (1,sample_number +1):
        name="example{index}_metaphlan.txt".format(index=idx)
        path= os.path.join(sample_dir,name)
        a_biom_table=Biom_table.Biom_table(path)
        if idx == 1: 
            for species in a_biom_table.tax_abundance(tax_group):
                col.append([species[0],[species[1]]])

        else:
            for species in a_biom_table.tax_abundance(tax_group):
                for idx in col:
                    if species[0]==idx[0]:
                        idx[1].append(species[1])
    
    data=[]
    label=[]
    for columns in col:
        if len(columns[1]) == sample_number :
            print (columns)
            data.append(columns[1])
            label.append(columns[0])
           
    fig1,ax1 = plt.subplots()  
    ax1.set_title("Abundance Boxplot") 
    ax1.boxplot(data,labels=label)  
    plt.setp(ax1.get_xticklabels(), rotation=30, horizontalalignment='right')
    plt.tight_layout()
    

    plt.show()
    
#Calling the function
box_plot_drawer("database",5)
