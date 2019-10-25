module Main where

import Lib
import ConcurrencyDemo
import ParallelDemo
import System.Random

generateRandomList :: Int -> [Int]
generateRandomList =
  do



main :: IO ()
main = 
  do
    putStrLn "Demoing concurrency:"
    sendReceiveMessage

    putStrLn "\nDemoing parallel list summation:"
    let size = 10000
    putStrLn ("generating list with random ints of size " ++ show size)
    putStrLn "summing a list in parallel"
