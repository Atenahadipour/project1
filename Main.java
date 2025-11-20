public class Main{
  pablic static int add(int a ,int b){
    if(b==0){
      return a;
    }
    return add(a+1,a-1);
    }
  public static void main(string[] args){
    System.out.println(add(3+5));
  }
}
