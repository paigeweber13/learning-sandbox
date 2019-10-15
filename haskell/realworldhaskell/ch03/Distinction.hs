-- these two tuples, a and b, have the same type
a = ("Porpoise", "Grey")
b = ("Table", "Oak")

-- however, these two algebraic data types have different types, despite being
-- structurally equivalent.
data Cetacean = Cetacean String String
data Furniture = Furniture String String

c = Cetacean "Porpoise" "Grey"
d = Furniture "Table" "Oak"

-- this is useful because we can leverage the type system to ensure that we are
-- passing correct data to a function. you wouldn't want to send a function
-- data about a table if it was expecting data about a porpoise, but with the
-- tuple implementation above, the compiler would allow that without raising an
-- error.
