#!/usr/bin/perl

use Digest::SHA qw(sha256_hex);

open( my $FILE, $ARGV[0] );
binmode($FILE);
$sha256_hex = Digest::SHA->new(256)->addfile($FILE)->hexdigest;
close($FILE);

print "" . $sha256_hex . " " . $ARGV[0] ."\n";
