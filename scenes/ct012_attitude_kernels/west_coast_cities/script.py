# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Cosmographia script for Earth observation.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2021 Nabla Zero Labs

import cosmoscripting

cosmo   = cosmoscripting.Cosmo()
bodies  = [ 'SC', 'Sun', 'Earth', 'Moon', 'Los Angeles' ]
bodies += [ 'San Francisco', 'Seattle' ]

########################################
# Initial setup

cosmo.showFullScreen()
cosmo.setTime( '2021-10-11 00:04:11 UTC' )
cosmo.pause()
cosmo.hideAllObjects()
cosmo.hideToolBar()
cosmo.hideSpiceMessages()
cosmo.hideEcliptic()
cosmo.hideCenterIndicator()
cosmo.hideLabels()
cosmo.hidePlanetOrbits()
cosmo.hideStatusMessages()

cosmo.selectObject( 'Earth' )
cosmo.setCentralObject( 'SC' )
cosmo.setCameraToSynodicFrame()
cosmo.setCameraPosition( [ 0.042362, -0.032439, -0.008405 ] )
cosmo.setCameraOrientation( [ 0.653753, 0.285397, 0.681349, -0.164072 ] )

for body in bodies:
	cosmo.showObject( body )
cosmo.showTrajectory( 'Moon' )
cosmo.showLabels()

########################################
# Begin scene
cosmo.fadeIn( 1 )
cosmo.showBodyFixedFrame( 'SC' )
cosmo.showDirectionVector( 'SC', 'Earth' )
cosmo.showDirectionVector( 'SC', 'Los Angeles' )
cosmo.wait( 12 )
cosmo.setTimeRate( 25 )
cosmo.unpause()
cosmo.wait( 10 )
cosmo.showDirectionVector( 'SC', 'San Francisco' )
cosmo.wait( 10 )
cosmo.hideDirectionVector( 'SC', 'Los Angeles' )
cosmo.showDirectionVector( 'SC', 'Seattle' )
cosmo.wait( 5 )
cosmo.showDirectionVector( 'SC', 'Sun' )
cosmo.wait( 1 )
cosmo.hideDirectionVector( 'SC', 'San Francisco' )
cosmo.wait( 7 )


cosmo.pause()


