package calculatorproj;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculatorController {
    private CalculatorView view;
    private CalculatorModel model;
    private boolean isnum1selected = true;

    public CalculatorController(CalculatorView view, CalculatorModel model){
        this.view = view;
        this.model = model;

        this.view.getadd_b1().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                performOperation("add");
            }
        });

        this.view.getSubtract_b1().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                performOperation("subtract");
            }
        });

        this.view.getMultiply_b1().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                performOperation("multiply");
            }
        });

        this.view.getDivide_b1().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                performOperation("divide");
            }
        });

        for(JButton numButton : this.view.getNum_b1()){
            numButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    JButton source = (JButton) e.getSource();
                    append_num(source.getText());
                }
            });
        }

        this.view.getSwitchInput_b1().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                toggleinputfield();
            }
        });

        this.view.getClear_b1().addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                clearAll();
            }
        });
    }

    private void performOperation(String operation){
        try{
            double num1 = Double.parseDouble(view.getNum1().getText());
            double num2 = Double.parseDouble(view.getNum2().getText());
            double result = 0;

            switch(operation){
                case "add":
                    result = model.add(num1,num2);
                    break;
                case "subtract":
                    result = model.subtract(num1,num2);
                    break;
                case "multiply":
                    result = model.multiply(num1,num2);
                    break;
                case "divide":
                    result = model.divide(num1,num2);
                    break;
            }

            view.getResult().setText(Double.toString(result));

        }catch (NumberFormatException ex){
            view.getResult().setText("Invalid Input!");
        }
        catch (ArithmeticException ex){
            view.getResult().setText(ex.getMessage());
        }
    }

    public void append_num(String num){
        if(isnum1selected){
            view.getNum1().setText(view.getNum1().getText()+num);

        }else{
            view.getNum2().setText(view.getNum2().getText()+num);
        }
    }

    private void toggleinputfield(){
        isnum1selected = !isnum1selected;
        if(isnum1selected){
            view.getNum1().requestFocus();
        }else{
            view.getNum2().requestFocus();
        }
    }


    private void clearAll(){
        view.getNum1().setText("");
        view.getNum2().setText("");
        view.getResult().setText("");
    }
//    public void setnum1selected(boolean isnum1selected){
//        this.isnum1selected = isnum1selected;
//    }


}

