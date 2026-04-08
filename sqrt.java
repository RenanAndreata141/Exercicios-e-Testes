/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package calculadora;

/**
 *
 * @author alunocmc
 */
public class attributs {
    protected int num;
    protected int num2;
    protected double resultado;

    public attributs(int num, int num2){
        this.num = num;
        this.num2 = num2;
    }
    public int getNum(){
        return num;
    }
    public void setNum(int num){
        this.num = num;
    }
    public int getNum2(){
        return num2;
    }
    public void setNum2(int num2){
        this.num2 = num2;
    }
    public double getResultado(){
        return resultado;
    }
    
    public void verificaInteiroECalcula(){
    }
    }
