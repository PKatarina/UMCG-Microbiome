import BiomTable_class
import Pie_chart
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
    #print(BT_test.tax_richness('phylum'))
    #print(BT_test.tax_richness('g'))

def BiomTable_pie_chart_tester():

    PC_test = BiomTable_class.BiomTable("example1_metaphlan.txt")
    Pie_chart.pie_chart_drawer(PC_test,'Abundance')
    Pie_chart.pie_chart_drawer(PC_test, 'Richness', 'p')

def BiomTable_box_plot_tester():

    BP_test = Box_plot.box_plot_drawer('database',5,'Richness')

def Diversity_class_tester():

    DC_test = Diversity_class.Diversity ("example1_metaphlan.txt")

    print(DC_test)
    print('Richness: ', DC_test.richness(), '\nShannon_index: ', DC_test.shannon_index(),
          "\nSimpson_index: ", DC_test.simpson_index())
    example_sample2 = BiomTable_class.BiomTable("example2_metaphlan.txt")
    print("Jaccard_index: ",DC_test.jaccard_index(example_sample2.tax_abundance('species')))
    list_lenght = 5
    print("Top {} taxonomy groups".format(list_lenght), DC_test.top_x_abundance(list_lenght))
    print(DC_test.tax_richness())

def PathwayTable_class_tester():

    PT_test = PathwayTable_class.PathwayTable("example1_pathabundance.tsv")
    print('String Representation', PT_test)
    print('Pathway table (list representation)', PT_test.get_rows())
    print('Total abundance: ', PT_test.get_total_abundance())
    print('Merge_sort function: ', PT_test.merge_sort(PT_test.get_rows()))
    print('Top pathways: ', PT_test.get_top_pathways(6))


BiomTable_pie_chart_tester()
#BiomTable_class_tester()
#BiomTable_box_plot_tester()
#Diversity_class_tester()
#PathwayTable_clas_tester()