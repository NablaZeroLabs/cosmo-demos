# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Parse Cosmograhia URL to Python commands.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2021 Nabla Zero Labs

from sys import argv

def parse_url( args ):
	nargs = len( args )

	if nargs != 2 or not args[ 1 ]:
		raise RuntimeError(
			f'Expected 1 commmand line argument, got {nargs}.' )

	s     = args[ 1 ].split( '&' )
	nvars = len( s )

	if nvars == 11:
		x  = s[ 2 ].replace( 'x=',  '' )
		y  = s[ 3 ].replace( 'y=',  '' )
		z  = s[ 4 ].replace( 'z=',  '' )
		qw = s[ 5 ].replace( 'qw=', '' )
		qx = s[ 6 ].replace( 'qx=', '' )
		qy = s[ 7 ].replace( 'qy=', '' )
		qz = s[ 8 ].replace( 'qz=', '' )
	elif nvars == 12:
		x  = s[ 3 ].replace( 'x=',  '' )
		y  = s[ 4 ].replace( 'y=',  '' )
		z  = s[ 5 ].replace( 'z=',  '' )
		qw = s[ 6 ].replace( 'qw=', '' )
		qx = s[ 7 ].replace( 'qx=', '' )
		qy = s[ 8 ].replace( 'qy=', '' )
		qz = s[ 9 ].replace( 'qz=', '' )
	else:
		raise RuntimeError(
			f'Expected 11 or 12 variables in URL, got {nvars}.' )

	line0 = f'cosmo.setCameraPosition( [ {x}, {y}, {z} ] )'
	line1 = f'cosmo.setCameraOrientation( [ {qw}, {qx}, {qy}, {qz} ] )'

	print( s )
	print( nvars )
	print()
	print( line0 )
	print( line1 )
	print()

if __name__ == '__main__':
	parse_url( argv )
