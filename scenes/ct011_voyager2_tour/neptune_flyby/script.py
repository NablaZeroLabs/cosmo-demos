# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Cosmographia script for Voyager 2 Neptune Flyby scene.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2020 Nabla Zero Labs

import cosmoscripting

cosmo  = cosmoscripting.Cosmo()
bodies = [ 'Sun', 'Earth', 'Mars', 'Jupiter', 'Saturn' 'Uranus' ]
moons  = [ 'Triton', 'Proteus' ]

########################################
# Initial setup

cosmo.showFullScreen()
cosmo.setTime( '1989-08-22 12:00 UTC' )
cosmo.pause()
cosmo.hideAllObjects()
cosmo.hideToolBar()
cosmo.hideSpiceMessages()
cosmo.hideEcliptic()
cosmo.hideCenterIndicator()
cosmo.hideLabels()
cosmo.hidePlanetOrbits()
cosmo.hideStatusMessages()
cosmo.setCentralObject( 'Neptune' )
cosmo.setCameraToInertialFrame()
cosmo.setCameraPosition( [ -665400.002393, 3312603.335019, 2619109.791719 ] )
cosmo.setCameraOrientation( [ 0.005701, 0.083927, -0.432006, -0.897939 ] )

for body in bodies:
	cosmo.showObject( body )
	cosmo.showTrajectory( body )

for body in moons:
	cosmo.showObject( body )
	cosmo.showTrajectory( body )

cosmo.showObject( 'Neptune' )
cosmo.showObject( 'Voyager 2' )
cosmo.showTrajectory( 'Voyager 2' )
cosmo.showLabels()

########################################
# Begin scene

cosmo.fadeIn( 6 )
cosmo.rollLeft( 5, 1 )
cosmo.selectObject( 'Neptune' )
cosmo.setTimeRate( 20000 )
cosmo.wait( 2 )
cosmo.unpause()
cosmo.wait( 2 )
cosmo.dollyForward( 3800000, 12 )
cosmo.circleCenterRight( 180, 8 )
cosmo.circleCenterUp( 140, 4 )
cosmo.wait( 0.5 )
cosmo.showStarNames()
cosmo.showConstellationNames()
cosmo.showConstellationFigures()
cosmo.hideObject( 'Triton' )
cosmo.hideObject( 'Proteus' )
cosmo.hideTrajectory( 'Triton' )
cosmo.hideTrajectory( 'Proteus' )
cosmo.selectObject( 'Voyager 2' )
cosmo.setTimeRate( 1000000 )
cosmo.wait( 6 )
cosmo.pause()
