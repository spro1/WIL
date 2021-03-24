import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        String key;
        Object[] values;

        for(int i = 0; i < clothes.length; i++){
            key = clothes[i][1];
            map.put(key, 1);
        }

        for(int i = 0; i < clothes.length; i++){
            key = clothes[i][1];
            map.put(key, map.get(key) + 1);
        }

        values = map.keySet().toArray();
        for(Object st : values){
            answer *= map.get(st);
        }
        
        return answer - 1;
    }
}
