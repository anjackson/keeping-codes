#!/usr/bin/perl

use File::Slurp;
use Digest::SHA qw(sha256_hex);

$sha256_hex = sha256_hex(read_file($ARGV[0]));

print "" . $sha256_hex . " " . $ARGV[0] ."\n";
