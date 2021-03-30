package main

import (
	"fmt"
	"os/exec"
	"regexp"
  "time"
)

type GPUState struct {
  Id uint
  Name string
  Temp int
  Fan int
  Power int
  Memory int
}

func main() {
  WAIT_TIME := 2 * time.Second

  regexpIdName := regexp.MustCompile(`\+=+\|\n\| +(\d+) +((?:(?:\w+) )+)`)
  regexpTemp := regexp.MustCompile(`(\d+)C`)
  regexpFanUsage := regexp.MustCompile(`(\d+)%`)
  regexpPower := regexp.MustCompile(`(\d+)W /`)
	regexpMemory := regexp.MustCompile(`(\d+)MiB /`)

	for {
    cmdNvidiaSmi := exec.Command("/usr/bin/nvidia-smi")
		outputBytes, err := cmdNvidiaSmi.Output()
		if err != nil {
			fmt.Printf("Error running command `%v`\n", cmdNvidiaSmi.String())
			fmt.Printf("Error was: %v\n", err)
		}
    output := string(outputBytes)

		matchesIdName := regexpIdName.FindStringSubmatch(output)
		matchesTemp := regexpTemp.FindStringSubmatch(output)
		matchesFanUsage := regexpFanUsage.FindAllStringSubmatch(output, 2)
    matchesFan := matchesFanUsage[0]
    matchesUsage := matchesFanUsage[1]
		matchesPower := regexpPower.FindStringSubmatch(output)
		matchesMemory := regexpMemory.FindStringSubmatch(output)

    allMatches := [][]string{
      matchesIdName, matchesTemp, matchesFan, matchesUsage, matchesPower,
      matchesMemory}

    for _, matches := range allMatches {
      fmt.Println("Got matches!")
			for i, match := range matches {
        fmt.Printf("Match %v: %v\n", i, match)
			}
      fmt.Println()
    }

    time.Sleep(WAIT_TIME)
	}
}
