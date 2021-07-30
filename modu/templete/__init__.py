from common.menu import print_menu
from modu.templete.basic_plot import plot_show, plot_two_list_show, plot_legend, plot_color, plot_linestyle, plot_scatter
from modu.templete.changed_temperatures_on_my_birthday import ChangedTemperaturesOnMyBirthday

if __name__ == '__main__':
    while 1:
        menu = print_menu(
            ['exit', 'Plot Show', 'Plot_two_list_show', 'scatter', 'Blank', 'ChangedTemperaturesOnMyBirthday'])
        if menu == 0:
            break
        if menu == 1:
            plot_show()
        if menu == 2:
            plot_two_list_show()
        if menu == 3:
            plot_scatter()

        if menu == 4:
            pass
        if menu == 5:
            ChangedTemperaturesOnMyBirthday().processing()
