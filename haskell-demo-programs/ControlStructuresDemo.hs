module Main where

import System.Environment

-- if/then/else blocks should be used for a single binary condition
exampleIf :: Bool -> String
exampleIf a = 
  if a
  then "you gave me something true!"
  else "you gave me something false!"

exampleGuards :: Char -> String
exampleGuards input
  | input == 'a' = "first letter"
  | input == 'b' = "second letter"
  | input == 'c' = "third letter"
  | input == 'd' = "fourth letter"

exampleCases :: Int -> Int
exampleCases x = 
  case x of
    -1 -> 0
    0  -> 0
    1  -> 0
    2  -> 1
    10 -> 3
    20 -> 4
    30 -> 5
    _ -> exampleCases (div x 2)

main = 
  do
    putStrLn "In Haskell, if statements are used for a single binary condition"
    putStrLn "Demoing if:"
    putStrLn "running with input 'true'"
    putStrLn (exampleIf True)
    putStrLn "running with input 'false'"
    putStrLn (exampleIf False)
    putStrLn ""

    putStrLn "Guards are much more common, and they are very similar to"
    putStrLn "if/else blocks in other languages. While Haskell does support"
    putStrLn "if/else blocks, they are syntactically difficult and uncommon."
    putStrLn "Demoing guards:"
    putStrLn "running with input 'a'"
    putStrLn (exampleGuards 'a')
    putStrLn "running with input 'b'"
    putStrLn (exampleGuards 'b')
    putStrLn "running with input 'c'"
    putStrLn (exampleGuards 'c')
    putStrLn "running with input 'd'"
    putStrLn (exampleGuards 'd')
    putStrLn ""

    putStrLn "caste statements are also possible, and are used for piecewise"
    putStrLn "functions or to take advantage of enumerability"
    putStrLn "Demoing cases:"
    putStrLn "running with input 10"
    print (exampleCases 10)
    putStrLn "running with input 30"
    print (exampleCases 30)
    putStrLn "running with input 60"
    print (exampleCases 60)
    putStrLn "running with input 200"
    print (exampleCases 200)
    putStrLn ""
