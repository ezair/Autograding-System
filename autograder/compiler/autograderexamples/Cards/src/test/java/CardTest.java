import org.junit.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.*;

/**
 * @author blad
 */
public class CardTest {
  @Test
  public void testCardConstructor() throws Exception {
    int faceValue = 2;
    Card.Suit suit = Card.Suit.Spade;
    Card card = new Card(faceValue, suit);
    assertNotNull("Card() returned null", card);
    assertEquals("Expected face value mismatch", faceValue, card.value);
    assertEquals("Expected suit value mismatch", suit, card.suit);
  }

  @Test(expected = NoSuchCardValueException.class)
  public void testCardValueOutOfRange() throws Exception {
    int badFaceValue = 0;
    Card.Suit suit = Card.Suit.Spade;
    Card evilCard = new Card(badFaceValue, suit);
    System.out.println(evilCard);
  }

  @Test
  public void testCardToString() throws Exception {
    List<String> faceValues = Arrays.asList("XX", " A", " 2", " 3", " 4", " 5", " 6",
        " 7", " 8", " 9", "10", " J", " Q", " K");
    for (Card.Suit suit : Card.Suit.values())
      for (int face = 1; face < 14; face++) {
        String expectedString = String.format("%s %s", faceValues.get(face), suit);
        Card card = new Card(face, suit);

        assertEquals("Card.toString not correct", expectedString, card.toString());
      }
  }

  @Test
  public void testCardEqualsAndHash() throws Exception {
    Card sevenClub_1 = new Card(7, Card.Suit.Club);
    Card sevenClub_2 = new Card(7, Card.Suit.Club);
    Card sevenHeart = new Card(7, Card.Suit.Heart);
    Card sixClub = new Card(6, Card.Suit.Club);

    assertEquals("!sevenClub.equals(sevenClub)", sevenClub_1, sevenClub_1);
    assertEquals("!sevenClub.equals((other) sevenClub)", sevenClub_1, sevenClub_2);
    assertNotEquals("sevenClub.equals(null)", sevenClub_1, null);
    assertNotEquals("sevenClub.equals(sevenHeart)", sevenClub_1, sevenHeart);
    assertNotEquals("sevenClub.equals(sixClub)", sevenClub_1, sixClub);

    assertEquals("sevenClub.hash != sevenClub.hash", sevenClub_1.hashCode(), sevenClub_1.hashCode());
    assertEquals("sevenClub.hash != (other) sevenClub.hash", sevenClub_1.hashCode(), sevenClub_2.hashCode());
    assertNotEquals("sevenClub.hash == sevenHeart.hash", sevenClub_1.hashCode(), sevenHeart.hashCode());
    assertNotEquals("sevenClub.hash == sixClub.hash", sevenClub_1.hashCode(), sixClub.hashCode());
  }
}
