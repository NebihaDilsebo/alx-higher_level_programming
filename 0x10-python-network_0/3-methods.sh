#!/bin/bash
# Display all HTTP method the server will accept
curl -Is "$1" | grep Allow | cut -c 8-
