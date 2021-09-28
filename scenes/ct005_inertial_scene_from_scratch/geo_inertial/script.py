# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Cosmographia script for Geostationary Orbit scene.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2021 Nabla Zero Labs

import cosmoscripting

cosmo  = cosmoscripting.Cosmo()
bodies = [ 'Sun', 'Earth', 'Moon', 'GEO Spacecraft' ]

########################################
# Initial setup

cosmo.showFullScreen()
cosmo.pause()
cosmo.setTime( '2021-08-06 00:10:00 UTC' )
cosmo.hideAllObjects()
cosmo.hideToolBar()
cosmo.hideSpiceMessages()
cosmo.hideEcliptic()
cosmo.hideCenterIndicator()
cosmo.hideLabels()
cosmo.hidePlanetOrbits()

for body in bodies:
	cosmo.showObject( body )
cosmo.showTrajectory( 'GEO Spacecraft' )
cosmo.showTrajectory( 'Moon' )

cosmo.setCentralObject( 'Earth' )
cosmo.selectObject( 'Earth' )
cosmo.setCameraToInertialFrame()
cosmo.setCameraPosition( [ -20588.815307, 128356.247694, 27401.753157 ] )
cosmo.setCameraOrientation( [ -0.076761, -0.043044, 0.607017, 0.789801 ] )
cosmo.showLabels()

########################################
# Begin scene

cosmo.fadeIn( 1 )
cosmo.wait( 2 )
cosmo.showDirectionVector( 'Earth', 'GEO Spacecraft' )
cosmo.wait( 1 )
cosmo.setTimeRate( 6000 )
cosmo.unpause()
cosmo.wait( 5 )
cosmo.circleCenterUp( 75, 5 )
cosmo.wait( 5 )

cosmo.pause()
