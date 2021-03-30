package main

import (
	"fmt"
	"os/exec"
	"regexp"
  "strconv"
  "time"
)

type GPUState struct {
  Id int
  Name string
  Temp int
  Fan int
  Usage int
  Power int
  Memory int
}

func main() {
  WAIT_TIME := 2 * time.Second
  CSV_HEADER := "gpu_id,gpu_name,temp_c,fan_percent,usage_percent,power_w," +
    "memory_MiB"

  regexpIdName := regexp.MustCompile(`\+=+\|\n\| +(\d+) +((?:(?:\w+) )+)`)
  regexpTemp := regexp.MustCompile(`(\d+)C`)
  regexpFanUsage := regexp.MustCompile(`(\d+)%`)
  regexpPower := regexp.MustCompile(`(\d+)W /`)
	regexpMemory := regexp.MustCompile(`(\d+)MiB /`)

  fmt.Println(CSV_HEADER)

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

    parseErrors := []error{}
    gpuCurrentId, err := strconv.ParseInt(matchesIdName[1], 0, 0)
    parseErrors = append(parseErrors, err)
    gpuCurrentTemp, err := strconv.ParseInt(matchesTemp[1], 0, 0)
    parseErrors = append(parseErrors, err)
    gpuCurrentFan, err := strconv.ParseInt(matchesFan[1], 0, 0)
    parseErrors = append(parseErrors, err)
    gpuCurrentUsage, err := strconv.ParseInt(matchesUsage[1], 0, 0)
    parseErrors = append(parseErrors, err)
    gpuCurrentPower, err := strconv.ParseInt(matchesPower[1], 0, 0)
    parseErrors = append(parseErrors, err)
    gpuCurrentMemory, err := strconv.ParseInt(matchesMemory[1], 0, 0)
    parseErrors = append(parseErrors, err)

    for _, err := range parseErrors {
      if err != nil {
        fmt.Printf("ERROR: while parsing: %v\n", err)
      }
    }

    currentState := GPUState{
      Id:     int(gpuCurrentId),
      Name:   matchesIdName[2],
      Temp:   int(gpuCurrentTemp),
      Fan:    int(gpuCurrentFan),
      Usage:  int(gpuCurrentUsage),
      Power:  int(gpuCurrentPower),
      Memory: int(gpuCurrentMemory),
    }

    fmt.Printf("Current state: %#v\n", currentState)

    time.Sleep(WAIT_TIME)
	}
}
