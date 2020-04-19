import matplotlib.pyplot as plt

TAX_DICT = {'kingdom': 'k', 'phylum': 'p', 'class': 'c',
            'order': 'o', 'family': 'f', 'genus': 'g',
            'species': 's', 'strain': 't'}


def data_chart_drawer(a_biom_table, chart_type, graph_type='bar', taxonomy='p'):
    """
    Input table and tax level on witch you want to make a pie chart
    """
    global TAX_DICT
    taxonomy_shortcode = ''

    if taxonomy in TAX_DICT or taxonomy in TAX_DICT.values():
        if len(taxonomy) > 1:
            taxonomy_shortcode = TAX_DICT[taxonomy]
        elif len(taxonomy) == 1:
            taxonomy_shortcode = taxonomy
    else:
        raise NameError("Invalid taxonomy level name input")

    label = []
    size = []
    data_set = []
    other = 0
    fig, ax = plt.subplots()

    if chart_type == 'Abundance':
        data_set = a_biom_table.tax_abundance(taxonomy)
    elif chart_type == 'Richness':
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
        ax.set_ylabel(chart_type)
        ax.set_xlabel(list(TAX_DICT.keys())[list(TAX_DICT.values()).index(taxonomy_shortcode)].capitalize())

    name = graph_type.capitalize() + " chart - " + chart_type + " data "
    ax.set_title(name)
    fig.tight_layout()

    plt.show()
