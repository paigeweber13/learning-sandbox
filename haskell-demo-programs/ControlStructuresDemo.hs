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

main = 
  do
    putStrLn "Demoing if:"
    putStrLn "running with input 'true'"
    putStrLn (exampleIf True)
    putStrLn "running with input 'false'"
    putStrLn (exampleIf False)
    putStrLn ""

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

