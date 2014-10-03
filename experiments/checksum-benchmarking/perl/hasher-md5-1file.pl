#!/usr/bin/perl

use File::Slurp;
use Digest::MD5 qw(md5_hex);

$md5_hex = md5_hex(read_file($ARGV[0]));

print "" . $md5_hex . " " . $ARGV[0] ."\n";
