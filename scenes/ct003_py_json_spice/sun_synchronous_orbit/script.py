# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Cosmographia script for Sun Synchronous Orbit scene.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2021 Nabla Zero Labs

import cosmoscripting

cosmo  = cosmoscripting.Cosmo()
bodies = [ 'Sun', 'Earth', 'Moon', 'SSO Spacecraft' ]

########################################
# Initial setup

cosmo.showFullScreen()
cosmo.pause()
cosmo.setTime( '2021-09-17 00:10:00 UTC' )
cosmo.hideAllObjects()
cosmo.hideToolBar()
cosmo.hideSpiceMessages()
cosmo.hideEcliptic()
cosmo.hideCenterIndicator()
cosmo.hideLabels()
cosmo.hidePlanetOrbits()

for body in bodies:
	cosmo.showObject( body )
cosmo.showTrajectory( 'SSO Spacecraft' )
cosmo.showTrajectory( 'Moon' )

cosmo.setCentralObject( 'Earth' )
cosmo.selectObject( 'Earth' )
cosmo.setCameraToInertialFrame()
cosmo.setCameraPosition( [ -18763.520461, -3770.166644, 8500.870754 ] )
cosmo.setCameraOrientation( [ 0.692937, 0.376302, -0.383892, -0.480481 ] )
cosmo.showLabels()

########################################
# Begin scene

cosmo.fadeIn( 1 )
cosmo.wait( 2 )
cosmo.showDirectionVector( 'Earth', 'Sun' )
cosmo.wait( 1 )
cosmo.setTimeRate( 1000 )
cosmo.unpause()
cosmo.wait( 5 )
cosmo.setTimeRate( 5000 )
cosmo.wait( 5 )
cosmo.setTimeRate( 50000 )
cosmo.wait( 5 )
cosmo.pause()
