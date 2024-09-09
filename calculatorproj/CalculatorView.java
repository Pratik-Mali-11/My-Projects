package calculatorproj;

import javax.swing.*;
import java.awt.*;

public class CalculatorView extends JFrame{
    private JTextField num1 = new JTextField(10);
    private JTextField num2 = new JTextField(10);
    private JTextField result = new JTextField(10);
    private  JButton add_b1 = new JButton("+");
    private  JButton subtract_b1 = new JButton("-");
    private  JButton multiply_b1 = new JButton("*");
    private  JButton divide_b1 = new JButton("/");
    private  JButton clear_b1 = new JButton("C");

    private  JButton[] num_b1 = new JButton[10];
    private  JButton switchInput_b1 = new JButton("Switch Input");

    public CalculatorView(){
        this.setTitle("Simple calculator");

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(400,400);
        this.setResizable(false);
        this.setLocationRelativeTo(null);
        this.setLayout(new BorderLayout());

        JPanel num_panel = new JPanel();
        num_panel.setLayout(new GridLayout(4,3));

        for(int i =0 ;i<=9;i++){
            num_b1[i] = new JButton(String.valueOf(i));
            num_panel.add(num_b1[i]);
        }

        JPanel operation_panel = new JPanel();
        operation_panel.setLayout(new GridLayout(7,2));

        operation_panel.add(new JLabel("First Number: "));
        operation_panel.add(num1);

        operation_panel.add(new JLabel("Second Number: "));
        operation_panel.add(num2);

        operation_panel.add(new JLabel("Result: "));
        operation_panel.add(result);

        result.setEditable(false);

        operation_panel.add(add_b1);
        operation_panel.add(subtract_b1);
        operation_panel.add(multiply_b1);
        operation_panel.add(divide_b1);
        operation_panel.add(clear_b1);
        operation_panel.add(new JLabel(""));
        operation_panel.add(switchInput_b1);

        this.add(operation_panel, BorderLayout.NORTH);
        this.add(num_panel,BorderLayout.CENTER);
    }

    public  JTextField getNum1(){
        return num1;
    }

    public  JTextField getNum2(){
        return num2;
    }

    public  JTextField getResult(){
        return result;
    }

    public  JButton getadd_b1(){
        return add_b1;
    }

    public  JButton getSubtract_b1(){
        return subtract_b1;
    }

    public  JButton getMultiply_b1(){
        return multiply_b1;
    }

    public  JButton getDivide_b1(){
        return divide_b1;
    }

    public JButton getClear_b1(){
        return clear_b1;
    }

    public JButton[] getNum_b1(){
        return num_b1;
    }

    public JButton getSwitchInput_b1(){
        return switchInput_b1;
    }
}