package util;

import java.util.Arrays;
import java.util.List;

/**
 * Named in opposition to standard naming practice: begins with a lowercase
 * letter to make the static import read better.
 * 
 * @author blad
 * 
 */
public class collection {
  /**
   * Take an arbitrary number of objects as parameters and return a list
   * containing the objects. Generic to derive the type from the context. This
   * method is named funny as per the original
   * 
   * http://gleichmann.wordpress.com/2008/01/13/building-your-own-literals-in-java-lists-and-arrays/ 
   * 
   * so that the static import looks like the import of a class List from the package
   * collection.
   * 
   * @param elems
   *          elements to place in the list
   * @returns a List<T> object containing the elements.
   */
  public static <T> List<T> List(T... elems) {
    return Arrays.asList(elems);
  }
}