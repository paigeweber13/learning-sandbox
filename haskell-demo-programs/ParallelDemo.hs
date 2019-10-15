module Main where

import System.Random
import Control.Parallel
import GHC.Conc (numCapabilities)

sumListParallel :: Num a => [a] -> a
sumListParallel inputList = do
  m <- newEmptyMVar
  forkIO $ do
    v <- takeMVar m
    putStrLn ("received " ++ show v)
  putStrLn "sending"
  putMVar m "wake up!"

main = 
  do
    let size = 10000
    putStrLn "generating list with random ints of size " ++ size
    g <- newStdGen
    print . take size $ (randomRs (0, 255) g)
    putStrLn "summing a list in parallel"
