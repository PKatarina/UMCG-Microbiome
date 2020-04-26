import matplotlib.pyplot as plt
import os
import BiomTable_class


def box_plot_drawer(samples_dir, data_type, taxonomy='phylum'):
    """
    The function opens a directory with metaphlan data. 
    First function argument is directory name.
    Metaphlan files have to be named eg. example1_metaphlan.txt
    with the changeing indecies.
    Second argument is the sample number.

    :type samples_dir: directory name
    :param data_type:
    :param taxonomy: taxonomy level
    """
    sorted_data = [[]]
    sample_number = 0
    possible_labels = []

    for file in os.listdir(os.getcwd() + '/' + samples_dir):

        data_set = []

        if 'metaphlan' and '.txt' in file:
            name = file
            path = samples_dir + '/' + name
            a_biom_table = BiomTable_class.BiomTable(path)

            if data_type == 'abundance':
                data_set = a_biom_table.tax_abundance(taxonomy)
            elif data_type == 'richness':
                data_set = a_biom_table.tax_richness(taxonomy)

            for data in data_set:
                if data[0] not in possible_labels:
                    possible_labels.append(data[0])
                    sorted_data.append([])
                sorted_data[0] = possible_labels
                sorted_data[possible_labels.index(data[0]) + 1].append(data[1])

            sample_number += 1

    box_plot_data = []
    label = []
    for idx in range(1, len(sorted_data)):
        if len(sorted_data[idx]) == sample_number:
            box_plot_data.append(sorted_data[idx])
            label.append(sorted_data[0][idx-1])

        print(sorted_data[0][idx - 1], sorted_data[idx])

    fig1, ax1 = plt.subplots()
    ax1.set_title(data_type.capitalize() + " Boxplot")
    ax1.boxplot(box_plot_data, labels=label, showmeans = True)
    plt.setp(ax1.get_xticklabels(), rotation=30, horizontalalignment='right')
    ax1.set_ylabel(data_type.capitalize())
    ax1.set_xlabel(taxonomy.capitalize())
    plt.tight_layout()

    plt.show()
