#!/bin/bash
for i in {1..3}
do
    python client_multithreaded.py $i &
done
wait
