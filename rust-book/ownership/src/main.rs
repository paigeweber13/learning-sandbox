fn print_thing_with_reference(s: &String){
    println!("{}", s);
}

fn print_thing(s: String){
    println!("{}", s);
}

fn main() {
    // first, let's declare a string
    let s1 = String::from("hello!");

    // if the string was passed by reference (meaning you pass a pointer so you
    // can manipulate something without giving up ownership), then the value
    // would not be moved and you could still run the `println!` after
    // print_thing. 

    print_thing_with_reference(&s1);

    println!("{}", s1);


    // if we try the same while passing the actual object, ownership is moved.

    print_thing(s1);

    // the following line would throw error[E0382]: borrow of moved value: `s1`
    // because s1 has moved to s (the parameter of print_thing). I believe rust
    // calls this "borrowing"
    // see https://doc.rust-lang.org/stable/book/ch04-01-what-is-ownership.html#ways-variables-and-data-interact-move

    // println!("{}", s1);
}
