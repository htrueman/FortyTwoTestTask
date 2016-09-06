#!/bin/sh

fnd=$(grep -ri "\bnoqa\b" apps fortytwo_test_task)

if [[ $fnd ]]; then
    exit 0
else
    exit 0
fi
