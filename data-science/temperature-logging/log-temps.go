package main

import (
	"fmt"
	"os"
	"os/exec"
	"regexp"
)

func main() {
	cmdNvidiaSmi := &exec.Cmd {
		Path: "/usr/bin/nvidia-smi",
		Args: []string{},
		Stdout: os.Stdout,
		Stderr: os.Stdout,
	}
	regexpTemp := regexp.MustCompile(`(\d+)C`)

	for {
		output, err := cmdNvidiaSmi.Output()
		if err != nil {
			fmt.Printf("Error running command `%v`\n", cmdNvidiaSmi.String())
			fmt.Printf("Error was: %v\n", err)
		}

		matches := regexpTemp.FindSubmatch(output)

		fmt.Printf("Got matches!\n")
		for i, match := range matches {
			fmt.Printf("Match %v: %v\n", i, match)
		}
	}
}
