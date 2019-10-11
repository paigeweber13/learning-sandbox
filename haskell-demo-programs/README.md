# Dependencies
 * GHC - these programs expect you to use the [haskell
   stack](https://docs.haskellstack.org/en/stable/README/)
 * GNU Make (optional)

# How to compile and run:
## with GNU Make:
 * `make run PROGRAM=name-of-program-no-file-extension`
 * you may also use `make run-all` to run all demos

## without GNU Make:
stack ghc -- -o IODemo.bin IODemo.hs && ./IODemo.bin  
