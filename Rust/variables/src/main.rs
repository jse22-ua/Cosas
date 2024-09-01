fn main() {
    let x = 5; //variable inmutable
    let mut y = 42; //variable mutable
    y = y + 1;
    const PI: f32 = 3.14159;//constante float de 32
    let j: i64 = 45;
    let f: u64 = 52; //unsigned of 64 bits
    let b: bool = false; //boolean
    println!("{},{},{}",f,j,b); 
    /*
    i será entero 
    f será float 
    32 serán los bits que utiliza
    64 bits utilizados
    */
    if f > 23{//condicional
        println!("it's more than 23!");
    }else {
        println!("it's less than 23");
    }
    println!("{} y pi es esto {}",x,PI);
    println!("{}",y);

    let mut n = 0; 

    //bucles
    loop{//bucle infito
        n +=1;
        if n > 10{//que hace que salgas de el
            break;
        }
        println!("The values is {}",n);
    }

    let mut count = 0;
    //while
    while count < 50{
        if count % 5 == 0{
            println!("{}",count);
        }
        count +=1;
    }

    //for in 
    for i in 0..10{
        println!("The numbre is {}", i);
    }

    let animals = vec!["Conejo","Perro","capibara"];
    for a in animals{
        println!("The animal is {}",a);
    }

    let utensilios = vec!["Cuchara","tenedor","bara"];
    println!("with iter()");
    for h in utensilios.iter(){
        println!("The tool is {} ",h);
    }

    let animales = vec!["Con","Perro","capibara"];
    println!("with iter().enumerate()");
    for (index,j) in animales.iter().enumerate(){
        println!("The animal is {}, in position:{} ",j,index);
    }
}