# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Cosmographia script for SSO Attitude scene.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2021 Nabla Zero Labs

import cosmoscripting

cosmo  = cosmoscripting.Cosmo()
bodies = [ 'SC', 'Sun', 'Earth', 'Moon' ]

########################################
# Initial setup

cosmo.showFullScreen()
cosmo.setTime( '2021-08-05 01:45:00 UTC' )
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
cosmo.setCameraToInertialFrame()
cosmo.setCameraPosition( [ -0.010706, 0.005886, 0.032213 ] )
cosmo.setCameraOrientation( [ 0.780647, -0.025485, -0.136225, -0.609413 ] )
cosmo.setCameraToSynodicFrame()

for body in bodies:
	cosmo.showObject( body )
cosmo.showLabels()

########################################
# Begin scene
cosmo.fadeIn( 1 )
cosmo.wait( 9 )
cosmo.unpause()
cosmo.showBodyFixedFrame( 'SC' )
cosmo.showDirectionVector( 'SC', 'Sun' )
cosmo.showDirectionVector( 'SC', 'Earth' )
cosmo.setTimeRate( 100 )
cosmo.wait( 23 )

cosmo.pause()
