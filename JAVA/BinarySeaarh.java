package JAVA;

import java.util.ArrayList;
import java.util.Arrays;

public class BinarySeaarh {
    public static void main(String[] args) {
        
        ArrayList<Integer> numeros = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));

        Integer target = 3;

        Integer iz = 0;
        Integer der = numeros.size()-1;

        while (iz <= der) {
            Integer mid = (iz + der) / 2;
            Integer act = numeros.get(mid);

            if (act == target){
                System.out.println(mid);
                break;
            } else if (act > target){
                der = mid-1;
            } else{
                iz = mid+1;
            }
            if (iz > der){
                System.out.println("NO EXISTE TAL NUMERO EN LA LISTA");
            }
    
        }
    }
}
