/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package morse;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import javax.sound.sampled.LineUnavailableException;

/**
 *
 * @author erica
 */
public class Main {

    public static void main(String[] args) throws IOException, LineUnavailableException, InterruptedException {
        Morse codeMorse = new Morse();
        Scanner scan = new Scanner(System.in);
        BufferedReader buffer = new BufferedReader(new InputStreamReader(System.in));
        int op = -1;

        while (op != 0) {
            System.out.print("Escolha a opção:\n 1 - Digite a frase para codificar e decodificar\n "
                    + "2 - Escolha um arquivo para codificar\n "
                    + "3 - Escolha um arquivo para decodificar\n"
                    + "0 - Sair\n");
            op = scan.nextInt();
            BufferedReader buff;
            switch (op) {
                case 1:{
                    System.out.print("Digite a frase\n");
                    String message = buffer.readLine();
                    String mor = codeMorse.toMorse(message);
                    System.out.println("Codificada: " + mor);
                  //  DotsAndTraces.Som(mor);
                    String mors = codeMorse.toChar(mor);
                    System.out.println("Decodificada: " + mors);
                    break;
                }
                case 2: {
                    System.out.printf("Informe o nome de arquivo texto:\n");
                    String nome = scan.next();
                    try {
                        FileReader arq = new FileReader(nome);
                        BufferedReader lerArq = new BufferedReader(arq);
                        String linha = lerArq.readLine();
                        while (linha != null) {
                            //System.out.printf("%s\n", linha); 
                            System.out.println(codeMorse.toMorse(linha));
                            linha = lerArq.readLine();
                        }
                        arq.close();
                    } catch (IOException e) {
                        System.err.printf("Erro na abertura do arquivo: %s.\n", e.getMessage());
                    }
                    break;
                }
                case 3:{
                    System.out.printf("Informe o nome de arquivo texto:\n");
                    String nome = scan.next();
                    try {
                        FileReader arq = new FileReader(nome);
                        BufferedReader lerArq = new BufferedReader(arq);
                        String linha = lerArq.readLine();
                        while (linha != null) {
                            //System.out.printf("%s\n", linha); 
                            System.out.println(codeMorse.toChar(linha));
                            linha = lerArq.readLine();
                        }
                        arq.close();
                    } catch (IOException e) {
                        System.err.printf("Erro na abertura do arquivo: %s.\n", e.getMessage());
                    }
                    break;
                }
            }
        }
    }
}
