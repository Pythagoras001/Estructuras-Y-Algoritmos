package JAVA.Conceptos;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class PrefixSumFunciones {

    // AQUI CREAMOS UNA FUNCION QUE RETORNA UNA LISTA PREFIX SUM
    public static List<Integer> prefix(List<Integer> x){
        List<Integer> prefix = new ArrayList<>(Collections.nCopies(x.size()+1, 0));
        
        for (int i = 1; i < x.size()+1; i++) {
            prefix.set(i, prefix.get(i-1)+x.get(i-1));
        }
        return prefix;
    }
    
    public static void main(String[] args) {
        ArrayList<Integer> numeros = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5,6 ));
        
        List<Integer> prefixSum = prefix(numeros); 

        Integer ini = 0;
        Integer fin = 4;

        System.out.println(prefixSum.get(fin)-prefixSum.get(ini));
    }
}
