from ga.chromosome_elem import ChromosomeElem
from track_generator.command import Command
from track_generator.generator import generate_track
from config import CHROMOSOME_LENGTH

import matplotlib.pyplot as plt

def Genetic_algo():
    # Optimization problem:
    #
    # Goal: Minimize Distance between Starting Point (a[0]) Ending Point (a[len(a)-1])
    #
    # Constrains:
    #  1. fix length of sequence CHROMOSOME_LENGTH
    #  2. No loop
    #  3. Start and End commands must be S
    #  4. After DY command it must be R or L
    #  5. L or R must be followed by DY or S
    #
    # Algorithm need:
    #
    # 1. Initial population:
    #
    # 2. Fitness function:
    # Min(math.sqrt((a[0].x-a[len(a)-1].x)**2 + (a[0].y-a[len(a)-1].y)**2))
    #
    # 3. Selection/filter:
    #   - No loop:
    #   Use orientation base intersection detector?
    #   - Start and End commands must be S:
    #   chromosome[0].command == Command.S && chromosome[len(chromosome)-1].command == Command.S
    #   - After DY command it must be R or L ; L or R must be followed by DY or S
    #     for(i in range(len(chromosome)-1)):
    #         if(chromosome[i].command == Command.DY
    #                 and chromosome[i+1].command != Command.L
    #                 and chromosome[i+1].command != Command.R):
    #             disgrace to the family
    #         if ((chromosome[i].command == Command.L
    #              or chromosome[i].command ==Command.R)
    #         and (chromosome[i+1].command != Command.DY
    #                 or chromosome[i+1].command != Command.S))
    #
    #
    # 4. Crossover:
    #   TBD
    #
    # 5. Mutation
    #   TBD
    #

    #first generation
    t = 0
    #optional stopping generation
    T_FINAL = 100



    return 0

if __name__ == '__main__':

    chromosome_elements = [ChromosomeElem(command=Command.S, value=11),
                           ChromosomeElem(command=Command.DY, value=15.5),
                           ChromosomeElem(command=Command.R, value=9),
                           ChromosomeElem(command=Command.S, value=10),
                           ChromosomeElem(command=Command.L, value=5)
    ]


    track_points = generate_track(chromosome_elements=chromosome_elements)

    plot_x = [track_point.x for track_point in track_points]
    plot_y = [track_point.y for track_point in track_points]
    plt.scatter(plot_x, plot_y)
    plt.show()
