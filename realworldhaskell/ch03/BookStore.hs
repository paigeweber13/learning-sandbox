data BookInfo = Book Int String [String]
                deriving (Show)

data MagazineInfo = Magazine Int String [String]
                    deriving (Show)

myInfo = Book 123456789 "Unauthorized Autobiography"
         ["Richard Bird", "Riley Weber"]
