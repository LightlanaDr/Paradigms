class TicTacToe:
    """Задача. Написать игру в “Крестики-нолики”"""
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def print_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def play(self):
        while True:
            self.print_board()
            move = input("Введите номер ячейки для вставки символа (1-9): ")
            if move.isdigit() and 1 <= int(move) <= 9 and self.board[int(move) - 1] == " ":
                self.board[int(move) - 1] = self.current_player
                if self.check_winner():
                    self.print_board()
                    print(f"Игрок {self.current_player} победил!")
                    break
                if self.draw():
                    print("Ничья!")
                    break
                self.current_player = "O" if self.current_player == "X" else "X"
            if not move.isdigit():
                print("Неверный символ! Попробуйте ещё раз.")
            else:
                print("Неверный ход! Попробуйте ещё раз.")

    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # строки
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),  # столбцы
                 (0, 4, 8), (2, 4, 6)]  # диагонали
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return True
        return False

    def draw(self):
        return " " not in self.board


if __name__ == '__main__':
    game = TicTacToe()
    game.play()
