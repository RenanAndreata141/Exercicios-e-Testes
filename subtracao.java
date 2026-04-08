/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package calculadora;
import java.util.Scanner;
/**
 *
 * @author alunocmc
 */
public class Calculadora {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        System.out.println("Digite o primeiro numero");
        Scanner entrada = new Scanner(System.in);
        int Entrada1 = entrada.nextInt();
        
        System.out.println("Digite o segundo numero");
        Scanner entrada2 = new Scanner(System.in);
        int Entrada2 = entrada2.nextInt();   
        
       attributs resultadoAdicao = new adicao(2, 3);
    
       resultadoAdicao.setNum(Entrada1);
       resultadoAdicao.setNum2(Entrada2);
       resultadoAdicao.verificaInteiroECalcula();
        
       attributs resultadoSubtracao = new subtracao(2, 3);
       
       resultadoSubtracao.setNum(Entrada1);
       resultadoSubtracao.setNum2(Entrada2);
       resultadoSubtracao.verificaInteiroECalcula();
       
               
       attributs resultadoDivisao = new divisao(2, 3);
       
       resultadoDivisao.setNum(Entrada1);
       resultadoDivisao.setNum2(Entrada2);
       resultadoDivisao.verificaInteiroECalcula();
       
       attributs resultadoMultiplicacao = new multiplicacao(2, 3);
       
       resultadoMultiplicacao.setNum(Entrada1);
       resultadoMultiplicacao.setNum2(Entrada2);
       resultadoMultiplicacao.verificaInteiroECalcula();
       
       attributs resultadoSqrt = new sqrt(2, 3);
       
       resultadoSqrt.setNum(Entrada1);
       resultadoSqrt.verificaInteiroECalcula();
       
       attributs[] attributs = {resultadoAdicao, resultadoSubtracao, resultadoDivisao, resultadoMultiplicacao, resultadoSqrt};
       for(attributs a : attributs){
           System.out.println("Seu primeiro numero e "+ a.getNum());
           System.out.println("Seu segundo numero e "+ a.getNum2());
           System.out.println("Seu primeiro numero e "+ a.getResultado());
           System.out.println("________________________________");
       }
    
    }
   
    
}
