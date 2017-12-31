

class Combinaison():

    """
    Considérant un tableau de dimension MxN
    Ce programme détermine un ensemble de combinaison de cellule d'un tableau
    Où chaque combinaison contient M éléments
    Sans repetition de la valeur de la ligne d'une cellule
    Sans repetition de la valeur de la colonne d'une cellule
    Sans mention d'une liste de valeur préalablement interdite.
    """

    def __init__(self, col, row, prohibited_positions):
        """
        Creation du tableau de base.
        le nombre de ligne est nécessairement supérieur ou egal au nombre de colonne

        :param col: int
        :param row: int
        :param prohibited_positions: liste de tuple tel que [(x, y)] où x correspond à l'indice
                                    de la colonne et y à l'indice de la ligne de la cellule
        """
        self.col = col
        table = {}

        for element in range(col):
            temp = []
            for item in range(row):
                if (element, item) not in prohibited_positions:
                    temp.append(item)

            table[element] = temp

        self.table = table

    def new_table(self, position, table):

        result = {}
        for element in table.keys():
            temp = []
            if element != position[0]:
                for item in table[element]:
                    if item != position[1]:
                        temp.append(item)
            result[element] = temp
        return result

    def run(self, table, previous, col, p):

        first_col = self.get_first_col(table)
        if first_col:
            for element in first_col[1]:
                position = (first_col[0], element)
                value = *p, position
                table_2 = self.new_table(position, table)
                if len(value) == col+1:
                    print(value)
                self.run(table_2, position, col, value)

    def get_first_col(self, table):
        for i in range(len(table)):
            if len(table[i]) > 0:
                return i, table[i]

    def start(self):

        table = self.table
        init_position = (0, 0)
        table = self.new_table(init_position, table)
        self.run(table, init_position, self.col, init_position)


# Combinaison(3, 3, []).start()