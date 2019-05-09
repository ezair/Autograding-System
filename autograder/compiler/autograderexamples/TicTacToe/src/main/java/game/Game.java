package game;

import ai.AI;
import board.Board;
import exception.BoardIndexOutOfRange;
import exception.InvalidPlayerException;

import java.util.Scanner;

/**
 * Created by blad on 3/18/15.
 */
public class Game {
  public static void main(String[] args) throws BoardIndexOutOfRange, InvalidPlayerException {
    Scanner keyboard = new Scanner(System.in);
    Board board = new Board();
    AI ai = new AI();
    while (!board.gameOver()) {
      System.out.println(board);
      System.out.print("Row Col> ");
      int row = keyboard.nextInt();
      int col = keyboard.nextInt();
      board = board.makeMove(Board.XMark, row, col);
      if (board.win(Board.XMark)) {
        System.out.println("You win!");
        break;
      } else if (board.catsGame()) {
        System.out.println("It is a tie.");
        break;
      }
      board = ai.whichMove(Board.OMark, board);
      if (board.win(Board.OMark)) {
        System.out.println("You lose!");
        break;
      }
    }
  }
}
