#!/usr/bin/perl

use File::Find;
use File::Slurp;
use Digest::MD5 qw(md5_hex);

for($i = 2; $i < 5; $i++)
{
	find(\&printer, "/Volumes/checksum_study/" . $i . "/");	
}

sub printer
{
	$path = $File::Find::name;
	if(-f $path)
	{
		md5_hex(read_file($path));
	}
}
