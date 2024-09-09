package calculatorproj;

public class CalculatorMain {
    public static void main(String[] args) {
        CalculatorView view = new CalculatorView();
        CalculatorModel model1 = new CalculatorModel();

        CalculatorController controller = new CalculatorController(view,model1);

        view.setVisible(true);
    }
}