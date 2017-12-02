import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Day01 {

    public static void main(String[] args) throws FileNotFoundException {
        String input = new Scanner(new File("./input.txt")).useDelimiter("\\Z").next();
        System.out.println(inverseCaptcha(input, 1));
        System.out.println(inverseCaptcha(input, input.length() / 2));
    }
    
    private static int inverseCaptcha(String input, int inc) {
        List<Integer> data = Arrays.asList(input.split("")).stream()
          .map(x->Integer.parseInt(x))
          .collect(Collectors.toList());
        
        int N = input.length();
        return IntStream.range(0, N)
            .mapToObj(i -> new int[] { data.get(i), data.get((i + inc) % N) })
            .filter(x -> x[0] == x[1])
            .map(x -> x[0])
            .reduce(0, (a, b) -> a + b);
    }
}
