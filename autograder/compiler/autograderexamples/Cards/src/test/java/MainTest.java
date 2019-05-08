import org.junit.Test;

import static org.junit.Assert.assertNotNull;

/**
 * Test class for demonstrating TDD and testing out Main class.
 *
 * @author blad
 */
public class MainTest {
  /**
   * Test method for {@link Main#main(java.lang.String[])}.
   */
  @Test
  public void testMain() {
    Main main = new Main();
    assertNotNull("Main() returned null", main);
  }

}
