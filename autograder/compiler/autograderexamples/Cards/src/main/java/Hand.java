import java.util.ArrayList;

public class Hand {

  // hand of cards
  private ArrayList<Card> hand;

  // empty hand construct
  public Hand() {
    hand = new ArrayList<Card>();
  }

  // adds specified card
  public void add(int value, Card.Suit suit) {
    Card card = new Card(value, suit);
    hand.add(card);
  }

  // returns size of hand
  public int size() {
    return hand.size();
  }

  // removes given card
  public void remove(int index) {
    hand.remove(index);
  }

  // returns card at given index
  public Card retrieve(int index) {
    return hand.get(index);
  }

  // returns index of given card
  public int indexFinder(Card card) {
    return hand.indexOf(card);
  }

}