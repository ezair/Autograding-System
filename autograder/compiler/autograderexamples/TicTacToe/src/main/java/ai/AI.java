package ai;

import board.Board;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by blad on 3/18/15.
 */
public class AI {
  int playerToEvaluateFor;
  MinMaxTreeNode root;

  private class MinMaxTreeNode extends ArrayList<MinMaxTreeNode> {
    final Board state;
    final int playerToMove;
    int height;
    int value;
    MinMaxTreeNode best;

    public MinMaxTreeNode(Board state, int playerToMove) {
      super(9 - state.count());
      this.state = state;
      this.playerToMove = playerToMove;
    }

    public boolean max() {
      return this.playerToMove == playerToEvaluateFor;
    }

    public void eval(int depth) throws Exception {
      if (depth >= 0) {

        best = null;
        List<Board> successors = state.legalMovesFor(playerToMove);

        if (!successors.isEmpty()) {
          int otherPlayer = Board.otherPlayer(playerToMove);
          for (Board board : successors) {
            MinMaxTreeNode mmtn = new MinMaxTreeNode(board, otherPlayer);
            add(mmtn);
            if (board.win(playerToMove)) {
              mmtn.height = 0;
              best = mmtn;
              mmtn.value = max()?1:-1;
            } else {
              mmtn.eval(depth - 1);
              if ((best == null) ||
                  (max() && ((best.value < mmtn.value) || (best.value == mmtn.value && mmtn.height < best.height))) ||
                  (!max() && ((best.value > mmtn.value) || (best.value == mmtn.value && mmtn.height < best.height)))) {
                best = mmtn;
                height = best.height + 1;
              }
            }
          }
          value = best.value;
        } else {
          height = 0;
          if (state.catsGame())
            value = 0;
          else if (state.win(playerToEvaluateFor))
            value = 1;
          else if (state.win(Board.otherPlayer(playerToEvaluateFor)))
            value = -1;
          else
            throw new Exception("Cannot happen: No moves and no finish!");
        }
      } else {
        value = 0;
      }
    }

    @Override
    public String toString() {
      String me = "\n" + state.toString() + "\n" + height;
      String indent = "\n    ";
      for (MinMaxTreeNode childNode : this) {
        String child = childNode.toString();
        me = me + child.replaceAll("\n", indent);
      }
      return me;
    }
  }

  public Board whichMove(int playerToMove, Board current) {
    this.playerToEvaluateFor = playerToMove;
    root = new MinMaxTreeNode(current, playerToMove);
    try {
      root.eval(9);
      return root.best.state;
    } catch (Exception e) {
      e.printStackTrace();
    }
    return null;
  }
}
