import matplotlib.pyplot as plt

TAX_DICT = {'kingdom': 'k', 'phylum': 'p', 'class': 'c',
            'order': 'o', 'family': 'f', 'genus': 'g',
            'species': 's', 'strain': 't'}


def pie_chart_drawer(a_biom_table, chart_type, taxonomy="p"):
    """
        Input table and tax level on witch you want
        to make a pie chart
        """
    global TAX_DICT

    plt.figure(figsize=(6, 6))

    label = []
    sizes = []
    other = 0
    data_set = []

    if chart_type == 'Abundance':
        data_set = a_biom_table.tax_abundance(taxonomy)
    elif chart_type == 'Richness':
        data_set = a_biom_table.tax_richness(taxonomy)

    for data in data_set:
        if data[1] < 1.0:
            other += data[1]
        else:
            label.append(data[0])
            sizes.append(data[1])
    label.append('Other')
    sizes.append(other)

    plt.pie(sizes, labels=label, autopct='%1.1f%%')

    plt.show()
