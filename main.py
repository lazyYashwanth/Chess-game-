import sys
import pygame
from src.const import WIDTH, HEIGHT, SQSIZE, MAX_FPS
from src.game import Game
from src.move import Move
from src.square import Square


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()
    game = Game()

    while True:
        clock.tick(MAX_FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.reset()

            if event.type == pygame.MOUSEBUTTONDOWN:
                row = event.pos[1] // SQSIZE
                col = event.pos[0] // SQSIZE
                piece = game.board.piece_at(row, col)
                if piece and piece.color == game.turn:
                    moves = game.board.valid_moves(piece, row, col)
                    piece.add_moves(moves)
                    game.dragger.save_initial(event.pos)
                    game.dragger.drag_piece(piece)
                    game.dragger.update_mouse(event.pos)

            elif event.type == pygame.MOUSEMOTION:
                if game.dragger.dragging:
                    game.dragger.update_mouse(event.pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                if game.dragger.dragging:
                    game.dragger.update_mouse(event.pos)
                    released_row, released_col = game.dragger.get_square_under_mouse()
                    initial = Square(game.dragger.initial_row, game.dragger.initial_col)
                    final = Square(released_row, released_col)
                    move = Move(initial, final)
                    piece = game.dragger.piece
                    if move in piece.moves:
                        captured = game.board.move(piece, move)
                        piece.clear_moves()
                        game.play_sound(captured)
                        game.next_turn()
                game.dragger.undrag_piece()

        game.show_bg(screen)
        game.show_moves(screen)
        game.show_pieces(screen)
        game.show_dragged(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
