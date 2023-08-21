# trace generated using paraview version 5.10.1
# import paraview
# paraview.compatibility.major = 5
# paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
import csv

xVel = []
yVel = []
camXPos = []
camYPos = []
clipXPos = []
clipYPos = []
timeValues = []
timeStep = []
power = []
checkPower = []
numSteps = 355


def runProcessing():
    ResetSession()
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
    renderView1.OrientationAxesVisibility = 0
    renderView1.AxesGrid.Visibility = 0
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

    # set active source
    SetActiveSource(flsgrf6pmelt400p1000130um)

    # get color transfer function/color map for 'Pressure'
    pressureLUT = GetColorTransferFunction("Pressure")

    # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
    pressureLUT.ApplyPreset("X Ray", True)

    # get color transfer function/color map for 'Temperature'
    temperatureLUT = GetColorTransferFunction("Temperature")

    # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
    temperatureLUT.ApplyPreset("X Ray", True)

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
    solidificationTimeLUT.RGBPoints = [
        9.891147101370734e-07,
        0.231373,
        0.298039,
        0.752941,
        0.0034944820468467697,
        0.865003,
        0.865003,
        0.865003,
        0.006987974978983402,
        0.705882,
        0.0156863,
        0.14902,
    ]
    solidificationTimeLUT.ScalarRangeInitialized = 1.0

    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(solidificationTimeLUT, renderView1)

    # set active source
    SetActiveSource(fluid)

    # reset view to fit data
    renderView1.ResetCamera(False)

    # get opacity transfer function/opacity map for 'Temperature'
    temperaturePWF = GetOpacityTransferFunction("Temperature")
    temperaturePWF.Points = [
        423.025146484375,
        0.0,
        0.5,
        0.0,
        1841.5760498046875,
        1.0,
        0.5,
        0.0,
    ]
    temperaturePWF.ScalarRangeInitialized = 1

    # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
    temperatureLUT.ApplyPreset("X Ray", True)

    # invert the transfer function
    temperatureLUT.InvertTransferFunction()

    # create a new 'Clip'
    clip1 = Clip(registrationName="Clip1", Input=fluid)
    clip1.ClipType = "Plane"
    clip1.HyperTreeGridClipper = "Plane"
    clip1.Scalars = ["POINTS", "Pressure"]
    clip1.Value = 5618517.0

    # init the 'Plane' selected for 'ClipType'
    clip1.ClipType.Origin = [
        0.07005737855433836,
        0.06995093158184318,
        0.006651218282058835,
    ]

    # init the 'Plane' selected for 'HyperTreeGridClipper'
    clip1.HyperTreeGridClipper.Origin = [
        0.07005737855433836,
        0.06995093158184318,
        0.006651218282058835,
    ]

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=clip1.ClipType)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=clip1.ClipType)

    # Properties modified on clip1
    clip1.ClipType = "Box"
    # Properties modified on clip1.ClipType
    clip1.ClipType.Length = [0.07, 0.07, 0.07]

    # show data in view
    clip1Display = Show(clip1, renderView1, "UnstructuredGridRepresentation")

    # trace defaults for the display properties.
    clip1Display.Representation = "Surface"
    clip1Display.ColorArrayName = ["POINTS", "Temperature"]
    clip1Display.LookupTable = temperatureLUT
    clip1Display.SelectTCoordArray = "None"
    clip1Display.SelectNormalArray = "Normals"
    clip1Display.SelectTangentArray = "None"
    clip1Display.OSPRayScaleArray = "Normals"
    clip1Display.OSPRayScaleFunction = "PiecewiseFunction"
    clip1Display.SelectOrientationVectors = "None"
    clip1Display.ScaleFactor = 0.006999999868276064
    clip1Display.SelectScaleArray = "None"
    clip1Display.GlyphType = "Arrow"
    clip1Display.GlyphTableIndexArray = "None"
    clip1Display.GaussianRadius = 0.0003499999934138032
    clip1Display.SetScaleArray = ["POINTS", "Normals"]
    clip1Display.ScaleTransferFunction = "PiecewiseFunction"
    clip1Display.OpacityArray = ["POINTS", "Normals"]
    clip1Display.OpacityTransferFunction = "PiecewiseFunction"
    clip1Display.DataAxesGrid = "GridAxesRepresentation"
    clip1Display.PolarAxes = "PolarAxesRepresentation"
    clip1Display.ScalarOpacityFunction = temperaturePWF
    clip1Display.ScalarOpacityUnitDistance = 0.003282433238165534
    clip1Display.OpacityArrayName = ["POINTS", "Normals"]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    clip1Display.ScaleTransferFunction.Points = [
        -1.0,
        0.0,
        0.5,
        0.0,
        0.9993227124214172,
        1.0,
        0.5,
        0.0,
    ]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    clip1Display.OpacityTransferFunction.Points = [
        -1.0,
        0.0,
        0.5,
        0.0,
        0.9993227124214172,
        1.0,
        0.5,
        0.0,
    ]

    # hide data in view
    Hide(fluid, renderView1)
    Hide(hotspots, renderView1)

    ColorBy(fluidDisplay, ("POINTS", "Temperature"))

    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(temperatureLUT, renderView1)

    # rescale color and/or opacity maps used to include current data range
    fluidDisplay.RescaleTransferFunctionToDataRange(True, False)

    # hide color bar/color legend
    fluidDisplay.SetScalarBarVisibility(renderView1, False)

    # update the view to ensure updated data information
    renderView1.Update()

    # current camera placement for renderView1
    renderView1.CameraPosition = [-0.015, -0.015, 0.12678054413808706]
    renderView1.CameraFocalPoint = [-0.015, -0.015, 0.006651218282058855]
    renderView1.CameraParallelScale = 0.03545
    renderView1.CameraParallelProjection = 1

    animationScene = GetAnimationScene()

    numSteps = animationScene.EndTime + 1

    print(numSteps)

    # createData(100, 0.013)

    readCsv()
    createPowerPos()
    createXPos(100, 0.02, camXPos)
    createYPos(0.02, camYPos)
    createXPos(100, -0.015, clipXPos)
    createYPos(-0.015, clipYPos)
    fillValues()

    i = 0
    while i < len(timeStep):
        time = timeStep[i]
        scientific_notation = format(time, ".2e")
        print(
            i, "     ", scientific_notation, "        ", camXPos[i], "   ", camYPos[i]
        )
        i = i + 1

    for i in range(len(timeStep)):
        if checkPower[i] == True:
            animationScene.AnimationTime = timeStep[i]
            renderView1.Update()

            # Calculate new camera position, focal point, and view up based on the time value
            new_camera_position = [camXPos[i], camXPos[i], 0.39297822260506643]
            new_camera_focal_point = [camXPos[i], camYPos[i], 0.006651218282058835]
            new_camera_view_up = [0, 1, 0]
            new_clip_position = [clipXPos[i], clipYPos[i], -0.01]

            renderView1.CameraPosition = new_camera_position
            renderView1.CameraFocalPoint = new_camera_focal_point
            renderView1.CameraViewUp = new_camera_view_up
            clip1.ClipType.Position = new_clip_position
            temperatureLUT.RescaleTransferFunction(300.0, 3000.0)
            renderView1.Update()
            # save screenshot

            SaveScreenshot(
                f"C:/Users/Aashman Sharma/Documents/Paraview/output/data{i}.png",
                case1flsgrf6pmelt400p1000130um,
                ImageResolution=[1632, 1632],
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


def createData(speed, hatch):
    timeValues.append(0)
    timeStep.append(0)

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


def readCsv():
    xCsv = r"C:\Users\Aashman Sharma\Documents\Paraview\Time_Series\400_1000_130-x.csv"
    yCsv = r"C:\Users\Aashman Sharma\Documents\Paraview\Time_Series\400_1000_130-y.csv"
    pCsv = (
        r"C:\Users\Aashman Sharma\Documents\Paraview\Time_Series\400_1000_130-power.csv"
    )

    with open(xCsv, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            timeValues.append(float(row[0]))
            xVel.append(float(row[1]))
    with open(yCsv, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            yVel.append(float(row[1]))
    with open(pCsv, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            power.append(float(row[1]))


def createXPos(speed, initialPos, xArr):
    arrFull = False
    if len(timeStep) > 1:
        arrFull = True

    dt = 0.00002
    prevPos = initialPos
    xArr.append(prevPos)

    i = 0

    curTimeStep = 0

    while i < len(timeValues) - 1:
        while timeValues[i + 1] > curTimeStep:
            if abs(xVel[i]) == speed and abs(xVel[i + 1]) == speed:
                dx = dt * xVel[i]
                prevPos += dx
                xArr.append(round(prevPos, 6))
            else:
                xArr.append(round(prevPos, 6))
            curTimeStep += dt

            if arrFull == False:
                timeStep.append(curTimeStep)
        i = i + 1


def createYPos(initialPos, yArr):
    dt = 0.00002
    speed = 125
    prevPos = initialPos
    yArr.append(prevPos)

    i = 0

    curTimeStep = timeStep[i]

    while i < len(timeValues) - 1:
        while timeValues[i + 1] > curTimeStep:
            if yVel[i] == speed and yVel[i + 1] == speed:
                dy = dt * yVel[i]
                prevPos += dy
                yArr.append(round(prevPos, 6))
            else:
                yArr.append(round(prevPos, 6))
            curTimeStep += dt

        i = i + 1


def createPowerPos():
    dt = 0.00002
    i = 0

    curTimeStep = i

    while i < len(timeValues) - 1:
        while timeValues[i + 1] > curTimeStep:
            if power[i] > 0:
                checkPower.append(True)
            else:
                checkPower.append(False)
            curTimeStep += dt

        i = i + 1


def fillValues():
    dt = 0.00002
    prevTime = timeStep[len(timeStep) - 1]
    camPrevXPos = camXPos[len(timeStep) - 1]
    camPrevYPos = camYPos[len(timeStep) - 1]
    clipPrevXPos = clipXPos[len(timeStep) - 1]
    clipPrevYPos = clipYPos[len(timeStep) - 1]

    if len(timeStep) != numSteps:
        while len(timeStep) != numSteps + 1:
            prevTime += dt
            timeStep.append(prevTime)
            camXPos.append(camPrevXPos)
            camYPos.append(camPrevYPos)
            clipXPos.append(clipPrevXPos)
            clipYPos.append(clipPrevYPos)
            checkPower.append(True)


runProcessing()
