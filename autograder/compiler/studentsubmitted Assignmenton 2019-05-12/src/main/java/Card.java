import java.util.Arrays;
import java.util.List;

/**
 * Class for representing individual playing cards. It is an immutable class so
 * it is safe to expose public final fields.
 * <p/>
 * Ace is value 1; J, Q, K are 11, 12, 13.
 *
 * @author blad
 */
public class Card {
  /**
   * The possible face value strings; due to 0-indexing, the first entry should not be possible to get
   */
  public static final List<String> faceValues = Arrays.asList("XX", " A", " 2", " 3", " 4", " 5", " 6",
      " 7", " 8", " 9", "10", " J", " Q", " K");
  /**
   * The suit for this card.
   */
  public final Suit suit;
  /**
   * Face value of the card: Ace is value 1; J, Q, K are 11, 12, 13.
   */
  public final int value;
  /**
   * Construct a card with the given values
   */
  public Card(int value, Suit suit) {
    if (!((1 <= value) && (value <= 13))) {
      String msg = String.format("Card face value out of bounds: %d", value);
      throw new NoSuchCardValueException(msg);
    }
    this.value = value;
    this.suit = suit;
  }

  /* (non-Javadoc)
   * @see java.lang.Object#hashCode()
   */
  @Override
  public int hashCode() {
    final int prime = 31;
    int result = 1;
    result = prime * result + ((suit == null) ? 0 : suit.hashCode());
    result = prime * result + value;
    return result;
  }

  /* (non-Javadoc)
   * @see java.lang.Object#equals(java.lang.Object)
   */
  @Override
  public boolean equals(Object obj) {
    if (this == obj)
      return true;
    if (obj == null)
      return false;
    if (getClass() != obj.getClass())
      return false;
    Card other = (Card) obj;
    if (suit != other.suit)
      return false;
    if (value != other.value)
      return false;
    return true;
  }

  /* (non-Javadoc)
   * @see java.lang.Object#toString()
   */
  @Override
  public String toString() {
    return String.format("%s %s", faceValues.get(value), suit);
  }

  /**
   * Enumerated class holding the card suits.
   */
  public enum Suit {
    Spade, Heart, Club, Diamond;
  }


}
