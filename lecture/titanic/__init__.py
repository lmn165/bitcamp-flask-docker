from lecture.titanic.templates.plot import Plot

if __name__ == '__main__':
    while 1:
        menu = input(f'0-Exit, 1-Visualization, 2-Modeling, 3-Machine, 4-Lenarning Machine Release')
        if menu == '0':
            break
        elif menu == '1':
            plot = Plot()
            # plot.show_plot_survived_death()
            # plot.show_plot_pclass()
            # plot.show_plot_embarked()
            # plot.show_plot_embarked_pclass()
            plot.show_plot_sex()