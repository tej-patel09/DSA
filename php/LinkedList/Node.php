<?php

namespace Node;

class Node
{
  public $value;
  public $next;

  function __construct($value)
  {
    $this->value = $value;
    $this->next = NULL;
  }
}
