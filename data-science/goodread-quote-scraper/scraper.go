package main

import(
	"fmt"
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
	// quoteCleaner := strings.NewReplacer

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
		// Visit link found on page
		// Only those links are visited which are in AllowedDomains
		c.Visit(e.Request.AbsoluteURL(link))
	})

	c.OnHTML("div.quoteText", func(e *colly.HTMLElement) {
		// fmt.Println("found quote:")
		// fmt.Printf("quote text: %#v\n\n", e.Text)
		// fmt.Printf("e.dom: %#v\n\n", e.DOM)
		// fmt.Printf("e: %#v\n\n", e)
		// fmt.Println()

		fullQuote := e.Text

		match := quoteScriptRegex.FindStringSubmatch(fullQuote)
		// fmt.Printf("match object: %#v\n", match)
		if match != nil {
			fullQuote = match[1]
			// fmt.Println("Regex matched")
			// fmt.Printf("Entire match is: %#v\n", match[0])
			// fmt.Printf("First group is: %#v\n", match[1])
		}

		fullQuote = whitespaceRegex.ReplaceAllString(fullQuote, " ")
		fullQuote = strings.Trim(fullQuote, " ")
		quote := authorAndWorkRegex.ReplaceAllString(fullQuote, "")
		quote = strings.Trim(quote, `"“”`)
		shortQuote := quote
		if len(shortQuote) <= shortQuoteMaxLen {
			// fmt.Println("WARN: truncated quote")
			shortQuote = quote[:shortQuoteMaxLen]
		} else {
			fmt.Printf("short quote text: %v\n", shortQuote)
		}

		// fmt.Printf("full quote text: %v\n", fullQuote)
		// fmt.Printf("quote text: %v\n", quote)
		// fmt.Printf("short quote text: %v\n", shortQuote)

		// var unmarshalledMap interface{}

		// err := colly.UnmarshalHTML(&quote, e)

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
		fmt.Println("Visiting", r.URL.String())
	})

	// Set error handler
	c.OnError(func(r *colly.Response, err error) {
		fmt.Println("Request URL:", r.Request.URL, "failed with response:", r, "\nError:", err)
	})

	c.Visit(URL)
	c.Wait()
}
