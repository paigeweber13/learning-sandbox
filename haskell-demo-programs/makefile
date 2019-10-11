STACK_ARGS=
GHC_ARGS=-o $(PROGRAM).bin $(PROGRAM).hs

compile:
	stack $(STACK_ARGS) ghc -- $(GHC_ARGS)

run:
	stack $(STACK_ARGS) ghc -- $(GHC_ARGS) && ./$(PROGRAM).bin

make run-all:
	for prog in IODemo ControlStructuresDemo DataStructuresDemo ; do \
		make run PROGRAM=$$prog; \
	done
