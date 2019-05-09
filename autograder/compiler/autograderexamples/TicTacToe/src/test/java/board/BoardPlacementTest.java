package board;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.Arrays;

import static org.junit.Assert.*;
import static board.Board.OMark;
import static board.Board.XMark;

@RunWith(Parameterized.class)
public class BoardPlacementTest {
  // @Parameters annotation marks this method as parameters provider
  @Parameterized.Parameters(name = "makeMove({0}, {1}, {2})")
  public static Iterable<Object []> data() {
    return Arrays.asList(new Object[][]{
        {XMark, 0, 0}, {XMark, 0, 1}, {XMark, 0, 2},
        {XMark, 1, 0}, {XMark, 1, 1}, {XMark, 1, 2},
        {XMark, 2, 0}, {XMark, 2, 1}, {XMark, 2, 2},
        {OMark, 0, 0}, {OMark, 0, 1}, {OMark, 0, 2},
        {OMark, 1, 0}, {OMark, 1, 1}, {OMark, 1, 2},
        {OMark, 2, 0}, {OMark, 2, 1}, {OMark, 2, 2}
    });
  }

  private int player;
  private int row;
  private int col;
  
  private Board board;

  public BoardPlacementTest(final int player, final int row, final int col) {
    this.player = player;
    this.row = row;
    this.col = col;
  }

  @Before
  public void setUp() throws Exception {
    board = new Board();
  }

  @Test
  public void testMoveGet() throws Exception {
    assertTrue("Board should start empty.", board.isEmpty());
    assertEquals(String.format("Location (%d, %d) should start empty.", row, col),
        Board.Empty, board.getSquare(row, col));

    board = board.makeMove(player, row, col);

    assertNotNull("Move returned null", board);
    assertFalse("Board no longer empty.", board.isEmpty());
    assertEquals(String.format("Location (%d, %d) should be %d.", row, col, player),
        player, board.getSquare(row, col));
  }

  @Test
  public void testInvalidMove() throws Exception {
    int otherPlayer = 3 - player;
    board = board.makeMove(player, row, col);
    Board triedBoard = board.makeMove(otherPlayer, row, col);
    System.out.println("board = " + board);
    System.out.println("triedBoard = " + triedBoard);

    assertNull("Second move overwrote first.", triedBoard);
    assertEquals(String.format("Location (%d, %d) should be %d.", row, col, player),
        player, board.getSquare(row, col));
  }
}