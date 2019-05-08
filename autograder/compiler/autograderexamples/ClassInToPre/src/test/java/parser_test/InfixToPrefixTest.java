package parser_test;

import static util.collection.List;
import static org.hamcrest.CoreMatchers.equalTo;
import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.List;

import org.junit.Before;
import org.junit.Ignore;
import org.junit.Test;

import parser.InfixToPrefix;
import static org.hamcrest.text.IsEqualIgnoringWhiteSpace.equalToIgnoringWhiteSpace;

public class InfixToPrefixTest {
  private InfixToPrefix infixToPrefix;
  
  @Before
  public void initialize() {
    infixToPrefix = new InfixToPrefix();
  }  
  
  private void testResults(String infix, String expectedPrefix) {
    String result = infixToPrefix.parse(infix);
    assertThat(result, is(equalToIgnoringWhiteSpace(expectedPrefix)));    
  }
  
  @Test
  public void convertASingleLiteralFromInfixToPrefix() {
    String infix = "10";
    String expectedPrefix = "10";
    
    testResults(infix, expectedPrefix);
  }

  
  @Test
  public void convertASingleBinaryExpressionFromInfixToPrefix() {
    List<String> infixes =          List("1 + 1", "10 * 7", "100 % 19", "8 - 102", "6 / 3");
    List<String> expectedPrefixes = List("+ 1 1", "* 10 7", "% 100 19", "- 8 102", "/ 6 3");
    for (int i = 0; i != infixes.size(); ++i) {
      String infix = infixes.get(i);
      String expectedPrefix = expectedPrefixes.get(i);
      testResults(infix, expectedPrefix);
    }
  }
  
  @Test
  public void convertAMultiPrecedenceExpressionFromInfixToPrefix() {
    List<String> infixes =          List("10 * 4 + 1", "1 + 10 * 4");
    List<String> expectedPrefixes = List("+ * 10 4 1", "+ 1 * 10 4");
    for (int i = 0; i != infixes.size(); ++i) {
      String infix = infixes.get(i);
      String expectedPrefix = expectedPrefixes.get(i);
      testResults(infix, expectedPrefix);
    }
  }
  
  @Test
  public void convertExpressionsContainingParentheses() {
	    List<String> infixes =          List("10 * ( 4 + 1 )", "( 1 + 10 * 4 )", "1 + ( 4 * 9 )", "( 18 )", "5 + ( 3 * 2 )");
	    List<String> expectedPrefixes = List("* 10 + 4 1", "+ 1 * 10 4", "+ 1 * 4 9", "18", "+ 5 * 3 2");
	    for (int i = 0; i != infixes.size(); ++i) {
	      String infix = infixes.get(i);
	      String expectedPrefix = expectedPrefixes.get(i);
	      testResults(infix, expectedPrefix);
	    }
	  }
  
    
}











