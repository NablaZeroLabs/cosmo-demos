# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Cosmographia script for Orion NRHO scene.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2021 Nabla Zero Labs

import cosmoscripting

cosmo  = cosmoscripting.Cosmo()
bodies = [ 'Sun', 'Earth', 'Moon', 'Orion' ]

########################################
# Initial setup

cosmo.showFullScreen()
cosmo.pause()
cosmo.setTime( '2024-06-06 00:00:00 UTC' )
cosmo.hideAllObjects()
cosmo.hideToolBar()
cosmo.hideSpiceMessages()
cosmo.hideEcliptic()
cosmo.hideCenterIndicator()
cosmo.hideLabels()
cosmo.hidePlanetOrbits()
cosmo.showInfoText()

for body in bodies:
	cosmo.showObject( body )
cosmo.showTrajectory( 'Orion' )
cosmo.showTrajectory( 'Moon' )

cosmo.setCentralObject( 'Moon' )
cosmo.selectObject( 'Moon' )
cosmo.setCameraToSynodicFrame()
cosmo.setCameraPosition( [ 112449.65962, 556.817102, 8623.26994 ] )
cosmo.setCameraOrientation( [ 0.572582, 0.398892, 0.40343, 0.591844 ] )
cosmo.showLabels()

########################################
# Begin scene

cosmo.fadeIn( 1 )
cosmo.wait( 6 )
cosmo.setTimeRate( 100000 )
cosmo.unpause()
cosmo.wait( 5 )
cosmo.circleCenterRight( 100, 12 )
cosmo.wait( 3 )
cosmo.pause()
