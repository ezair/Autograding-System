import java.util.Random;

import static java.lang.Thread.sleep;

/**
 * A Deck of cards.
 * Created by blad on 1/13/15.
 */
public class Deck {
  /**
   * Number of cards in a deck
   */
  public static final int CARDS_IN_A_FULL_DECK = 52;
  /**
   * Delay when updating the deck contents
   */
  private static final long UPDATE_DELAY_MILLISECONDS = 250;
  /**
   * Random number generator for shuffling
   */
  private final Random random;
  /**
   * The current contents of the deck
   */
  private final Card[] deck;
  /**
   * The number of cards still in play in the deck.
   */
  private int cardCount;

  /**
   * Construct a new Deck of cards with the given Random number generator.
   *
   * @param random the random number generator to use in this deck
   */
  public Deck(Random random) {
    this.random = random;
    this.deck = new Card[CARDS_IN_A_FULL_DECK];
    populate();
    shuffle();
  }

  /**
   * Construct a new Deck of cards with a new Random number generator.
   */
  public Deck() {
    this(new Random());
  }

  /**
   * Add one deck of cards to the current contents of the deck.
   */
  private void populate() {
    cardCount = 0;
    for (Card.Suit suit : Card.Suit.values()) {
      for (int face = 1; face < 14; face++) {
        Card card = new Card(face, suit);
        deck[cardCount++] = card;
      }
    }
  }

  /**
   * Shuffle the current contents of the deck. From end of array down to location 1
   * swap the given card with a randomly selected location below the current
   * location. Can stop when index is 0 because there is nowhere to swap the one card.
   */
  private void shuffle() {
    for (int i = size() - 1; i > 0; i--) {
      int exchange = random.nextInt(i + 1);
      Card temp = deck[i];
      deck[i] = deck[exchange];
      deck[exchange] = temp;
    }
  }

  /**
   * The current size of the deck
   *
   * @return number of cards remaining in the deck
   */
  public int size() {
    return cardCount;
  }


  /**
   * Returns the card from the top of the deck.
   *
   * @return Card from top of the deck.
   * @throws DeckUnderflowException if called when the deck is empty.
   */
  public Card deal() throws DeckUnderflowException {

    if (size() > 0) {
      // Pre-decrement the number of cards in the deck
      int myCardNdx = cardCount;
      myCardNdx -= 1;
      long time = System.currentTimeMillis() + UPDATE_DELAY_MILLISECONDS;
      try {
        sleep(250);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
      cardCount = myCardNdx;
      return deck[myCardNdx];
    }
    throw new DeckUnderflowException();
  }
}
