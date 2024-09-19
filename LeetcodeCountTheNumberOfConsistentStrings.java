import java.util.HashMap;
import java.util.Map;

public class LeetcodeCountTheNumberOfConsistentStrings {
    public int countConsistentStrings(String allowed, String[] words) {
        Map<Character,Integer> charMap = new HashMap<>();
        for (char c : allowed.toCharArray()) {
            charMap.put(c, 1);
        }
        int count = 0;
        for (String string : words) {
            for (char c : string.toCharArray()) {
                if (!charMap.containsKey(c)) {
                    count++;
                    break;
                }
            }
        }
        return words.length - count;
    }
}