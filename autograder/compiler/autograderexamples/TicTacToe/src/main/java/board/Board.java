package board;

import exception.BoardIndexOutOfRange;
import exception.InvalidPlayerException;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by blad on 3/16/15.
 */
public class Board {
  public static final int Empty = 0;
  public static final int XMark = 1;
  public static final int OMark = 2;
  private static final int BoardBoundLow = 0;
  private static final int BoardBoundHigh = 2;
  private static final char[] convert = { ' ', 'X', 'O'};

  /* The board representation */
  private int[] board;

  /**
   * Construct a new, empty board.
   */
  public Board() {
    board = makeBoard();
  }

  /**
   * Construct a new, copied board.
   */
  public Board(Board original) {
    board = makeBoard(original.board);
  }

  /**
   * Initialize a new board to an empty state.
   *
   * @return reference to new board representation
   */
  private int[] makeBoard() {
    int[] b = new int[9];
    for (int i = 0; i < 9; ++i)
      b[i] = 0;
    return b;
  }

  /**
   * Initialize new board to match given borad.
   * @param original Board to match
   * @return reference to a new, matching representation.
   */
  private int[] makeBoard(int[] original) {
    int[] b = new int[9];
    for (int i = 0; i < 9; ++i)
      b[i] = original[i];
    return b;
  }

  /**
   * Is the cell at (row, col) empty?
   *
   * @param row 0-2 index of the row
   * @param col 0-2 index of the column
   * @return is the given cell empty?
   */
  public boolean free(int row, int col) {
    return free(offset(row, col));
  }

  /**
   * Is the cell at the given index free
   *
   * @param index offset into linear view of board
   * @return is that cell empty.
   */
  private boolean free(int index) {
    return board[index] == Empty;
  }

  /**
   * Count of occupied cells on the board.
   *
   * @return number of non-empty board cells
   */
  public int count() {
    int full = 0;
    for (int i = 0; i < 9; ++i) {
      full += free(i) ? 0 : 1;
    }
    return full;
  }

  /**
   * Does the player have a win in the given row?
   *
   * @param player player value to check
   * @param row    0-2 row number to check
   * @return true if player won in the row
   */
  private boolean rowWin(int player, int row) {
    boolean winning = true;
    for (int col = 0; col < 3 && winning; col++)
      winning &= board[offset(row, col)] == player;
    return winning;
  }

  /**
   * Does the player have a win in the given col?
   *
   * @param player player value to check
   * @param col    0-2 col number to check
   * @return true if player won in the column
   */
  private boolean colWin(int player, int col) {
    boolean winning = true;
    for (int row = 0; row < 3 && winning; row++)
      winning &= board[offset(row, col)] == player;
    return winning;
  }

  /**
   * Does the player have a win along one of the diagonals?
   *
   * @param player player value to check
   * @return true if the player won on either diagonal
   */
  private boolean diagWin(int player) {
    boolean major = true;
    boolean minor = true;
    boolean winning = major || minor;
    for (int index = 0; index < 3 && winning; index++) {
      major &= board[offset(index, index)] == player;
      minor &= board[offset(index, 2 - index)] == player;
      winning = major || minor;
    }
    return winning;
  }


  /**
   * Does the given player have a win on the board.
   *
   * @param player player to check for a win by
   * @return true if given player has won
   */
  public boolean win(int player) {
    boolean winning = false;
    for (int row = 0; row < 3 && !winning; row++)
      winning |= rowWin(player, row);
    for (int col = 0; col < 3 && !winning; col++)
      winning |= colWin(player, col);
    winning |= diagWin(player);
    return winning;
  }

  /**
   * Is the current state of the game a tie?
   *
   * @return true if there are no moves left.
   */
  public boolean catsGame() {
    return count() == 9;
  }

  /**
   * Make the move for the given player into the indicated location
   * @param player moving player
   * @param row row, 0-2, for move
   * @param col column, 0-2, for move
   * @return a new board with the move made.
   * @throws InvalidPlayerException
   * @throws BoardIndexOutOfRange
   */
  public Board makeMove(int player, int row, int col) throws InvalidPlayerException, BoardIndexOutOfRange {
    validatePlayer(player);
    validateBoardIndex(row, col);
    boolean freeToMove = free(row, col);
    if (freeToMove) {
      Board moved = new Board(this);
      moved.board[offset(row, col)] = player;
      return moved;
    }
    return null;
  }

  /**
   * Validate that the index pair is within legal bounds. Throw an exception otherwise.
   * @param row 0-2 is valid range
   * @param col 0-2 is valid range
   * @throws BoardIndexOutOfRange the board index (the row or the column) is out of range.
   */
  private static void validateBoardIndex(int row, int col) throws BoardIndexOutOfRange {
    if ((row < BoardBoundLow || BoardBoundHigh < row) ||
        (col < BoardBoundLow || BoardBoundHigh < col))
      throw new BoardIndexOutOfRange(String.format("Bad board index (%d, %d)", row, col));
  }

  /**
   * Validate that the player is either XMark or OMark.
   * @param player XMark - OMark is valid range
   * @throws InvalidPlayerException the player number is not valid
   */
  private static void validatePlayer(int player) throws InvalidPlayerException {
    if ((player != XMark) && (player != OMark))
      throw new InvalidPlayerException(String.format("Invalid player encoding %d", player));
  }

  /**
   * Get the current value in the given square
   * @param row row number, 0-2
   * @param col column number 0-2
   * @return the current content of the given square.
   * @throws BoardIndexOutOfRange
   */
  public int getSquare(int row, int col) throws BoardIndexOutOfRange {
    validateBoardIndex(row, col);
    return board[offset(row, col)];
  }

  /**
   * Convert a row, col pair to an offset into the board representation.
   *
   * @param row row number, 0-2
   * @param col column number 0-2
   * @return index 0-8 in the 1-d representation
   */
  private int offset(int row, int col) {
    return row * 3 + col;
  }

  /**
   * Is the board currently empty?
   * @return true if board is empty
   */
  public boolean isEmpty() {
    return count() == 0;
  }

  /**
   * The other player's value
   * @param player current player
   * @return player other than the current player.
   */
  public static int otherPlayer(int player) throws InvalidPlayerException {
    validatePlayer(player);
    return 3 - player;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;

    Board other = (Board) o;

    return hashCode() == other.hashCode();
   }

  public boolean gameOver() {
    return catsGame() || win(Board.XMark) || win(Board.OMark);
  }

  /**
   * Return a list of boards with each legal move the given player can make.
   * @param player the moves to make.
   * @return list of boards with legal moves made.
   */
  public List<Board> legalMovesFor(int player) {
    List<Board> successors = new ArrayList<Board>(9 - count());
    for (int i = 0; i <9; i++) {
      if (free(i)) {
        Board moved = new Board(this);
        moved.board[i] = player;
        successors.add(moved);
      }
    }
    return successors;
  }

  @Override
  public int hashCode() {
    final int prime = 11;
    int eval = 0;
    for (int i = 0; i < 9; ++i)
      eval = eval * prime + board[i];
    return eval;
  }

  @Override
  public String toString() {

    StringBuilder printable = new StringBuilder();
    String rowBefore = "";
    for (int row = 0; row < 3; row++) {
      printable.append(rowBefore);
      rowBefore = "---+---+---\n";
      String colBefore = " ";
      for (int col = 0; col < 3; col++) {
        printable.append(colBefore);
        colBefore = " | ";
        printable.append(convert[board[offset(row, col)]]);
      }
      printable.append(" \n");
    }
    return printable.toString();
  }
}
