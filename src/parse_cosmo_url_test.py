# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      parse_cosmo_url_test.py
## @brief     Cosmograhia URL parser unit tests.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2021 Nabla Zero Labs

import pytest
from parse_cosmo_url import parse_url

def test_no_arguments_passed_in_expect_throw():
	with pytest.raises( RuntimeError ):
		parse_url( [ 'parse_cosmo_url.py' ] )

def test_empty_first_argument_expect_throw():
	with pytest.raises( RuntimeError ):
		parse_url( [ 'parse_cosmo_url.py', '' ] )

def test_too_many_variables_in_url_expect_throw():
	url = ( 'cosmo:Sun?select=Sun&frame=icrf&jd=2459479.166353'
		    '&x=621948642.994960&y=-1345464080.888191&z=234503252.731015'
		    '&qw=0.723297&qx=0.644880&qy=0.077452&qz=0.234462&ts=1&fov=50'
		    '&test'
	)
	with pytest.raises( RuntimeError ):
		parse_url( [ 'parse_cosmo_url.py', url ] )

def test_too_few_variables_in_url_expect_throw():
	url = ( 'frame=icrf&jd=2459479.166353'
		    '&x=621948642.994960&y=-1345464080.888191&z=234503252.731015'
		    '&qw=0.723297&qx=0.644880&qy=0.077452&qz=0.234462&ts=1'
	)
	with pytest.raises( RuntimeError ):
		parse_url( [ 'parse_cosmo_url.py', url ] )

def test_basic_usage_11_vars():
	url = ( 'frame=icrf&jd=2459479.166353'
		    '&x=621948642.994960&y=-1345464080.888191&z=234503252.731015'
		    '&qw=0.723297&qx=0.644880&qy=0.077452&qz=0.234462&ts=1&fov=50'
	)
	parse_url( [ 'parse_cosmo_url.py', url ] )	

def test_basic_usage_12_vars():
	url = ( 'cosmo:Sun?select=Sun&frame=icrf&jd=2459479.166353'
		    '&x=621948642.994960&y=-1345464080.888191&z=234503252.731015'
		    '&qw=0.723297&qx=0.644880&qy=0.077452&qz=0.234462&ts=1&fov=50'
	)
	parse_url( [ 'parse_cosmo_url.py', url ] )	
