# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Cosmographia script for Voyager 2 Saturn Flyby scene.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2020 Nabla Zero Labs

import cosmoscripting

cosmo       = cosmoscripting.Cosmo()
bodies      = [ 'Sun', 'Earth', 'Mars', 'Jupiter', 'Uranus', 'Neptune' ]
saturnians  = [ 'Mimas', 'Enceladus', 'Tethys', 'Dione', 'Rhea', 'Titan' ]
saturnians += [ 'Hyperion', 'Iapetus' ]

########################################
# Initial setup

cosmo.showFullScreen()
cosmo.setTime( '1981-08-22 12:00 UTC' )
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
cosmo.setCameraPosition( [ 0.030303, 0.013919, 0.015341 ] )
cosmo.setCameraOrientation( [ -0.297485, -0.382978, -0.396137, -0.779683 ] )

for body in bodies:
	cosmo.showObject( body )
	cosmo.showTrajectory( body )

for body in saturnians:
	cosmo.showObject( body )
	cosmo.showTrajectory( body )

cosmo.showObject( 'Saturn' )
cosmo.showObject( 'Saturn Rings' )
cosmo.showObject( 'Voyager 2' )
cosmo.showLabels()

########################################
# Begin scene

cosmo.fadeIn( 1 )
cosmo.selectObject( 'Saturn' )
cosmo.wait( 6 )
cosmo.setTimeRate( 30000 )
cosmo.trackObject( 'Saturn' )
cosmo.unpause()
cosmo.wait( 3 )
cosmo.showVelocityVector( 'Voyager 2' )
cosmo.showDirectionVector( 'Voyager 2', 'Earth' )
cosmo.wait( 6 )
cosmo.showDirectionVector( 'Voyager 2', 'Uranus' )
cosmo.setTimeRate( 10000 )
cosmo.wait( 8 )
cosmo.setCameraToInertialFrame()
cosmo.setTimeRate( 30000 )
cosmo.selectObject( 'Uranus' )
cosmo.circleCenterRight( 160, 8 )
cosmo.pause()
