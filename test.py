# trace generated using paraview version 5.10.1
# import paraview
# paraview.compatibility.major = 5
# paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *

xVel = []
yVel = []
xPos = []
yPos = []
timeValues = []
timeStep = []
numSteps = 355


def runProcessing():
    generateData(100, 0.013)

    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # create a new 'Restart timeline'
    flsgrf6pmelt400p1000130um = Restarttimeline(
        registrationName="flsgrf.6-p-melt-400p-1000-130um",
        FileName="C:\\Users\\Aashman Sharma\\Documents\\Paraview\\Example_Simulations\\6-p-melt-400p-1000-130um\\flsgrf.6-p-melt-400p-1000-130um",
    )
    flsgrf6pmelt400p1000130um.CellArrays = [
        "Static Contact Angle",
        "Normalized Drag Coefficient",
        "Solid Fraction",
        "Dynamic Viscosity",
        "Diagnostics: Nf Values",
        "Liquid Region Label",
        "Pressure",
        "Phase Change Mass Flux",
        "Diagnostics: Pressure Iteration Residual",
        "Surface Tension Pressure",
        "Mass Source Rate Per Unit Open Volume",
        "Volume Source Rate Per Unit Open Volume",
        "Macroscopic Density",
        "Macroscopic Energy Of Fluid #1",
        "Cooling Rate R",
        "Evaporation Pressure",
        "Melt Region",
        "Temperature Gradient G",
        "Temperature Gradient DT/dx",
        "Temperature Gradient DT/dy",
        "Temperature Gradient DT/dz",
        "Temperature",
        "X-velocity",
        "Y-velocity",
        "Diagnostics: Cumulative Fluid Fraction Error",
        "Z-velocity",
    ]
    flsgrf6pmelt400p1000130um.HistoryData = [
        "Diagnostics: Time-step Size",
        "Diagnostics: Elapsed Clock Time",
        "Diagnostics: Elapsed Clock Time Per Time Step",
        "Diagnostics: % Parallel Efficiency",
        "Fill Fraction",
        "Solidified Volume Fraction",
        "Diagnostics: Time-step Stability Limit",
        "Diagnostics: X-direction Convective Time-step Limit",
        "Diagnostics: Y-direction Convective Time-step Limit",
        "Diagnostics: Z-direction Convective Time-step Limit",
        "Diagnostics: Viscous Time-step Limit",
        "Diagnostics: Free Surface Time-step Limit",
        "Diagnostics: Surface Tension Time-step Limit",
        "Diagnostics: Thermal Conduction Time-step Limit",
        "Diagnostics: Pressure Convergence Criterion",
        "Diagnostics: Pressure Relaxation Factor",
        "Diagnostics: Maximum Pressure Residual",
        "Diagnostics: Pressure Iteration Count",
        "Diagnostics: Thermal Convergence Criterion",
        "Diagnostics: Thermal Relaxation Factor",
        "Diagnostics: Maximum Normalized Thermal Residual",
        "Diagnostics: Maximum Thermal Residual In Degrees",
        "Diagnostics: Thermal Iteration Count",
        "Average Vorticity",
        "Diagnostics: Convective Volume Error",
        "Diagnostics: Convective Volume Error; % Lost",
        "Diagnostics: Interblock Boundary Volume Error",
        "Diagnostics: Interblock Boundary Volume Error; % Lost",
        "Volume Of Fluid #1",
        "Fluid Surface Area",
        "Solidified Volume Of Fluid 1",
        "Cumulative Evaporated Mass",
        "Fluid Center Of Mass X-coordinate",
        "Fluid Center Of Mass Y-coordinate",
        "Fluid Center Of Mass Z-coordinate",
        "Diagnostics: Fluid 1 Volume Net Influx",
        "Mass-averaged Fluid Mean Kinetic Energy",
        "Total Fluid Mass",
        "Diagnostics: Accumulated Fluid Mass Source",
        "Total Fluid #1 Thermal Energy",
        "Minimum Fluid #1 Temperature",
        "Maximum Fluid #1 Temperature",
        "Average Fluid #1 Temperature",
        "Cooling Rate R Mass",
        "Evaporation Pressure Mass",
        "Melt Region Mass",
        "Temperature Gradient G Mass",
        "Temperature Gradient DT/dx Mass",
        "Temperature Gradient DT/dy Mass",
        "Temperature Gradient DT/dz Mass",
        "Total Number Of Particles",
        "Hot Spots",
        "Laser #  1 : X-coordinate",
        "Laser #  1 : Y-coordinate",
        "Laser #  1 : Z-coordinate",
        "Mesh Block 2: Zmax Fluid #1 Volume Flow Rate",
        "Mesh Block 2: Zmax Specified Pressure",
        "Mesh Block 2: Zmax Specified Fluid Fraction",
        "Mesh Block 2: Zmax Specified X-velocity",
        "Mesh Block 2: Zmax Specified Y-velocity",
        "Mesh Block 2: Zmax Specified Fluid #1 Temperature",
        "Mesh Block 2: Zmax Specified Void Temperature",
        "Mesh Block 2: Zmax Specified Melt Region",
    ]

    # get animation scene
    animationScene1 = GetAnimationScene()

    # update animation scene based on data timesteps
    animationScene1.UpdateAnimationUsingDataTimeSteps()

    # rename source object
    RenameSource("Case 1: flsgrf.6-p-melt-400p-1000-130um", flsgrf6pmelt400p1000130um)

    # get active view
    renderView1 = GetActiveViewOrCreate("RenderView")

    # destroy renderView1
    Delete(renderView1)
    del renderView1

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # Create a new 'Render View'
    renderView1 = CreateView("RenderView")
    renderView1.AxesGrid = "GridAxes3DActor"
    renderView1.StereoType = "Crystal Eyes"
    renderView1.CameraFocalDisk = 1.0
    renderView1.CameraParallelProjection = 1
    renderView1.BackEnd = "OSPRay raycaster"
    renderView1.OSPRayMaterialLibrary = materialLibrary1

    # get layout
    case1flsgrf6pmelt400p1000130um = GetLayoutByName(
        "Case 1: flsgrf.6-p-melt-400p-1000-130um"
    )

    # assign view to a particular cell in the layout
    AssignViewToLayout(view=renderView1, layout=case1flsgrf6pmelt400p1000130um, hint=0)

    # create a new 'Annotate Time'
    time = AnnotateTime(registrationName="Time")
    time.Format = "Time: %0.3f"

    # show data in view
    timeDisplay = Show(time, renderView1, "TextSourceRepresentation")

    # trace defaults for the display properties.
    timeDisplay.WindowLocation = "Any Location"
    timeDisplay.FontSize = 30

    # reset view to fit data
    renderView1.ResetCamera(False)

    # create a new 'Extract Block'
    meshBlock1 = ExtractBlock(
        registrationName="Mesh Block 1", Input=flsgrf6pmelt400p1000130um
    )

    # show data in view
    meshBlock1Display = Show(meshBlock1, renderView1, "StructuredGridRepresentation")

    # trace defaults for the display properties.
    meshBlock1Display.Representation = "Outline"
    meshBlock1Display.ColorArrayName = [None, ""]
    meshBlock1Display.SelectTCoordArray = "None"
    meshBlock1Display.SelectNormalArray = "None"
    meshBlock1Display.SelectTangentArray = "None"
    meshBlock1Display.OSPRayScaleFunction = "PiecewiseFunction"
    meshBlock1Display.SelectOrientationVectors = "Velocity"
    meshBlock1Display.ScaleFactor = 0.014225888310465963
    meshBlock1Display.SelectScaleArray = "None"
    meshBlock1Display.GlyphType = "Arrow"
    meshBlock1Display.GlyphTableIndexArray = "None"
    meshBlock1Display.GaussianRadius = 0.0007112944155232981
    meshBlock1Display.SetScaleArray = [None, ""]
    meshBlock1Display.ScaleTransferFunction = "PiecewiseFunction"
    meshBlock1Display.OpacityArray = [None, ""]
    meshBlock1Display.OpacityTransferFunction = "PiecewiseFunction"
    meshBlock1Display.DataAxesGrid = "GridAxesRepresentation"
    meshBlock1Display.PolarAxes = "PolarAxesRepresentation"
    meshBlock1Display.ScalarOpacityUnitDistance = 0.002457596786255209

    # create a new 'FLSGRF Extract Particles'
    hotspots = FLSGRFExtractParticles(
        registrationName="Hot spots", Input=flsgrf6pmelt400p1000130um
    )
    hotspots.ParticleClass = "Hot spots"

    # show data in view
    hotspotsDisplay = Show(hotspots, renderView1, "UnstructuredGridRepresentation")

    # trace defaults for the display properties.
    hotspotsDisplay.Representation = "Surface"
    hotspotsDisplay.ColorArrayName = [None, ""]
    hotspotsDisplay.SelectTCoordArray = "None"
    hotspotsDisplay.SelectNormalArray = "Normals"
    hotspotsDisplay.SelectTangentArray = "None"
    hotspotsDisplay.OSPRayScaleArray = "Magnitude"
    hotspotsDisplay.OSPRayScaleFunction = "PiecewiseFunction"
    hotspotsDisplay.SelectOrientationVectors = "None"
    hotspotsDisplay.ScaleFactor = 0.11141813099384308
    hotspotsDisplay.SelectScaleArray = "Magnitude"
    hotspotsDisplay.GlyphType = "Arrow"
    hotspotsDisplay.GlyphTableIndexArray = "Magnitude"
    hotspotsDisplay.GaussianRadius = 0.005570906549692154
    hotspotsDisplay.SetScaleArray = ["POINTS", "Magnitude"]
    hotspotsDisplay.ScaleTransferFunction = "PiecewiseFunction"
    hotspotsDisplay.OpacityArray = ["POINTS", "Magnitude"]
    hotspotsDisplay.OpacityTransferFunction = "PiecewiseFunction"
    hotspotsDisplay.DataAxesGrid = "GridAxesRepresentation"
    hotspotsDisplay.PolarAxes = "PolarAxesRepresentation"
    hotspotsDisplay.ScalarOpacityUnitDistance = 0.03343245831802152
    hotspotsDisplay.OpacityArrayName = ["POINTS", "Magnitude"]

    # create a new 'Logo'
    fLOW3DLOGO = Logo(registrationName="FLOW-3D LOGO")

    # a texture
    fLOW3Dpng = CreateTexture("C:\\flow3d\\POST_2023R1\\/f3d/images/FLOW-3D.png")

    # change texture
    fLOW3DLOGO.Texture = fLOW3Dpng

    # show data in view
    fLOW3DLOGODisplay = Show(fLOW3DLOGO, renderView1, "LogoSourceRepresentation")

    # set active source
    SetActiveSource(flsgrf6pmelt400p1000130um)

    # get color transfer function/color map for 'Pressure'
    pressureLUT = GetColorTransferFunction("Pressure")

    # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
    pressureLUT.ApplyPreset("Cool to Warm", True)

    # get color transfer function/color map for 'Temperature'
    temperatureLUT = GetColorTransferFunction("Temperature")

    # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
    temperatureLUT.ApplyPreset("Cool to Warm", True)

    # create a new 'FLSGRF IsoObject'
    fluid = FLSGRFIsoObject(registrationName="Fluid", Input=flsgrf6pmelt400p1000130um)
    fluid.Surface = "Fluid"
    fluid.Box = "Box"
    fluid.Colors = [
        "Cell Type",
        "Cell Volume Fraction",
        "Component Number",
        "Cooling Rate R",
        "Diagnostics: Cumulative Fluid Fraction Error",
        "Diagnostics: Nf Values",
        "Diagnostics: Pressure Iteration Residual",
        "Dynamic Viscosity",
        "Evaporation Pressure",
        "Fraction Of Fluid",
        "Liquid Region Label",
        "Macroscopic Density",
        "Macroscopic Energy Of Fluid #1",
        "Mass Source Rate Per Unit Open Volume",
        "Melt Region",
        "Normalized Drag Coefficient",
        "Phase Change Mass Flux",
        "Pressure",
        "Solid Fraction",
        "Static Contact Angle",
        "Surface Tension Pressure",
        "Temperature",
        "Temperature Gradient DT/dx",
        "Temperature Gradient DT/dy",
        "Temperature Gradient DT/dz",
        "Temperature Gradient G",
        "Velocity",
        "Volume Fraction After AVRCK Adjustment",
        "Volume Source Rate Per Unit Open Volume",
        "X-velocity",
        "Y-velocity",
        "Z-velocity",
        "vtkGhostType",
    ]

    # init the 'Box' selected for 'Box'
    fluid.Box.Position = [
        -0.0010720646241679788,
        -0.0011556369718164206,
        -0.007207692600786686,
    ]
    fluid.Box.Length = [0.14225888310465962, 0.14221314317546785, 0.028215383179485798]

    # show data in view
    fluidDisplay = Show(fluid, renderView1, "UnstructuredGridRepresentation")

    # trace defaults for the display properties.
    fluidDisplay.Representation = "Surface"
    fluidDisplay.ColorArrayName = [None, ""]
    fluidDisplay.SelectTCoordArray = "None"
    fluidDisplay.SelectNormalArray = "Normals"
    fluidDisplay.SelectTangentArray = "None"
    fluidDisplay.OSPRayScaleArray = "Normals"
    fluidDisplay.OSPRayScaleFunction = "PiecewiseFunction"
    fluidDisplay.SelectOrientationVectors = "None"
    fluidDisplay.ScaleFactor = 0.014025523991585943
    fluidDisplay.SelectScaleArray = "None"
    fluidDisplay.GlyphType = "Arrow"
    fluidDisplay.GlyphTableIndexArray = "None"
    fluidDisplay.GaussianRadius = 0.0007012761995792971
    fluidDisplay.SetScaleArray = ["POINTS", "Normals"]
    fluidDisplay.ScaleTransferFunction = "PiecewiseFunction"
    fluidDisplay.OpacityArray = ["POINTS", "Normals"]
    fluidDisplay.OpacityTransferFunction = "PiecewiseFunction"
    fluidDisplay.DataAxesGrid = "GridAxesRepresentation"
    fluidDisplay.PolarAxes = "PolarAxesRepresentation"
    fluidDisplay.ScalarOpacityUnitDistance = 0.00342998138298535
    fluidDisplay.OpacityArrayName = ["POINTS", "Normals"]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    fluidDisplay.ScaleTransferFunction.Points = [
        -1.0,
        0.0,
        0.5,
        0.0,
        1.0,
        1.0,
        0.5,
        0.0,
    ]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    fluidDisplay.OpacityTransferFunction.Points = [
        -1.0,
        0.0,
        0.5,
        0.0,
        1.0,
        1.0,
        0.5,
        0.0,
    ]

    # rescale color and/or opacity maps used to exactly fit the current data range
    fluidDisplay.RescaleTransferFunctionToDataRange(False, True)

    # create a new 'FLSGRF IsoObject'
    openVolume = FLSGRFIsoObject(
        registrationName="Open Volume", Input=flsgrf6pmelt400p1000130um
    )
    openVolume.Surface = "Fluid"
    openVolume.Box = "Box"
    openVolume.Colors = [
        "Cell Type",
        "Cell Volume Fraction",
        "Component Number",
        "Cooling Rate R",
        "Diagnostics: Cumulative Fluid Fraction Error",
        "Diagnostics: Nf Values",
        "Diagnostics: Pressure Iteration Residual",
        "Dynamic Viscosity",
        "Evaporation Pressure",
        "Fraction Of Fluid",
        "Liquid Region Label",
        "Macroscopic Density",
        "Macroscopic Energy Of Fluid #1",
        "Mass Source Rate Per Unit Open Volume",
        "Melt Region",
        "Normalized Drag Coefficient",
        "Phase Change Mass Flux",
        "Pressure",
        "Solid Fraction",
        "Static Contact Angle",
        "Surface Tension Pressure",
        "Temperature",
        "Temperature Gradient DT/dx",
        "Temperature Gradient DT/dy",
        "Temperature Gradient DT/dz",
        "Temperature Gradient G",
        "Velocity",
        "Volume Fraction After AVRCK Adjustment",
        "Volume Source Rate Per Unit Open Volume",
        "X-velocity",
        "Y-velocity",
        "Z-velocity",
        "vtkGhostType",
    ]

    # init the 'Box' selected for 'Box'
    openVolume.Box.Position = [
        -0.0010720646241679788,
        -0.0011556369718164206,
        -0.007207692600786686,
    ]
    openVolume.Box.Length = [
        0.14225888310465962,
        0.14221314317546785,
        0.028215383179485798,
    ]

    # create a new 'FLSGRF IsoObject'
    solid = FLSGRFIsoObject(registrationName="Solid", Input=flsgrf6pmelt400p1000130um)
    solid.Surface = "Fluid"
    solid.Box = "Box"
    solid.Colors = [
        "Cell Type",
        "Cell Volume Fraction",
        "Component Number",
        "Cooling Rate R",
        "Diagnostics: Cumulative Fluid Fraction Error",
        "Diagnostics: Nf Values",
        "Diagnostics: Pressure Iteration Residual",
        "Dynamic Viscosity",
        "Evaporation Pressure",
        "Fraction Of Fluid",
        "Liquid Region Label",
        "Macroscopic Density",
        "Macroscopic Energy Of Fluid #1",
        "Mass Source Rate Per Unit Open Volume",
        "Melt Region",
        "Normalized Drag Coefficient",
        "Phase Change Mass Flux",
        "Pressure",
        "Solid Fraction",
        "Static Contact Angle",
        "Surface Tension Pressure",
        "Temperature",
        "Temperature Gradient DT/dx",
        "Temperature Gradient DT/dy",
        "Temperature Gradient DT/dz",
        "Temperature Gradient G",
        "Velocity",
        "Volume Fraction After AVRCK Adjustment",
        "Volume Source Rate Per Unit Open Volume",
        "X-velocity",
        "Y-velocity",
        "Z-velocity",
        "vtkGhostType",
    ]

    # init the 'Box' selected for 'Box'
    solid.Box.Position = [
        -0.0010720646241679788,
        -0.0011556369718164206,
        -0.007207692600786686,
    ]
    solid.Box.Length = [0.14225888310465962, 0.14221314317546785, 0.028215383179485798]

    # create a new 'FLSGRF IsoObject'
    voidFluid2 = FLSGRFIsoObject(
        registrationName="Void/Fluid 2", Input=flsgrf6pmelt400p1000130um
    )
    voidFluid2.Surface = "Fluid"
    voidFluid2.Box = "Box"
    voidFluid2.Colors = [
        "Cell Type",
        "Cell Volume Fraction",
        "Component Number",
        "Cooling Rate R",
        "Diagnostics: Cumulative Fluid Fraction Error",
        "Diagnostics: Nf Values",
        "Diagnostics: Pressure Iteration Residual",
        "Dynamic Viscosity",
        "Evaporation Pressure",
        "Fraction Of Fluid",
        "Liquid Region Label",
        "Macroscopic Density",
        "Macroscopic Energy Of Fluid #1",
        "Mass Source Rate Per Unit Open Volume",
        "Melt Region",
        "Normalized Drag Coefficient",
        "Phase Change Mass Flux",
        "Pressure",
        "Solid Fraction",
        "Static Contact Angle",
        "Surface Tension Pressure",
        "Temperature",
        "Temperature Gradient DT/dx",
        "Temperature Gradient DT/dy",
        "Temperature Gradient DT/dz",
        "Temperature Gradient G",
        "Velocity",
        "Volume Fraction After AVRCK Adjustment",
        "Volume Source Rate Per Unit Open Volume",
        "X-velocity",
        "Y-velocity",
        "Z-velocity",
        "vtkGhostType",
    ]

    # init the 'Box' selected for 'Box'
    voidFluid2.Box.Position = [
        -0.0010720646241679788,
        -0.0011556369718164206,
        -0.007207692600786686,
    ]
    voidFluid2.Box.Length = [
        0.14225888310465962,
        0.14221314317546785,
        0.028215383179485798,
    ]

    # create a new 'FLSGRF IsoObject'
    liquid = FLSGRFIsoObject(registrationName="Liquid", Input=flsgrf6pmelt400p1000130um)
    liquid.Surface = "Fluid"
    liquid.Box = "Box"
    liquid.Colors = [
        "Cell Type",
        "Cell Volume Fraction",
        "Component Number",
        "Cooling Rate R",
        "Diagnostics: Cumulative Fluid Fraction Error",
        "Diagnostics: Nf Values",
        "Diagnostics: Pressure Iteration Residual",
        "Dynamic Viscosity",
        "Evaporation Pressure",
        "Fraction Of Fluid",
        "Liquid Region Label",
        "Macroscopic Density",
        "Macroscopic Energy Of Fluid #1",
        "Mass Source Rate Per Unit Open Volume",
        "Melt Region",
        "Normalized Drag Coefficient",
        "Phase Change Mass Flux",
        "Pressure",
        "Solid Fraction",
        "Static Contact Angle",
        "Surface Tension Pressure",
        "Temperature",
        "Temperature Gradient DT/dx",
        "Temperature Gradient DT/dy",
        "Temperature Gradient DT/dz",
        "Temperature Gradient G",
        "Velocity",
        "Volume Fraction After AVRCK Adjustment",
        "Volume Source Rate Per Unit Open Volume",
        "X-velocity",
        "Y-velocity",
        "Z-velocity",
        "vtkGhostType",
    ]

    # init the 'Box' selected for 'Box'
    liquid.Box.Position = [
        -0.0010720646241679788,
        -0.0011556369718164206,
        -0.007207692600786686,
    ]
    liquid.Box.Length = [0.14225888310465962, 0.14221314317546785, 0.028215383179485798]

    # create a new 'FLSGRF IsoObject'
    solidifiedLiquid = FLSGRFIsoObject(
        registrationName="Solidified Liquid", Input=flsgrf6pmelt400p1000130um
    )
    solidifiedLiquid.Surface = "Fluid"
    solidifiedLiquid.Box = "Box"
    solidifiedLiquid.Colors = [
        "Cell Type",
        "Cell Volume Fraction",
        "Component Number",
        "Cooling Rate R",
        "Diagnostics: Cumulative Fluid Fraction Error",
        "Diagnostics: Nf Values",
        "Diagnostics: Pressure Iteration Residual",
        "Dynamic Viscosity",
        "Evaporation Pressure",
        "Fraction Of Fluid",
        "Liquid Region Label",
        "Macroscopic Density",
        "Macroscopic Energy Of Fluid #1",
        "Mass Source Rate Per Unit Open Volume",
        "Melt Region",
        "Normalized Drag Coefficient",
        "Phase Change Mass Flux",
        "Pressure",
        "Solid Fraction",
        "Static Contact Angle",
        "Surface Tension Pressure",
        "Temperature",
        "Temperature Gradient DT/dx",
        "Temperature Gradient DT/dy",
        "Temperature Gradient DT/dz",
        "Temperature Gradient G",
        "Velocity",
        "Volume Fraction After AVRCK Adjustment",
        "Volume Source Rate Per Unit Open Volume",
        "X-velocity",
        "Y-velocity",
        "Z-velocity",
        "vtkGhostType",
    ]

    # init the 'Box' selected for 'Box'
    solidifiedLiquid.Box.Position = [
        -0.0010720646241679788,
        -0.0011556369718164206,
        -0.007207692600786686,
    ]
    solidifiedLiquid.Box.Length = [
        0.14225888310465962,
        0.14221314317546785,
        0.028215383179485798,
    ]

    # show data in view
    hotspotsDisplay = Show(hotspots, renderView1, "UnstructuredGridRepresentation")

    # rescale color and/or opacity maps used to exactly fit the current data range
    hotspotsDisplay.RescaleTransferFunctionToDataRange(False, True)

    # get color transfer function/color map for 'SolidificationTime'
    solidificationTimeLUT = GetColorTransferFunction("SolidificationTime")

    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(solidificationTimeLUT, renderView1)

    # set active source
    SetActiveSource(fluid)

    # reset view to fit data
    renderView1.ResetCamera(False)

    # get opacity transfer function/opacity map for 'Temperature'
    temperaturePWF = GetOpacityTransferFunction("Temperature")

    # Properties modified on animationScene1
    animationScene1.AnimationTime = 0.0

    # get the time-keeper
    timeKeeper1 = GetTimeKeeper()

    Hide(hotspots, renderView1)

    # layout/tab size in pixels
    # case1flsgrf6pmelt400p1000130um.SetSize(1391, 611)

    # current camera placement for renderView1
    renderView1.CameraPosition = [-0.015, -0.015, 0.12678054413808706]
    renderView1.CameraFocalPoint = [-0.015, -0.015, 0.006651218282058855]
    renderView1.CameraParallelScale = 0.03545
    renderView1.CameraParallelProjection = 1

    animationScene = GetAnimationScene()

    for i in range(len(timeStep)):
        animationScene.AnimationTime = timeStep[i]
        renderView1.Update()

        # Calculate new camera position, focal point, and view up based on the time value
        new_camera_position = [xPos[i], yPos[i], 0.39297822260506643]
        new_camera_focal_point = [xPos[i], yPos[i], 0.006651218282058835]
        new_camera_view_up = [0, 1, 0]

        renderView1.CameraPosition = new_camera_position
        renderView1.CameraFocalPoint = new_camera_focal_point
        renderView1.CameraViewUp = new_camera_view_up
        # save screenshot

        SaveScreenshot(
            f"C:/Users/Aashman Sharma/Documents/Paraview/data{i}.png",
            case1flsgrf6pmelt400p1000130um,
            ImageResolution=[1391, 611],
        )

    # ================================================================
    # addendum: following script captures some of the application
    # state to faithfully reproduce the visualization during playback
    # ================================================================

    # --------------------------------
    # saving layout sizes for layouts

    # layout/tab size in pixels
    # case1flsgrf6pmelt400p1000130um.SetSize(1391, 611)

    # -----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
    renderView1.CameraPosition = [-0.015, -0.015, 0.12678054413808706]
    renderView1.CameraFocalPoint = [-0.015, -0.015, 0.006651218282058855]
    renderView1.CameraParallelScale = 0.06829368646690677
    renderView1.CameraParallelProjection = 1

    # --------------------------------------------
    # uncomment the following to render all views
    # RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).


def generateData(speed, hatch):
    xduration = 0.1 / speed
    yduration = hatch / 125

    count = 0
    prevtime = 0

    check = False
    for x in range(11):
        curSpeed = speed

        if count % 2 == 0:
            if count % 4 != 0:
                curSpeed *= -1

            if check:
                prevtime += 0.0000008
                rounded_number = round(prevtime, 8)
                timeValues.append(rounded_number)
            xVel.append(curSpeed)
            yVel.append(0)
            prevtime += xduration
            xVel.append(curSpeed)
            yVel.append(0)
            rounded_number = round(prevtime, 8)
            timeValues.append(rounded_number)
            check = True
        else:
            prevtime += 0.0000008
            rounded_number = round(prevtime, 8)
            timeValues.append(rounded_number)
            yVel.append(125)
            xVel.append(0)
            prevtime += yduration
            yVel.append(125)
            xVel.append(0)
            rounded_number = round(prevtime, 8)
            timeValues.append(rounded_number)

        count += 1
    prevtime += 0.0000008
    rounded_number = round(prevtime, 8)
    timeValues.append(rounded_number)
    yVel.append(0)
    xVel.append(0)

    createXPos(speed)
    createYPos(hatch)

    print("Speed:", speed, "     ", "Hatch:", hatch)
    print("Time             X         Y")
    print("----------------------------------")
    i = 0
    while i < len(timeValues):
        print(timeValues[i], "    ", xPos[i], "   ", yPos[i])
        i = i + 1


def createXPos(speed):
    dt = 0.00002
    prevPos = 0
    xPos.append(prevPos)

    i = 0

    curTimeStep = 0

    while i < len(timeValues) - 1:
        while timeValues[i + 1] > curTimeStep:
            if abs(xVel[i]) == speed and abs(xVel[i + 1]) == speed:
                dx = dt * xVel[i]
                prevPos += dx
                xPos.append(round(prevPos, 6))
            else:
                xPos.append(round(prevPos, 6))
            curTimeStep += dt
            timeStep.append(round(curTimeStep, 6))
        i = i + 1


def createYPos():
    dt = 0.00002
    speed = 125
    prevPos = 0
    yPos.append(prevPos)

    i = 0

    curTimeStep = timeStep[i]

    while i < len(timeValues) - 1:
        while timeValues[i + 1] > curTimeStep:
            if yVel[i] == speed and yVel[i + 1] == speed:
                dy = dt * yVel[i]
                prevPos += dy
                yPos.append(round(prevPos, 6))
            else:
                yPos.append(round(prevPos, 6))
            curTimeStep += dt

        i = i + 1


runProcessing()
