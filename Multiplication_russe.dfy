method mulitplicationRusse(x:nat,y:nat) returns (m:nat)
ensures m==x*y{
    var a := x;
    var b := y;
    var r := 0;
    while(a>0)
        invariant a>=0
        invariant r+a*b == x*y
        decreases a
    {
        if(a%2 == 0){
            b:=2*b;
            a:=a/2;
        }else{
            r:=r+b;
            a:=a-1;
        }
    }
    m:=r;
}