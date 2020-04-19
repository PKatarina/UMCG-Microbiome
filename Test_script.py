import BiomTable_class
import Data_chart
import Box_plot
import Diversity_class
import PathwayTable_class


def BiomTable_class_tester():
    BT_test = BiomTable_class.BiomTable("example1_metaphlan.txt")
    print(BT_test)
    # print(BT_test.get_table())
    print(BT_test.tax_abundance('phylum'))
    # print(BT_test.tax_abundance('asdf'))
    print(BT_test.tax_abundance('k'))
    print(BT_test.tax_richness('phylum'))
    print(BT_test.tax_richness('g'))


def BiomTable_data_chart_tester():
    PC_test = BiomTable_class.BiomTable("example1_metaphlan.txt")
    Data_chart.data_chart_drawer(PC_test, 'Abundance', graph_type= 'pie')
    #Data_chart.data_chart_drawer(PC_test, 'Abundance', taxonomy='g')


def BiomTable_box_plot_tester():
    BP_test = Box_plot.box_plot_drawer('database', 5, 'Richness')


def Diversity_class_tester():
    DC_test = Diversity_class.Diversity("example1_metaphlan.txt")

    print(DC_test)
    print('Richness: ', DC_test.richness(), '\nShannon_index: ', DC_test.shannon_index(),
          "\nSimpson_index: ", DC_test.simpson_index())
    example_sample2 = BiomTable_class.BiomTable("example2_metaphlan.txt")
    print("Jaccard_index: ", DC_test.jaccard_index(example_sample2.tax_abundance('species')))
    list_lenght = 5
    print("Top {} taxonomy groups".format(list_lenght), DC_test.top_x_abundance(list_lenght))
    print(DC_test.tax_richness())


def PathwayTable_class_tester():
    PT_test = PathwayTable_class.PathwayTable("example1_pathabundance.tsv")
    print('String Representation', PT_test)
    print('Pathway table (list representation)', PT_test.get_rows())
    print('Total abundance: ', PT_test.get_total_abundance())
    print('Top pathways: ', PT_test.get_top_pathways(6))

    for row1 in PT_test.get_table():
        print(row1[1], row1[0][0:10])

    for row2 in PT_test.get_top_pathways(10):
        print(row2)

BiomTable_data_chart_tester()
#BiomTable_class_tester()
# BiomTable_box_plot_tester()
#Diversity_class_tester()
#PathwayTable_class_tester()
