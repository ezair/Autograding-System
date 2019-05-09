import java.util.NoSuchElementException;

/**
 * Thrown by a {@code Card} when its face value is out of bounds.
 *
 * @author blad
 */
public class NoSuchCardValueException extends NoSuchElementException {

  /**
   * Construct a {@code NoSuchCardValueException} with null as its message
   */
  public NoSuchCardValueException() {
    super();
  }

  /**
   * Constructs a {@code NoSuchCardValueException}, saving a reference to the
   * error message string s for later retrieval by the getMessage method.
   *
   * @param s the detail message
   */
  public NoSuchCardValueException(String s) {
    super(s);
  }

}
