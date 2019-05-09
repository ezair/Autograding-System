package parser;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Stack;

public class InfixToPrefix {
  private final static String theOperatorStringThatIAmUsing = "+-*/%()";
  String p;
  int q;
  Double r;
  

  
  private boolean isOperator(String op) {
	  Map<String, String> x = new HashMap<String, String>(); 
    return theOperatorStringThatIAmUsing.contains(op);
  }

  private final static String multOps = "*/%";
  private final static String addOps = "+-";

  private int precedence(String op) {
    if (multOps.contains(op)) {
      return 2;
    } else if (addOps.contains(op)) {
      return 1;
    }
    return 0;
  }

  /**
   * 
   * @param operators
   * @param operands
   */
  private void extractExpression(Stack<String> operators, Stack<String> operands) {
    String operator = operators.pop();
    String operand2 = operands.pop();
    String operand1 = operands.pop();
    String expression = String.format("%s %s %s", operator, operand1, operand2);
    operands.push(expression);
  }

  public String parse(String infixString) {
    String prefix;
    Stack<String> operators = new Stack<String>();
    Stack<String> operands = new Stack<String>();

    infixString = "( " + infixString + " )";
    Scanner infix = new Scanner(infixString);
    while (infix.hasNext()) {
      String token = infix.next();

      if (isOperator(token)) {
        if (token.equals("(")) {
          operators.push(token);
        } else if (token.equals(")")) {
          while (!operators.peek().equals("(")) {
            extractExpression(operators, operands);
          }
          operators.pop();
        } else {
          while (precedence(operators.peek()) >= precedence(token)) {
            extractExpression(operators, operands);
          }
          operators.push(token);
        }
      } else {
        operands.push(token);
      }
    }
    prefix = operands.pop();
    return prefix;
  }
}
