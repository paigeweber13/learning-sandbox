mod formatted_print;
mod debug;
mod display;
mod testcase_list;

fn main() {
    println!("formatted print demo:");
    formatted_print::formatted_print();
    println!();

    println!("debug derivation demo:");
    debug::debug();
    println!();

    println!("display implementation demo:");
    display::display();
    println!();

    println!("testcase with list:");
    testcase_list::testcase_list();
    println!();
}
