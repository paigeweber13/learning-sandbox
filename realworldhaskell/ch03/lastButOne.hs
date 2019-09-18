lastButOne      :: [a] -> a
lastButOne list = if null list || length list < 2
                  then last list
                  else list !! (length list - 2)