//Atenahadipour
//A+B
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
//A^B
public class Main{
  pablic static Long power(long a,long b){
    long resuit =1;
    for(long i=0; i<b; i++){
      resuit *=a;
    }
    return result;
  }
  public static void main(string[]args){
    System.out.println(power(3,4));
  }
}
//ragham por arzesh
public class Main{
  public static int figure(int n){
    if(n<0){
      n=-n
        }
    while(n>=10){
      n/=10;
    }
    return n;
  }
  public static void main(string[]args){
    System.out.println(figure(907));
  }
}
//jam argham
public class Main{
  public static int sum(int n){
    if(n<0){
      n=-n;
    }
    int sum =0;
    while (n>0){
      sum += n% 10;
      n/=10;
    }
    return sum;
  }
  public static void main (string[]args){
    system.out.println(sum(65))
      }
}
//ragam zoj
public class Main{
  public static int z (int n){
    if(n<0);
    n=-n;
  }
  int count =0
  while(n>0){
  int digit =n%10;
  if (digit % 2==0)
    count++
      }
  n/=10;
  }
    return count;
}
public static void Main(string[]args);
system.out.printLn(z(48291));
}
}


    
        
