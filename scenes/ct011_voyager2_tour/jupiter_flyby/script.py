# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Cosmographia script for Voyager 2 Jupiter Flyby scene.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2020 Nabla Zero Labs

import cosmoscripting

cosmo   = cosmoscripting.Cosmo()
bodies  = [ 'Sun', 'Earth', 'Mars', 'Saturn', 'Uranus', 'Neptune' ]
jovians = [ 'Io', 'Europa', 'Ganymede', 'Callisto' ]

########################################
# Initial setup

cosmo.showFullScreen()
cosmo.setTime( '1979-07-07 12:00 UTC' )
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
cosmo.setCameraPosition( [ 0.025367, -0.025133, -0.00159 ] )
cosmo.setCameraOrientation( [ 0.566735, 0.714912, 0.144169, 0.383312 ] )

for body in bodies[ :-2 ]:
	cosmo.showObject( body )
	cosmo.showTrajectory( body )

for body in jovians:
	cosmo.showObject( body )
	cosmo.showTrajectory( body )

cosmo.showObject( 'Jupiter' )
cosmo.showObject( 'Voyager 2' )
cosmo.showLabels()

########################################
# Begin scene

cosmo.fadeIn( 1 )

cosmo.wait( 6 )
cosmo.setTimeRate( 10000 )
cosmo.selectObject( 'Jupiter' )
cosmo.unpause()
cosmo.showVelocityVector( 'Voyager 2' )
cosmo.showDirectionVector( 'Voyager 2', 'Earth' )
cosmo.showDirectionVector( 'Voyager 2', 'Callisto' )
cosmo.circleCenterLeft( 10, 7 )
cosmo.hideDirectionVector( 'Voyager 2', 'Callisto' )
cosmo.showDirectionVector( 'Voyager 2', 'Ganymede' )
cosmo.setCameraToInertialFrame()
cosmo.circleCenterRight( 50, 5 )
cosmo.wait( 2 )
cosmo.showDirectionVector( 'Voyager 2', 'Europa' )
cosmo.wait( 2 )
cosmo.hideDirectionVector( 'Voyager 2', 'Ganymede' )
cosmo.circleCenterRight( 50, 7 )
cosmo.hideDirectionVector( 'Voyager 2', 'Europa' )
cosmo.wait( 1 )
cosmo.showDirectionVector( 'Voyager 2', 'Saturn' )
cosmo.circleCenterLeft( 30, 3 )
cosmo.setTimeRate( 50000 )
cosmo.wait( 5 )

cosmo.pause()
