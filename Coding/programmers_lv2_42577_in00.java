import java.util.HashMap;

class Solution {
    public boolean solution(String[] phone_book) {
        HashMap<String, Boolean> map = new HashMap<String, Boolean>();
        boolean answer = true;
        
        for(String number : phone_book){
            map.put(number, false);
        }
        
        for(String number : phone_book){
            for(int i  = 1; i <=  number.length() ; i++){
                if(map.containsKey(number.substring(0,i))){
                    if(!map.get(number)){
                        map.put(number, true);
                    }
                    else{
                        answer = false;
                        return answer;   
                    }
                }
            }
        }
        
        return answer;
    }
}
