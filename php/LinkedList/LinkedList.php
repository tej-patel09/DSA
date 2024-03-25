<?php

namespace LinkedList;

require_once("./Node.php");

use Node\Node as n;

class linked_list
{
  protected $head;
  protected $tail;
  protected $length = 0;

  function __construct($value)
  {
    $new_node = new n($value);
    $this->head = $new_node;
    $this->tail = $new_node;
    $this->length = 1;
  }

  function print_list(): void
  {
    $temp = $this->head;
    print("\n");
    while ($temp != NULL) {
      print($temp->value . " ");
      $temp = $temp->next;
    }
  }

  function append($value): bool
  {
    $new_node = new n($value);
    if ($this->length == 0) {
      $this->head = $new_node;
      $this->tail = $new_node;
    } else {
      $this->tail->next = $new_node;
      $this->tail = $new_node;
    }
    $this->length += 1;
    return True;
  }

  function pop(): n|NULL
  {
    if ($this->length == 0) {
      return NULL;
    }
    $temp = $this->head;
    $pre = $this->head;
    while ($temp->next) {
      $pre = $temp;
      $temp = $temp->next;
    }
    $this->tail = $pre;
    $this->tail->next = NULL;
    $this->length -= 1;
    if ($this->length == 0) {
      $this->head = NULL;
      $this->tail = NULL;
    }
    return $temp;
  }

  function get($index): n|NULL
  {
    if ($index < 0 || $index >= $this->length) {
      return NULL;
    }
    $temp = $this->head;
    for ($i = 0; $i < $index; $i++) {
      $temp = $temp->next;
    }
    return $temp;
  }

  function reverse(): bool
  {
    $temp = $this->head;
    $this->head = $this->tail;
    $this->tail = $temp;
    $after = $temp->next;
    $before = null;
    while ($after) {
      // for ($i = 0; $i < $this->length; $i++) {
      $after = $temp->next;
      $temp->next = $before;
      $before = $temp;
      $temp = $after;
    }
    return True;
  }
}
