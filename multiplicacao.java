package calculadora;


import calculadora.attributs;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author alunocmc
 */
public class adicao extends attributs {
    protected double resultado;
    
    public adicao(int num, int num2){
        super(num, num2);
        this.num = num;
        this.num2 = num2;
    }
    @Override
    public double getResultado(){
        return resultado;
    }
    @Override
    public void verificaInteiroECalcula(){
        if(num == Math.floor(num) || num2 == Math.floor(num2)){
            resultado = num + num2;
        }
        else{
            System.out.println("Seu numero não é inteiro");
        }
    }
}