import org.junit.Before;
import org.junit.Test;

import java.util.Arrays;
import java.util.List;
import java.util.Random;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

public class DeckTest {
  private static final int TEST_SEED = 1502770669;
  private Deck deck;

  @Before
  public void setUp() throws Exception {
    deck = new Deck(new Random(TEST_SEED));
  }

  @Test
  public void testDeckConstructor() throws Exception {
    assertNotNull("Problem with Deck()", deck);
    assertEquals("New deck.size != 52", Deck.CARDS_IN_A_FULL_DECK, deck.size());
  }

  @Test
  public void testOrderOfTheDeck() throws Exception {
    List<Card> expectedDeck = Arrays.asList(
        new Card(13, Card.Suit.Spade),
        new Card(4, Card.Suit.Club),
        new Card(10, Card.Suit.Club),
        new Card(8, Card.Suit.Club),
        new Card(5, Card.Suit.Diamond),
        new Card(3, Card.Suit.Spade),
        new Card(7, Card.Suit.Club),
        new Card(9, Card.Suit.Diamond),
        new Card(3, Card.Suit.Heart),
        new Card(3, Card.Suit.Diamond),
        new Card(12, Card.Suit.Spade),
        new Card(13, Card.Suit.Club),
        new Card(2, Card.Suit.Heart),
        new Card(5, Card.Suit.Spade),
        new Card(2, Card.Suit.Diamond),
        new Card(11, Card.Suit.Diamond),
        new Card(5, Card.Suit.Club),
        new Card(7, Card.Suit.Heart),
        new Card(9, Card.Suit.Heart),
        new Card(6, Card.Suit.Heart),
        new Card(8, Card.Suit.Spade),
        new Card(6, Card.Suit.Spade),
        new Card(6, Card.Suit.Club),
        new Card(4, Card.Suit.Spade),
        new Card(6, Card.Suit.Diamond),
        new Card(8, Card.Suit.Heart),
        new Card(4, Card.Suit.Diamond),
        new Card(1, Card.Suit.Club),
        new Card(12, Card.Suit.Diamond),
        new Card(10, Card.Suit.Heart),
        new Card(1, Card.Suit.Diamond),
        new Card(9, Card.Suit.Club),
        new Card(3, Card.Suit.Club),
        new Card(1, Card.Suit.Spade),
        new Card(13, Card.Suit.Diamond),
        new Card(7, Card.Suit.Spade),
        new Card(11, Card.Suit.Spade),
        new Card(13, Card.Suit.Heart),
        new Card(10, Card.Suit.Spade),
        new Card(10, Card.Suit.Diamond),
        new Card(11, Card.Suit.Heart),
        new Card(12, Card.Suit.Club),
        new Card(2, Card.Suit.Spade),
        new Card(9, Card.Suit.Spade),
        new Card(12, Card.Suit.Heart),
        new Card(1, Card.Suit.Heart),
        new Card(4, Card.Suit.Heart),
        new Card(11, Card.Suit.Club),
        new Card(7, Card.Suit.Diamond),
        new Card(2, Card.Suit.Club),
        new Card(8, Card.Suit.Diamond),
        new Card(5, Card.Suit.Heart)
    );
    int cardCount = 0;
    while (deck.size() > 0)
      assertEquals("Deck order changed.", expectedDeck.get(cardCount++), deck.deal());
  }

  @Test(expected = DeckUnderflowException.class)
  public void testDeckUnderflow() throws Exception {
    // Empty the deck
    while (deck.size() > 0)
      deck.deal();
    // Deal one more
    deck.deal();


  }
}