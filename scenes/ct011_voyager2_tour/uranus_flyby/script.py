# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Cosmographia script for Voyager 2 Uranus Flyby scene.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2020 Nabla Zero Labs

import cosmoscripting

cosmo  = cosmoscripting.Cosmo()
bodies = [ 'Sun', 'Earth', 'Mars', 'Jupiter', 'Saturn' 'Neptune' ]
moons  = [ 'Miranda', 'Ariel', 'Umbriel', 'Titania', 'Oberon' ]

########################################
# Initial setup

cosmo.showFullScreen()
cosmo.setTime( '1986-01-22 12:00 UTC' )
cosmo.pause()
cosmo.hideAllObjects()
cosmo.hideToolBar()
cosmo.hideSpiceMessages()
cosmo.hideEcliptic()
cosmo.hideCenterIndicator()
cosmo.hideLabels()
cosmo.hidePlanetOrbits()
cosmo.hideStatusMessages()
cosmo.setCentralObject( 'Voyager 2' )
cosmo.setCameraToInertialFrame()
cosmo.setCameraPosition( [ -0.002334, 0.028823, 0.018592 ] )
cosmo.setCameraOrientation( [ -0.055984, -0.017112, 0.489184, 0.870214 ] )

for body in bodies:
	cosmo.showObject( body )
	cosmo.showTrajectory( body )

for body in moons:
	cosmo.showObject( body )
	cosmo.showTrajectory( body )

cosmo.showObject( 'Uranus' )
cosmo.showObject( 'Voyager 2' )
cosmo.showLabels()

########################################
# Begin scene

cosmo.fadeIn( 1 )
cosmo.selectObject( 'Saturn' )
cosmo.wait( 6 )
cosmo.setTimeRate( 30000 )
cosmo.trackObject( 'Uranus' )
cosmo.unpause()
cosmo.wait( 3 )
cosmo.showVelocityVector( 'Voyager 2' )
cosmo.showDirectionVector( 'Voyager 2', 'Earth' )
cosmo.wait( 2 )
cosmo.setTimeRate( 7000 )
cosmo.showDirectionVector( 'Voyager 2', 'Neptune' )
cosmo.wait( 11 )
cosmo.selectObject( 'Neptune' )
cosmo.setTimeRate( 50000 )
cosmo.wait( 5 )
cosmo.pause()
