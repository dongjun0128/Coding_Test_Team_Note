import java.util.Stack;

public class StackDataStructure {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();

        // 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

        stack.push(5);
        stack.push(2);
        stack.push(3);
        stack.push(7);
        stack.pop();
        stack.push(1);
        stack.push(4);
        stack.pop();

        // 스택의 최상단 원소부터 출력
        while(!stack.empty()){
            // Stack 에서 최상단 원소를 출력할 때는 peek()사용
            System.out.println(stack.peek() +" ");
            stack.pop();
        }

    }
}
