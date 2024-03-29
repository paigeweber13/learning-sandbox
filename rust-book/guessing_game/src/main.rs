use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("guess the number, between 1 and 100!");

    let secret_number = rand::thread_rng().gen_range(1, 100);
    // debug
    // println!("the secret number is: {}", secret_number);

    loop {
        println!("input your guess...");
        let mut guess = String::new();
        io::stdin().read_line(&mut guess)
            .expect("Failed to read line");
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("please input a number!");
                continue;
            }
        };

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            },
        }
    }
}
