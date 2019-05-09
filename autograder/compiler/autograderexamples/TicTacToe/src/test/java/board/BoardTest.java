package board;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class BoardTest {
  private Board board;

  @Before
  public void before() {
    board = new Board();
  }

  @Test
  public void testBoardDefaultConstructor() throws Exception {
    assertNotNull(board);
  }

  @Test
  public void testBoardCopyConstructor() throws Exception {
    Board otherBoard = new Board(board);
    assertEquals(board, otherBoard);
    assertNotSame(board, otherBoard);
    int player = Board.XMark;
    for (int row = 0; row < 3; row++)
      for (int col = 0; col < 3; col++) {
        board = board.makeMove(player, row, col);
        otherBoard = new Board(board);

        assertEquals(board, otherBoard);
        assertNotSame(board, otherBoard);

        player = Board.otherPlayer(player);
      }
  }

  @Test
  public void testMakeMove() throws Exception {
    assertTrue("Problem with isEmpty", board.isEmpty());
    board = board.makeMove(1, 1, 1);
    assertFalse("Board empty after move", board.isEmpty());
  }

  @Test
  public void testIsEmpty() throws Exception {
    assertTrue("Problem with isEmpty", board.isEmpty());

  }

  @Test
  public void testFree() throws Exception {
    for (int row = 0; row < 3; row++)
      for (int col = 0; col < 3; col++) {
        assertTrue(String.format("(%d, %d) should be free.", row, col), board.free(row, col));
        board = board.makeMove(Board.OMark, row, col);
        assertFalse(String.format("(%d, %d) should NOT free.", row, col), board.free(row, col));
      }
  }

  @Test
  public void testCount() throws Exception {
    int expectedCount = 0;
    for (int row = 0; row < 3; row++)
      for (int col = 0; col < 3; col++) {
        assertEquals("Before move.", expectedCount, board.count());
        board = board.makeMove(Board.XMark, row, col);
        expectedCount++;
        assertEquals("After move.", expectedCount, board.count());
      }
  }

  @Test
  public void testCatsGame() throws Exception {
    int player = Board.XMark;
    for (int row = 0; row < 3; row++)
      for (int col = 0; col < 3; col++) {
        assertFalse("Before move.", board.catsGame());
        board = board.makeMove(player, row, col);
        player = Board.otherPlayer(player);
      }
    assertTrue("After loop.", board.catsGame());
  }

  @Test
  public void testOtherPlayer() throws Exception {
    assertEquals("otherPlayer(XMark) = OMark", Board.OMark, Board.otherPlayer(Board.XMark));
    assertEquals("otherPlayer(OMark) = XMark", Board.XMark, Board.otherPlayer(Board.OMark));

  }

  @Test
  public void testWin() throws Exception {
    int player = Board.XMark;
    for (int row = 0; row < 3; row++) {
      board = new Board();
      for (int col = 0; col < 3; col++) {
        assertFalse("No winner yet.",board.win(player));
        board = board.makeMove(player, row, col);
      }
      assertTrue(String.format("Winner %d in row %d", player, row), board.win(player));
      player = Board.otherPlayer(player);
    }

    for (int col = 0; col < 3; col++) {
      board = new Board();
      for (int row = 0; row < 3; row++) {
        assertFalse("No winner yet.", board.win(player));
        board = board.makeMove(player, row, col);
      }
      assertTrue(String.format("Winner %d in col %d", player, col), board.win(player));
      player = Board.otherPlayer(player);
    }

    board = new Board();
    for (int index = 0; index < 3; index++) {
      assertFalse("No winner yet.", board.win(player));
      board = board.makeMove(player, index, index);
    }
    assertTrue(String.format("Winner %d on major diagonal", player), board.win(player));
    player = Board.otherPlayer(player);

    board = new Board();
    for (int index = 0; index < 3; index++) {
      assertFalse("No winner yet.", board.win(player));
      board = board.makeMove(player, index, 2 - index);
    }
    assertTrue(String.format("Winner %d on minor diagonal", player), board.win(player));
    player = Board.otherPlayer(player);
  }

  private static final String cleanRep =
      "   |   |   \n" +
      "---+---+---\n" +
      "   |   |   \n" +
      "---+---+---\n" +
      "   |   |   \n";

  private static int[] cellOffsetInRep = {1, 5, 9, 25, 29, 33, 49, 53, 57};
  private static char[] cellContents = {' ', 'X', 'O'};

  private String repSet(char playerChar, int row, int col) {
    return repSet(playerChar, row, col, cleanRep);
  }

  private String repSet(char playerChar, int row, int col, String rep) {
    int offset = 3 * row + col;
    int cell = cellOffsetInRep[offset];
    return rep.substring(0, cell) + playerChar + rep.substring(cell+1);
  }

  @Test
  public void testToString() throws Exception {
    int player = Board.XMark;
    for (int row = 0; row < 3; row++) {
      board = new Board();
      String expectedString = cleanRep;
      for (int col = 0; col < 3; col++) {
        assertEquals(expectedString, board.toString());
        board = board.makeMove(player, row, col);
        expectedString = repSet(cellContents[player], row, col, expectedString);
      }
      player = Board.otherPlayer(player);
    }


  }

  @Test
  public void testEquals() throws Exception {
    Board otherBoard = new Board();
    assertEquals("Empty boards are equal", otherBoard, board);
    int player = Board.XMark;
    for (int row = 0; row < 3; row++)
      for (int col = 0; col < 3; col++) {
        board = board.makeMove(player, row, col);
        assertNotEquals(String.format("Not equals failed for \n%s", board), otherBoard, board);

        otherBoard = otherBoard.makeMove(player, row, col);
        assertEquals(String.format("Equals failed for \n%s", board), otherBoard, board);

        player = Board.otherPlayer(player);
      }
  }

  private static final int[] expectedHashes = {0, 214358881, 253333223, 255104784, 255426886, 255441527, 255444189, 255444310, 255444332, 255444333};
  @Test
  public void testHashCode() throws Exception {
    String allHashes = "";
    int hashIndex = 0;
    assertEquals("Empty board hashes to 0", expectedHashes[hashIndex++], board.hashCode());
    // allHashes = String.format("{%d",board.hashCode());
    int player = Board.XMark;
    for (int row = 0; row < 3; row++)
      for (int col = 0; col < 3; col++) {
        board = board.makeMove(player, row, col);
        assertEquals(String.format("Hash failed for \n%s", board), expectedHashes[hashIndex++], board.hashCode());
        // allHashes = String.format("%s, %d", allHashes, board.hashCode());
        player = Board.otherPlayer(player);
      }
    // allHashes += "}";
    // System.out.println(allHashes);
  }
}