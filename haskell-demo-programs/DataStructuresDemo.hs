module Main where

doubleList :: Num a => [a] -> [a]
doubleList [] = []
doubleList (x:xs) = (x * 2) : doubleList xs

main =
  do
    putStrLn "Haskell primarily uses Lists and Tuples to handle data."
    putStrLn "doing basic list operations"
    let a = [1, 2, 3] :: [Int]
    let b = [9, 8, 7] :: [Int]
    putStrLn ("a: " ++ show a)
    putStrLn ("b: " ++ show b)
    let c = a ++ b
    putStrLn ("a and b concatenated: " ++ show c)
    putStrLn ("adding another number to that list: " ++ show (19:c))
    putStrLn ""

    putStrLn "All items in a list must be the same type. Tuples, however, may"
    putStrLn "have elements of different types. For example:"
    let coordinate = ("cartesian", 2, 5)
    putStrLn ("coordinate: " ++ show coordinate)
    putStrLn "tuples are immutable, so there isn't much we can do here..."

    putStrLn "here are some operations on lists:"
    let d = [1, 0, -61, 43]
    putStrLn "we can use recursion to double all elements in a list:"
    let e = doubleList d
    putStrLn ("original list: " ++ show d)
    putStrLn ("doubled list: " ++ show e)

