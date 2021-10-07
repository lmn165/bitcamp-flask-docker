from book_modu.basic_boxplot.models import BasicBoxplot

if __name__ == '__main__':
    basic_boxplot = BasicBoxplot()
    # basic_boxplot.show_boxplot(sorted_random_arr())
    # basic_boxplot.show_boxplot_month('08')
    # basic_boxplot.show_boxplot_all_month()
    basic_boxplot.show_boxplot_per_date('08')