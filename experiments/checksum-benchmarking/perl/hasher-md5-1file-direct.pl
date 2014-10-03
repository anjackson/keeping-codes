#!/usr/bin/perl

use File::Slurp;
use Digest::MD5 qw(md5_hex);

open( my $FILE, $ARGV[0] );
binmode($FILE);
$md5_hex = Digest::MD5->new->addfile($FILE)->hexdigest;
close($FILE);

print "" . $md5_hex . " " . $ARGV[0] ."\n";
