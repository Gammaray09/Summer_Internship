# trace generated using paraview version 5.10.1
# import paraview
# paraview.compatibility.major = 5
# paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
import csv
import time
import numpy as np
import matplotlib.pyplot as plt


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

    # hide data in view
    Hide(time, renderView1)

    # hide data in view
    Hide(fLOW3DLOGO, renderView1)

    # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
    temperatureLUT.ApplyPreset("Blue Orange (divergent)", True)

    # Properties modified on fluid
    fluid.IsoValue = 0.02
    fluid.Colors = ["Pressure", "Temperature"]

    # Properties modified on fluid.Box
    fluid.Box.UseReferenceBounds = 1
    fluid.Box.Bounds = [
        0.0195,
        0.0205,
        0.005,
        0.035,
        -0.00720769,
        0.0210077,
    ]
    fluid.Box.Position = [0.0, 0.0, 0.0]
    fluid.Box.Length = [1.0, 1.0, 1.0]

    # update the view to ensure updated data information
    renderView1.Update()

    # Properties modified on animationScene1
    animationScene1.AnimationTime = 0.0

    # get the time-keeper
    timeKeeper1 = GetTimeKeeper()

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=fluid.Box)

    # change representation type
    fluidDisplay.SetRepresentationType("Points")

    # change representation type
    fluidDisplay.SetRepresentationType("Point Gaussian")

    # change representation type
    fluidDisplay.SetRepresentationType("Outline")

    # change representation type
    fluidDisplay.SetRepresentationType("Point Gaussian")

    # change representation type
    fluidDisplay.SetRepresentationType("Points")

    # change representation type
    fluidDisplay.SetRepresentationType("Surface")

    # Properties modified on fluid
    fluid.a3DClip = 1

    # Properties modified on fluid.Box
    fluid.Box.Bounds = [0.0195, 0.0205, 0.005, 0.035, -0.00720769, 0.0210077]

    # update the view to ensure updated data information
    renderView1.Update()

    # reset view to fit data
    renderView1.ResetCamera(False)

    # reset view to fit data
    renderView1.ResetCamera(False)

    # reset view to fit data
    renderView1.ResetCamera(False)

    # update the view to ensure updated data information
    renderView1.Update()

    # -----------------------------All Code Above is auto generated by Trace--------------------------------------------

    # hides fluid and hotspot data
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

    # Intial Camera placement
    renderView1.CameraPosition = [0.2, 0.02, 0.0068047]
    renderView1.CameraFocalPoint = [0.2, 0.02, 0.0068047]
    renderView1.CameraParallelScale = 0.03545
    renderView1.CameraParallelProjection = 1

    # Get current animation data
    animationScene = GetAnimationScene()

    camXPos = []
    camYPos = []
    timeStep = []

    # Runs Anant's trajectory functions
    timeStep, camXPos, camYPos = runTraj()

    # Prints all time and trajectory values in terminal
    i = 0
    while i < len(timeStep):
        time = timeStep[i]
        scientific_notation = format(time, ".2e")
        print(
            i, "     ", scientific_notation, "        ", camXPos[i], "   ", camYPos[i]
        )
        i = i + 1

    # This loop iterates through every timestep in the timestep arr and set camera/clip position with
    # corresponding index in cameraPos and clipPos arrays. After camera/clip are at correct position a
    # screenshot is taken and saved to a specific folder

    for i in range(5):
        # Sets animation to current timestep
        animationScene.AnimationTime = timeStep[i]
        renderView1.Update()

        # Gets corresponding postion value based on timestep index
        fluid.IsoValue = 0.02
        new_camera_position = [camXPos[i], camYPos[i], 0.0068047]
        new_camera_focal_point = [camXPos[i], camYPos[i], 0.0068047]
        new_camera_view_up = [0, 1, 0]

        fluid.Box.UseReferenceBounds = 1
        fluid.Box.Bounds = [
            0.0195,
            0.0205,
            0.005,
            0.035,
            -0.00720769,
            0.0210077,
        ]
        fluid.Box.Position = [0.0, 0.0, 0.0]
        fluid.Box.Length = [1.0, 1.0, 1.0]

        temperatureLUT.RescaleTransferFunction(300.0, 3000.0)

        # Sets position of camera and clip
        renderView1.CameraPosition = new_camera_position
        renderView1.CameraFocalPoint = new_camera_focal_point
        renderView1.CameraViewUp = new_camera_view_up
        renderView1.CameraParallelScale = 0.03545
        renderView1.CameraParallelProjection = 1

        renderView1.Update()

        # save screenshot in folder
        scientific_notation = format(timeStep[i], ".2e")
        SaveScreenshot(
            f"C:/Users/Aashman Sharma/Documents/Paraview/output_side/snap_{i}.tiff",
            case1flsgrf6pmelt400p1000130um,
            ImageResolution=[1632, 1632],
        )


# -----------------------------------------------Anant's Functions----------------------------------------------


def ReadLaserTrajectory(loc, s, h):
    print("runTraj")
    P0 = 400
    locF = loc + "\\"
    fnameP = locF + str(P0) + "_" + str(s) + "_" + str(h) + "-power.csv"
    fnamex = locF + str(P0) + "_" + str(s) + "_" + str(h) + "-x.csv"
    fnamey = locF + str(P0) + "_" + str(s) + "_" + str(h) + "-y.csv"

    def read_csv_as_float(filename):
        with open(filename, "r") as f:
            reader = csv.reader(f)
            data = np.array([list(map(float, row)) for row in reader])
        return data

    Fp = read_csv_as_float(fnameP)
    Fx = read_csv_as_float(fnamex)
    Fy = read_csv_as_float(fnamey)

    # Read data from the second column of the first CSV file
    Ft = Fx[:, 0]
    Fp = Fp[:, 1]
    Fx = Fx[:, 1]
    Fy = Fy[:, 1]

    dat = np.column_stack((Ft, Fx, Fy, Fp))

    return dat


def GetLaserTrajectory(dat, x0, y0, t0, dt, Nt):
    t = t0 + dt * np.linspace(0, Nt - 1, Nt)
    p = np.zeros(Nt)
    x = np.zeros(Nt)
    y = np.zeros(Nt)
    vx = np.zeros(Nt)
    vy = np.zeros(Nt)

    tLim = dat[:, 0]
    vxLim = dat[:, 1]
    vyLim = dat[:, 2]
    pLim = dat[:, 3]

    Nlim = dat.shape[0]
    dtLim = np.diff(tLim)
    dtm = np.min(dtLim)
    tM = np.max(t)
    NtL = int(np.ceil(tM / dtm))
    tL = t0 + dtm * np.linspace(0, NtL - 1, NtL)

    pL = np.zeros(NtL)
    xL = np.zeros(NtL)
    yL = np.zeros(NtL)
    vxL = np.zeros(NtL)
    vyL = np.zeros(NtL)

    for i in range(1, NtL):
        for j in range(Nlim - 1):
            if tL[i] < tLim[0]:
                pL[i], vxL[i], vyL[i] = pLim[0], vxLim[0], vyLim[0]
                break
            elif tL[i] >= tLim[j] and tL[i] < tLim[j + 1]:
                # Commented out the interpolation code as it's commented in the original MATLAB code
                # tFac = (tL[i] - tLim[j]) / (tLim[j+1] - tLim[j])
                pL[i], vxL[i], vyL[i] = pLim[j], vxLim[j], vyLim[j]
                break
            elif tL[i] >= tLim[Nlim - 1]:
                pL[i], vxL[i], vyL[i] = pLim[Nlim - 1], vxLim[Nlim - 1], vyLim[Nlim - 1]

    xL[0], yL[0] = x0, y0
    for i in range(1, NtL):
        xL[i] = xL[i - 1] + dtm * vxL[i - 1]
        yL[i] = yL[i - 1] + dtm * vyL[i - 1]

    p = np.interp(t, tL, pL)
    vx = np.interp(t, tL, vxL)
    vy = np.interp(t, tL, vyL)
    x = np.interp(t, tL, xL)
    y = np.interp(t, tL, yL)

    pOn = p != 0

    datTraj = {"t": t, "x": x, "y": y, "vx": vx, "vy": vy, "p": p, "pOn": pOn}

    return datTraj


def runTraj():
    loc = r"C:\Users\Aashman Sharma\Documents\Paraview\Time_Series"
    Nt = 356
    xCam = 0.0215
    yCam = 0.02
    t0 = 0
    dt = 1.9e-5
    s = 1000
    h = 130
    dat = ReadLaserTrajectory(loc, s, h)
    datTrajCam = GetLaserTrajectory(dat, xCam, yCam, t0, dt, Nt)

    timeStep = datTrajCam.get("t")
    camXPos = datTrajCam.get("x")
    camYPos = datTrajCam.get("y")

    return timeStep, camXPos, camYPos


# --------------------------------------------------------------------------------------------------------------

# Runs the whole code and prints out runtime
startTime = time.perf_counter()
runProcessing()
finalTime = time.perf_counter()
print(finalTime - startTime)
