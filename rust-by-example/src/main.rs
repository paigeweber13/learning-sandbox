use std::io;

mod ch1 {
    pub mod formatted_print;
    pub mod debug;
    pub mod display;
    pub mod testcase_list;
    pub mod formatting;
}

fn main() {
    if ask_to_continue("ch1") { ch1_code(); }
}

fn ask_to_continue(example_info: &str) -> bool {
    println!("Would you like to run examples from {}?", example_info);
    let mut input = String::new();

    match io::stdin().read_line(&mut input) {
        Ok(_) => {
            if input.trim().to_lowercase() == "y" { 
                println!("skipping...");
                true 
            }
            else { 
                println!("skipping...");
                false
            }
        },
        Err(_) => {
            println!("error with input, skipping");
            false
        },
    }
}

fn ch1_code() {
    println!("formatted print demo:");
    ch1::formatted_print::formatted_print();
    println!();

    println!("debug derivation demo:");
    ch1::debug::debug();
    println!();

    println!("display implementation demo:");
    ch1::display::display();
    println!();

    println!("testcase with list:");
    ch1::testcase_list::testcase_list();
    println!();

    println!("advanced formatting including hex:");
    ch1::formatting::formatting();
    println!();
}
