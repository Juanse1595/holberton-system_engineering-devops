# 0x05-processes_and_signals

This directory contains programs with examples on how processes and signals works on Unix like systems

## 0-what-is-my-pid

Write a Bash script that displays its own PID.

## 1-list_your_processes

Write a Bash script that displays a list of currently running processes.

## 2-show_your_bash_pid

Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

## 3-show_your_bash_pid_made_easy

Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

## 4-to_infinity_and_beyond

Write a Bash script that displays To infinity and beyond indefinitely.

## 5-dont_stop_me_now

We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that stops 4-to_infinity_and_beyond process.

## 6-stop_me_if_you_can

Write a Bash script that stops 4-to_infinity_and_beyond process.

## 7-highlander

Write a Bash script that displays:

To infinity and beyond indefinitely
With a sleep 2 in between each iteration
I am invincible!!! when receiving a SIGTERM signal

## 8-beheaded_process

Write a Bash script that kills the process 7-highlander.