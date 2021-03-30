package main

import (
  "encoding/csv"
	"fmt"
  "os"
	"os/exec"
	"regexp"
  "strings"
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
  CSV_FILE := "data/gpu-temp-log-" + time.Now().Format("2006-01-02_1504") +
    ".csv"
  CSV_HEADER := []string{"timestamp", "gpu_id", "gpu_name", "temp_c", 
    "fan_percent", "usage_percent", "power_w", "memory_MiB"}

  csv_file, err := os.Create(CSV_FILE)
  if err != nil {
    fmt.Printf("ERROR: while creating file. Error was: %v\n", err)
  }
  defer csv_file.Close()
  csv_writer := csv.NewWriter(csv_file)
  csv_writer.Write(CSV_HEADER)

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

    currentTimeString := time.Now().Format("2006-01-02_150405")
    currentId := matchesIdName[1]
    currentName := strings.Trim(matchesIdName[2], " ")
    currentTemp := matchesTemp[1]
    currentFan := matchesFan[1]
    currentUsage := matchesUsage[1]
    currentPower := matchesPower[1]
    currentMemory := matchesMemory[1]

    currentLine := []string{currentTimeString, currentId, currentName,
      currentTemp, currentFan, currentUsage, currentPower, currentMemory}
    csv_writer.Write(currentLine)
    csv_writer.Flush()

    time.Sleep(WAIT_TIME)
	}
}
