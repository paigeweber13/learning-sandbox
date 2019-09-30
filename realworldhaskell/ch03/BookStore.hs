-- BookInfo is the type constructor and Book is the value constructor
-- type constructors are used in type declarations and type signatures. Value
-- constructors are used to create actual values. This is what is most commonly
-- used.
data BookInfo = Book Int String [String]
                deriving (Show)

-- here we use the value constructor Book to create the variable myInfo
myInfo = Book 123456789 "Unauthorized Autobiography"
         ["Richard Bird", "Riley Weber"]

data MagazineInfo = Magazine Int String [String]
                    deriving (Show)

-- this is an example of how you use a type constructor
-- it is very common for the type constructor and value constructor to have the
-- same name, as the set of cases where you use a type constructor and the set
-- of cases where you use a value constructor are disjoint
data BookReview = BookReview BookInfo CustomerID String

-- now using type synonyms to make BetterReview more readable than BookReview
type CustomerID = Int
type ReviewBody = String

data BetterReview = BetterReview BookInfo CustomerID ReviewBody

-- type synonyms can also be used to make shorter names for a type:
type BookRecord = (BookInfo, BookReview)

-- this is an example of an algebraic data type: a data type that has more than
-- one value constructor.
-- these value constructors can take zero or more arguments.
-- CashOnDelivery takes zero
-- CreditCard takes three
type CardHolder = String
type CardNumber = String
type Address = [String]

data BillingInfo = CreditCard CardNumber CardHolder Address
                 | CashOnDelivery
                 | Invoice CustomerID
                   deriving (Show)
