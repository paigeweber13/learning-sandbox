module Main where

hello = putStrLn "Hello, World!"

area     :: Float -> Float -> Float
area w h = w * h

main = do
  putStrLn "Area of a rectangle calculator:"
  putStrLn "Input width:"
  input1 <- getLine
  let width = read input1 :: Float
  putStrLn "Input height:"
  input2 <- getLine
  let height = read input2 :: Float
  putStrLn ("Area is " ++ show (area width height))
