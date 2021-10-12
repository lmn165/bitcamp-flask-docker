<<<<<<< HEAD:lecture/titanic/__init__.py
from lecture.titanic.legacy.templates.plot import Plot
=======
from lecture.titanic.templates.plot import Plot
>>>>>>> 35435834777e479117f611cc4465f5fe32d2ce9b:titanic/__init__.py

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