# simple perl code to demonstrate dynamic scoping 
# based on https://www.geeksforgeeks.org/static-and-dynamic-scoping/

$b = 5;
sub foo
{
  $a = $b + 5;
  return $a;
}

sub bar
{
  # this creates a new variable, but uses dynamic scoping
  local $b = 2;

  # this edits the global variable
  #$b = 2;

  # to force static scoping
  #my $b = 2;
  
  return foo();
}

sub main
{
  print foo()."\n";
  print bar()."\n";
}

main();

