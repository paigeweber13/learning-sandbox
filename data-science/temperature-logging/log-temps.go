package main

import (
	"fmt"
	"os/exec"
	"regexp"
)

func main() {
	regexpTemp := regexp.MustCompile(`(\d+)C`)

	for {
    cmdNvidiaSmi := exec.Command("/usr/bin/nvidia-smi")
		output, err := cmdNvidiaSmi.Output()
		if err != nil {
			fmt.Printf("Error running command `%v`\n", cmdNvidiaSmi.String())
			fmt.Printf("Error was: %v\n", err)
		}

		matches := regexpTemp.FindSubmatch(output)

		fmt.Printf("Got matches!\n")
		for i, match := range matches {
      fmt.Printf("Match %v: %v\n", i, string(match))
		}
	}
}
