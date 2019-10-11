module Main where

main =
  do
    -- Haskell primarily uses Lists and Tuples to handle data.
    print "doing basic list operations"
    let a = [1, 2, 3] :: [Int]
    let b = [9, 8, 7] :: [Int]
    putStrLn ("a: " ++ show a)
    putStrLn ("b: " ++ show b)
    let c = a ++ b
    putStrLn ("a and b concatenated: " ++ show c)
    putStrLn ("adding another number to that list: " ++ show (19:c))
    putStrLn ""

    -- All items in a list must be the same type. Tuples, however, may have
    -- elements of different types
    putStrLn "doing basic tuple operations"
    let coordinate = ("cartesian", 2, 5)
    putStrLn ("coordinate: " ++ show coordinate)
