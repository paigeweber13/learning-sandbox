module Main where

import Lib
import ParallelDemo

main :: IO ()
main = 
  do
    let size = 10000
    putStrLn "generating list with random ints of size " ++ size
    g <- newStdGen
    print . take size $ (randomRs (0, 255) g)
    putStrLn "summing a list in parallel"
