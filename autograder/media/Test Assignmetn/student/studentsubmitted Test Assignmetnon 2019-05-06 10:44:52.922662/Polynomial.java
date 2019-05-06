/*
    Jared DeMarais
    CIS 203
    Section:001
    Assignment: 1
 */
public class polynomial{
    private int degree;
    private double[] coefficients;
    public polynomial(int degree,double[] coefficients){
        if(degree<=0){
        }else{
            if (coefficients.length != degree+1) {
            }else {
                if (coefficients[degree] == 0.0) {
                }else{
                    this.degree=degree;
                    this.coefficients=coefficients;
                }
            }
        }
    }
    public String toString(){
        System.out.println();
    }
    public double evaluate(double x){

    }
}