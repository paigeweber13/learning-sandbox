module ParallelDemo where

import Control.Parallel
import GHC.Conc (numCapabilities)

sumListParallel :: Num a => [a] -> a
sumListParallel inputList = sum inputList
