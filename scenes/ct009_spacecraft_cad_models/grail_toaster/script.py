# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Cosmographia script for GRAIL Toasters scene.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2021 Nabla Zero Labs

import cosmoscripting

cosmo  = cosmoscripting.Cosmo()
bodies = [ 'Sun', 'Earth', 'Moon', 'GRAIL-A', 'GRAIL-B' ]

########################################
# Initial setup

cosmo.showFullScreen()
cosmo.pause()
cosmo.setTime( '2012-10-28 00:10:00 UTC' )
cosmo.hideAllObjects()
cosmo.hideToolBar()
cosmo.hideSpiceMessages()
cosmo.hideEcliptic()
cosmo.hideCenterIndicator()
cosmo.hideLabels()
cosmo.hidePlanetOrbits()

for body in bodies:
	cosmo.showObject( body )
cosmo.showTrajectory( 'GRAIL-B' )

cosmo.setCentralObject( 'GRAIL-A' )
cosmo.selectObject( 'GRAIL-B' )
cosmo.setCameraToInertialFrame()
cosmo.setCameraPosition( [ -0.04133, 0.046232, -0.001186 ] )
cosmo.setCameraOrientation( [ -0.367265, 0.684175, -0.203634, -0.596284 ] )

cosmo.trackObject( 'Moon' )
cosmo.showBodyFixedFrame( 'GRAIL-A' )
cosmo.showDirectionVector( 'GRAIL-A', 'GRAIL-B' )
cosmo.selectObject( 'GRAIL-B' )

cosmo.showLabels()

########################################
# Begin scene

cosmo.fadeIn( 1 )
cosmo.wait( 6 )
cosmo.setTimeRate( 100 )
cosmo.unpause()
cosmo.wait( 15 )

cosmo.pause()
