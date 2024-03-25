<?php
/* 
cd .\php\LinkedList & php .\main.php 
*/
require_once("./LinkedList.php");

use LinkedList\linked_list as ll;

$my_list = new ll(4);
$my_list->append(10);
$my_list->append(11);
$my_list->append(12);
$my_list->append(13);
// $x = $my_list->pop();
// print_r($x);
$my_list->print_list();
$my_list->reverse();
$my_list->print_list();
