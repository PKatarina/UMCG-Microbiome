import Biom_table
import matplotlib.pyplot as plt



TAX_DICT={'kingdom': 'k', 'phylum':'p','class':'c',
'order':'o', 'family':'f', 'genus': 'g', 'species':'s',
'strain':'t'}

def pie_chart_drawer(a_biom_table,taxonomy):
    global TAX_DICT
    """
    Input table and tax level on witch you want 
    to make a pie chart
    """
    plt.figure(figsize=(5,5))
    label=[]
    values=[]
    other=0
    for data in a_biom_table.tax_abundance(TAX_DICT[taxonomy]):
        if data[1] < 1.0:
            other+=data[1]
        else:
            label.append(data[0])
            values.append(data[1])
    label.append('Other')
    values.append(other)

    plt.pie(values,labels=label)

    plt.show()
    

a_name= "example1_metaphlan.txt"
mytable = Biom_table.Biom_table(a_name)

print (mytable)

pie_chart_drawer(mytable, 'phylum')
