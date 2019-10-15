STACK_ARGS=
GHC_ARGS=-o $(PROGRAM).bin $(PROGRAM).hs

compile:
	stack $(STACK_ARGS) ghc -- $(GHC_ARGS)

run:
	stack $(STACK_ARGS) ghc -- $(GHC_ARGS) && ./$(PROGRAM).bin

make run-all:
	for filename in ./*.hs ; do \
		echo "running $$filename \n" ; \
		prog="$${filename%.*}"; \
		make run PROGRAM=$$prog; \
	  read -p "press enter to continue to the next demo..." a; \
		echo "\n"; \
	done; \
	echo "complete!";
