var surv =10
var hyd=11
var cad =9
var ma =9
var mom =11
var tran = 9
var results = []
var moms=[]
var hyds =[]
var trans=[]
var cads =[]
var mas =[]
var survs=[]
for(var i =7;i<=7;i++){
    for(var j =8;j<=8;j++){
        for(var k =10;k<=10;k++){
            for(var l =6;l<=8;l++){
                for(var m =8;m<=8;m++){
                    for(var n =7;n<=7;n++){
                        var grad = i*surv + j*hyd + k*cad + l*ma + mom*m + tran*n
                        var res = grad/59
                        if(res>=7.5){
                            moms.push(m)
                        trans.push(n)
                        cads.push(k)
                        mas.push(l)
                        survs.push(i)
                        hyds.push(j)
                        results.push(res)
                        }
                        
                    }
                }
            }
        }
    }   
}
console.log("MOM  TRANS  CADS  MAS  SURv  hyds  res")
for(var p =0;p<results.length;p++){
    var st = (moms[p]) + "    " + (trans[p]) + "     " + (cads[p]) + "       " + (mas[p])+ "     " + (survs[p]) + "     " + (hyds[p]) + "     " + (results[p])
    console.log(st)
    
}