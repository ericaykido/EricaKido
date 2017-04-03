/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package jogodavelha;

/**
 * 
 * Érica Yumi Kido R.A.: 13.02422-0
 * @author erica
 */
public class Jogo {
     private final char J1 = 'X';
     private final char J2 = 'O';
     private final char[][] tabuleiro;
     private int jn;
     private int contador;
     
     public int getjn(){
            return jn;
        }
     
     public Jogo() {
        this.tabuleiro = new char[3][3];
        Inicio();
    }
     
     public void Inicio(){
         for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                tabuleiro[i][j] = '0';
            }
        }
        jn = 1;
        contador = 1;
     }
     
     public String getJogador() {
        if (jn == 1){
            return J1 + "";
        } else {
            return J2 + "";
        }
     }
     public int jogada(int l){
          if (tabuleiro[(l / 3)][(l % 3)] == '0') {
            if (jn == 1) {
                tabuleiro[(l / 3)][(l % 3)] = J1;
            } else {
                tabuleiro[(l / 3)][(l % 3)] = J2;
            }
            contador++;
        }
      
        if(check()){
            return jn;  
        }
       if(contador == 10){
           return 0;
       }
       jn = jn%2 +1;
       return 3;
     }
     
     public boolean check(){
             for (int i = 0; i < 3; i++) {
                if ((tabuleiro[i][0] == tabuleiro[i][1]) && (tabuleiro[i][0] == tabuleiro[i][2]) && (tabuleiro[i][0] != '0'))                  
                    return true;
                if ((tabuleiro[0][i] == tabuleiro[1][i]) && (tabuleiro[1][i] == tabuleiro[2][i]) && (tabuleiro[0][i] != '0')) 
                    return true;
            }
            if ((tabuleiro[0][0] == tabuleiro[1][1]) && (tabuleiro[1][1] == tabuleiro[2][2])&& (tabuleiro[0][0] != '0')) 
                return true;
            return ((tabuleiro[2][0] == tabuleiro[1][1]) && (tabuleiro[1][1] == tabuleiro[0][2]));
                
            }
     
}
     

