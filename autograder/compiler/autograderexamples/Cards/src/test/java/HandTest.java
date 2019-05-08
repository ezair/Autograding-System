import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

public class HandTest {

  // testing empty hand constructor
  @Test
  public void testHandConstructor() throws Exception {
    Hand hand = new Hand();
    assertNotNull("Empty Hand constructed", hand);
  }

  // testing add and size
  @Test
  public void testAddCardToHand() throws Exception {
    int size = 2;
    Hand hand = new Hand();
    hand.add(10, Card.Suit.Spade);
    hand.add(1, Card.Suit.Heart);
    assertEquals("Expected size to be static", hand.size(), size);
  }

  // testing remove by index
  @Test
  public void testRemoveCardByIndex() {
    int size = 2;
    Hand hand = new Hand();
    hand.add(10, Card.Suit.Spade);
    hand.add(1, Card.Suit.Heart);
    assertEquals("Expected size to be static", hand.size(), size);
    hand.remove(0);
    size--;
    assertEquals("Expected size inequality", hand.size(), size);
  }

  // test retrieve by index
  @Test
  public void testRetrieveCardByIndex() {
    Hand hand = new Hand();
    Card card = new Card(1, Card.Suit.Heart);
    hand.add(1, Card.Suit.Heart);
    hand.add(1, Card.Suit.Spade);
    hand.add(1, Card.Suit.Diamond);
    assertEquals("Expected card to be different", hand.retrieve(0), card);
  }

  // test card location by index
  @Test
  public void testFindCardLocation() {
    Hand hand = new Hand();
    Card card = new Card(1, Card.Suit.Heart);
    hand.add(1, Card.Suit.Spade);
    hand.add(1, Card.Suit.Heart);
    hand.add(1, Card.Suit.Diamond);
    assertEquals("Expected card index to be different", hand.indexFinder(card), 1);
  }

}