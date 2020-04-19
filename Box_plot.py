import BiomTable_class
import matplotlib.pyplot as plt


def box_plot_drawer(sample_dir, sample_number, chart_type, taxonomy='p'):
    """
    The function opens a directory with metaphlan data. 
    First function argument is directory name.
    Metaphlan files have to be named eg. example1_metaphlan.txt with the changeing indecies.
    Second argument is the sample number.

    :param sample_number: contains the number of samples
    :param taxonomy: shortcode for taxonomy level
    :type sample_dir: directory name
    """
    col = []

    for idx in range(1, sample_number + 1):
        data_set = []
        name = "example{index}_metaphlan.txt".format(index=idx)
        path = sample_dir + '/' + name
        a_biom_table = BiomTable_class.BiomTable(path)

        if chart_type == 'Abundance':
            data_set = a_biom_table.tax_abundance(taxonomy)
        elif chart_type == 'Richness':
            data_set = a_biom_table.tax_richness(taxonomy)

        if idx == 1:
            for species in data_set:
                col.append([species[0], [species[1]]])

        else:
            for species in data_set:
                for jdx in col:
                    if species[0] == jdx[0]:
                        jdx[1].append(species[1])

    data = []
    label = []
    for columns in col:
        if len(columns[1]) == sample_number:
            print(columns)
            data.append(columns[1])
            label.append(columns[0])

    fig1, ax1 = plt.subplots()
    ax1.set_title(chart_type + " Boxplot")
    ax1.boxplot(data, labels=label)
    plt.setp(ax1.get_xticklabels(), rotation=30, horizontalalignment='right')
    plt.tight_layout()

    plt.show()
