/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package morse;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 *
 * @author erica
 */
public class Morse {
    private final HashMap<Character, String> codes = new HashMap<>();
    
    public Morse(){
        codes.put('a', "*-");
        codes.put('b', "-***");
        codes.put('c', "-*-*");
        codes.put('d', "-**");
        codes.put('e', "*");
        codes.put('f', "**-*");
        codes.put('g', "--*");
        codes.put('h', "****");
        codes.put('i', "**");
        codes.put('j', "*---");
        codes.put('k', "-*-");
        codes.put('l', "*-**");
        codes.put('m', "--");
        codes.put('n', "-*");
        codes.put('o', "---");
        codes.put('p', "*--*");
        codes.put('q', "--*-");
        codes.put('r', "*-*");
        codes.put('s', "***");
        codes.put('t', "-");
        codes.put('u', "**-");
        codes.put('v', "***-");
        codes.put('w', "*--");
        codes.put('x', "-**-");
        codes.put('y', "-*--");
        codes.put('z', "--**");
        codes.put('0', "-----");
        codes.put('1', "*----");
        codes.put('2', "**---");
        codes.put('3', "***--");
        codes.put('4', "****-");
        codes.put('5', "*****");
        codes.put('6', "-****");
        codes.put('7', "--***");
        codes.put('8', "---**");
        codes.put('9', "----*");
        codes.put(' ', "      ");
        
    }
    public String toMorse(String s) {
        String elem = "";
        final char[] charArray = s.toLowerCase().toCharArray();
        for (int i = 0; i < charArray.length; i++) {
            if (codes.containsKey(charArray[i])) {
                elem += codes.get(charArray[i]);
                if (i != charArray.length - 1) {
                    elem += "";
                }
            } else {
                elem += charArray[i];
            }
        }
        return elem;
    }
    
    public String toChar(String s){
        String elem = "";
        final char[] charArray = s.toCharArray();
        String str = "";
        int c = 0;
        
        for (int i = 0; i < charArray.length; i++) { 
            if (charArray[i] == ' ' && i != charArray.length - 1) {
                c++;
                if (c == 7) {
                    elem += "";
                }
                if (charArray[i + 1] != ' ') {
                    c = 0;
                }
            } else if (charArray[i] == '*' || charArray[i] == '-') {
                str += charArray[i];
                if (i == charArray.length - 1) {
                    if (getKey(str) != null) {
                        elem += getKey(str);
                        str = "";
                    }
                } else if (charArray[i + 1] == ' ') {
                    if (getKey(str) != null) {
                        elem += getKey(str);
                        str = "";
                    }
                }
            } else {
                elem += charArray[i];
            }
        }
        return elem; 
    }
    public Character getKey(String value) {
        Character key = null;
        for (Map.Entry<Character, String> entry : codes.entrySet()) {
            if (value.equals(entry.getValue())) {
                key = entry.getKey();
                break;
            }
        }
        return key;
    }
}
