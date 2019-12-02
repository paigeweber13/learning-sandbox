module Main where

myDist :: Double -> Double
myDist x
  | x < 0 = 0
  | 2 < x = 0
  | otherwise = 0.5

poly :: Double -> Double -> Double
poly c x = x ** 2 + c

main = do
  putStrLn (show (myDist 0.2))
  putStrLn show (poly 3 4)
  let poly2 = poly 3
  putStrLn (show (poly2 4))
