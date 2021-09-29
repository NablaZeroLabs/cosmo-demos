# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Cosmographia Python script for Voyagers Interplanetary scene.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2020 Nabla Zero Labs

import cosmoscripting

cosmo  = cosmoscripting.Cosmo()

bodies  = [ 'Sun', 'Earth', 'Mars', 'Jupiter', 'Saturn' ]
bodies += [ 'Uranus', 'Neptune', 'Voyager 1', 'Voyager 2' ]

########################################
# Initial setup

cosmo.showFullScreen()
cosmo.setTime( '1977-09-08 UTC' )
cosmo.pause()
cosmo.hideAllObjects()
cosmo.hideToolBar()
cosmo.hideSpiceMessages()
cosmo.hideEcliptic()
cosmo.hideCenterIndicator()
cosmo.hideLabels()
cosmo.hidePlanetOrbits()
cosmo.hideInfoText()
cosmo.hideStatusMessages()
cosmo.setCentralObject( 'Sun' )
cosmo.setCameraToInertialFrame()
cosmo.setCameraPosition( [ -31705163.474087, -903627409.677422, 1572715235.560303 ] )
cosmo.setCameraOrientation( [ 0.203285, 0.043537, -0.247462, 0.946331 ] )

for body in bodies:
	cosmo.showObject( body )
	cosmo.showTrajectory( body )
	cosmo.trajectoryWidth( body, 3 )
cosmo.showLabels()

########################################
# Begin scene

cosmo.fadeIn( 1 )
cosmo.wait( 5 )
cosmo.setTimeRate( 10000000 )
cosmo.unpause()
cosmo.wait( 5 )
cosmo.dollyBackward( 1572715235, 5 )
cosmo.dollyBackward( 4572715235, 5 )
cosmo.setTimeRate( 30000000 )
cosmo.circleCenterDown( 90, 3 )
cosmo.setTimeRate( 50000000 )
cosmo.wait( 15 )

cosmo.pause()
