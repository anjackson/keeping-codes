#!/usr/bin/perl

use File::Find;
use File::Slurp;
use Digest::SHA qw(sha256_hex);

for($i = 2; $i < 5; $i++)
{
	find(\&printer, "/Volumes/checksum_study/" . $i . "/");	
}

sub printer
{
	$path = $File::Find::name;
	if(-f $path)
	{
		sha256_hex(read_file($path));
	}
}
