# legal-work
Fun non-sus code *wink*
Wrote using knowledge from my networking class!

# How it works
To find the destination IP address:
  I used dns dig just because I wanted to explore all possibilities for the IP.
  You may use ping as well.

Find src IP (my IP). Use a VPN.

## the `hive` function:
  1. creates a socket object
  2. connects to website given IP, port
  3. you can now send requests and receive data!
  4. send get request for webpage (byte data)
  5. close socket (yay, less resources!)
  6. if this fails, try again bwahaha

## `main` function:
  1. loop `hive` function
  2. basically sends a bunch of concurrent GET requests to webpage

## DISCLAIMER
Do not use this to actually DDoS a website. It's CRIMINAL. 
This is also meant for a low security/scaled website -- I'm sure you big corpo websites have measures in place to prevent such simple attacks. E.g. creating multiple servers so that if one destination server is attacked, traffic can be redirected to other servers.



