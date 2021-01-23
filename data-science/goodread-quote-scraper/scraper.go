package main

import(
	"fmt"
	"os"
	"regexp"
	"strings"
	"sync/atomic"
	"time"

	"github.com/gocolly/colly"
)

type Quote struct {
	quoteText string  `selector:"div.quoteText"`
	AuthorName string `selector:"div.quoteText > span.authorOrTitle"`
	WorkName string   `selector:"div.quoteText > span > a.authorOrTitle"`
}

func main() {
	const URL = "https://www.goodreads.com/author/quotes/957894.Albert_Camus"
	const maxDepth = 5
	const shortQuoteMaxLen = 59

	var numTimesFollowedNext uint32 = 0

	quoteScriptRegex := regexp.MustCompile(`(?s)(.*)\/\/<!\[CDATA\[.*`)
	authorAndWorkRegex := regexp.MustCompile(`(?s)\s?―.*`)
	whitespaceRegex := regexp.MustCompile(`\s+`)

	splitURL := strings.Split(URL, ".")
	authorName := splitURL[len(splitURL) - 1]

	quoteFileName := authorName + "_quotes.txt"
	quoteFile, err := os.OpenFile(quoteFileName, os.O_WRONLY|os.O_CREATE, 0644)
	if err != nil {
		fmt.Printf("ERROR: unable to open file '%v' for writing\n", quoteFileName)
		return
	}

	shortQuoteFileName := authorName + "_short_quotes.txt"
	shortQuoteFile, err := os.OpenFile(shortQuoteFileName, os.O_WRONLY|os.O_CREATE, 0644)
	if err != nil {
		fmt.Printf("ERROR: unable to open file '%v' for writing\n", shortQuoteFileName)
		return
	}

	// Instantiate default collector
	c := colly.NewCollector(
		// not working for some reason?
		// colly.MaxDepth(1),

		// Visit only domains
		colly.AllowedDomains("www.goodreads.com"),

		// do parallel
		colly.Async(true),
	)

	// limit to 2 threads, one request per second
	c.Limit(&colly.LimitRule{
		DomainGlob: "*", 
		Parallelism: 2,
		RandomDelay: 1 * time.Second,
	})

	// On every a element which has href attribute call callback
	c.OnHTML("a.next_page[href]", func(e *colly.HTMLElement) {
		atomic.AddUint32(&numTimesFollowedNext, 1)
		if numTimesFollowedNext >= maxDepth { return }

		link := e.Attr("href")

		// Print link
		fmt.Printf("Link found: %q -> %s\n", e.Text, link)

		// Visit link
		c.Visit(e.Request.AbsoluteURL(link))
	})

	c.OnHTML("div.quoteText", func(e *colly.HTMLElement) {
		fullQuote := e.Text

		match := quoteScriptRegex.FindStringSubmatch(fullQuote)
		if match != nil {
			fullQuote = match[1]
		}

		fullQuote = whitespaceRegex.ReplaceAllString(fullQuote, " ")
		fullQuote = strings.Trim(fullQuote, " ")

		quote := authorAndWorkRegex.ReplaceAllString(fullQuote, "")
		quote = strings.Trim(quote, `"“”`)

		quoteFile.WriteString(fullQuote + "\n")
		if len(quote) <= shortQuoteMaxLen {
			shortQuoteFile.WriteString(quote + "\n")
		}


		// works for everything except quote text.... unfortunate
		/*
		var quote Quote
		err := e.Unmarshal(&quote)
		if (err != nil){
			fmt.Println("ERROR unmarshalling element:", err)
		}

		fmt.Println("Unmarshalled element:")
		fmt.Printf("%#v\n", quote)
		fmt.Println()
		*/
	})

	// Before making a request print "Visiting ..."
	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Saving quotes on webpage", r.URL.String())
	})

	// Set error handler
	c.OnError(func(r *colly.Response, err error) {
		fmt.Println("Request URL:", r.Request.URL, "failed with response:", r, "\nError:", err)
	})

	c.Visit(URL)
	c.Wait()
}
