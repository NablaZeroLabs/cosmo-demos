# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Cosmographia script for SSO Spacecraft Sun scene.
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
cosmo.showTrajectory( 'Moon' )

cosmo.setCentralObject( 'SSO Spacecraft' )
cosmo.selectObject( 'Earth' )
cosmo.setCameraToInertialFrame()
cosmo.setCameraPosition( [ 0.023973, -0.015095, 0.004675 ] )
cosmo.setCameraOrientation( [ 0.720473, 0.492792, 0.46207, 0.156734 ] )
cosmo.showLabels()

cosmo.trackObject( 'Earth' )
cosmo.showBodyFixedFrame( 'SSO Spacecraft' )
cosmo.showDirectionVector( 'SSO Spacecraft', 'Earth' )
cosmo.showDirectionVector( 'SSO Spacecraft', 'Sun' )
cosmo.showVelocityVector( 'SSO Spacecraft' )

########################################
# Begin scene

cosmo.fadeIn( 1 )
cosmo.wait( 6 )
cosmo.setTimeRate( 200 )
cosmo.unpause()
cosmo.wait( 15 )

cosmo.pause()
