package ai;

import board.Board;
import org.junit.Test;

import static org.junit.Assert.*;

public class AITest {

  @Test
  public void testWinInOne() throws Exception {
    Board board = new Board();
    board = board.makeMove(Board.XMark, 1, 1);
    board = board.makeMove(Board.OMark, 0, 1);
    board = board.makeMove(Board.XMark, 0, 0);
    board = board.makeMove(Board.OMark, 1, 0);
    AI ai = new AI();
    System.out.println(board + "yields\n" + ai.whichMove(Board.XMark, board));
    System.out.println(ai.root);
  }

  @Test
  public void testWinInTwo() throws Exception {
    Board board = new Board();
    board = board.makeMove(Board.XMark, 0, 0);
    board = board.makeMove(Board.OMark, 0, 1);
    board = board.makeMove(Board.XMark, 0, 2);
    board = board.makeMove(Board.OMark, 1, 0);
    AI ai = new AI();
    System.out.println(board + "yields\n" + ai.whichMove(Board.XMark, board));
    System.out.println(ai.root);
  }

  @Test
  public void testFromStart() throws Exception {
    Board board = new Board();
    AI ai = new AI();
    System.out.println(board + "yields\n" + ai.whichMove(Board.XMark, board));
  }
}