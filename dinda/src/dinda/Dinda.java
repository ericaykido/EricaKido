/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dinda;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

/**
 *
 * @author erica
 */
public class Dinda {

    /**
     * @param args the command line arguments
     * @throws java.io.IOException
     */
    public static void main(String[] args) throws IOException {
        File contasFile = new File(".\\contas.csv");
        BufferedReader contasCSV = new BufferedReader(new FileReader(contasFile));
        String contaLinha = null;        
        String transacaoLinha = null; 

        String valFinal = "final.csv";
        FileWriter write = new FileWriter(valFinal);
       
        while(((contaLinha = contasCSV.readLine()) != null)){ 
            String[] valorCon = contaLinha.split(",");
            int con = Integer.valueOf(valorCon[1]);
            String[] idConta = valorCon;
            File transacaoFile = new File(".\\transacoes.csv");
            BufferedReader transacoesCSV = new BufferedReader(new FileReader(transacaoFile));
           
                
            while(((transacaoLinha = transacoesCSV.readLine()) != null)){
                String[] valorTran = transacaoLinha.split(",");
                int tran = Integer.valueOf(valorTran[1]);
                String[] idTransacao = valorTran;                    
                if(idConta[0].equals(idTransacao[0])){

                    int fin = con + tran;
                    if (fin < 0){
                        con -= 5;
                       // System.out.println("Multa por conta estar negativa " + con);
                        write.append(idConta[0] + "," + con + "\n");
                        write.flush();
                    }
                    else
                    {
                       // System.out.println("Valor ajustado " + fin);
                        write.append(idConta[0] + "," + fin + "\n");
                        write.flush();
                    }
                }
            }
        }                       
    contasCSV.close();
    }
}

