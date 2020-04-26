import matplotlib.pyplot as plt

def biom_chart_drawer(a_biom_table, data_type, graph_type='bar', taxonomy='phylum'):
    """
    Input table and tax level on witch you want to make a pie chart
    """

    label = []
    size = []
    data_set = []
    other = 0
    fig, ax = plt.subplots()

    if data_type == 'abundance':
        data_set = a_biom_table.tax_abundance(taxonomy)
    elif data_type == 'richness':
        data_set = a_biom_table.tax_richness(taxonomy)

    for data in data_set:
        if data[1] < 1.0:
            other += data[1]
        else:
            label.append(data[0])
            size.append(data[1])
    label.append('Other')
    size.append(other)

    if graph_type == 'pie':
        ax.pie(size, labels=label, autopct='%1.1f%%')
    elif graph_type == 'bar':
        ax.bar(label, size)
        plt.xticks(rotation=45)
        ax.set_ylabel(data_type)
        ax.set_xlabel(taxonomy.capitalize())

    name = graph_type.capitalize() + " chart - " + data_type.capitalize() + " data "
    ax.set_title(name)
    fig.tight_layout()

    plt.show()
