<?php
import os
 
function func_print_test_env($event, $context)
{

echo 'The test env's value is: ' .$_ENV["TEST_ENV"] . '!';

}
