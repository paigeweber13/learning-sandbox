use std::fmt;

struct List(Vec<i32>);

impl fmt::Display for List {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // extract the value using tuple indexing, and create a reference to
        // 'vec'. 
        let vec = &self.0;

        // '?' means return the error from the returned result if it exists,
        // otherwise continue.
        // formerly this would be written `try!(write!(f, "["));`
        write!(f, "[")?;

        // iterate over 'v' in 'vec' while enumerating the iteration cound in
        // 'count'. 
        for (count, v) in vec.iter().enumerate() {
            // For every element except the first, add a comma BEFORE writing
            // the current 'v'
            if count != 0 { write!(f, ", ")?; }
            write!(f, "{}: {}", count, v)?;
        }

        // no '?' here because we want this final fmt::Result value to be
        // returned 
        write!(f, "]")
    }
}

pub fn testcase_list() {
    let v = List(vec![1, 2, 3]);
    println!("{}", v);
}
