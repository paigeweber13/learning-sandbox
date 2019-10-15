module ParallelDemo where

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
