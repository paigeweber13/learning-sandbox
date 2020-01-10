mod formatted_print;
mod debug;

fn main() {
    println!("formatted print demo:");
    formatted_print::formatted_print();
    println!();

    println!("formatted print demo:");
    debug::debug();
    println!();
}
