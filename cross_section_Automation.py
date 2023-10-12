# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Restart timeline'
flsgrf6pmelt400p1000130um = Restarttimeline(registrationName='flsgrf.6-p-melt-400p-1000-130um', FileName='C:\\Users\\aashm\\Documents\\Summer_Internship\\sims\\6-p-melt-400p-1000-130um\\flsgrf.6-p-melt-400p-1000-130um')
flsgrf6pmelt400p1000130um.CellArrays = ['Static Contact Angle', 'Normalized Drag Coefficient', 'Solid Fraction', 'Dynamic Viscosity', 'Diagnostics: Nf Values', 'Liquid Region Label', 'Pressure', 'Phase Change Mass Flux', 'Diagnostics: Pressure Iteration Residual', 'Surface Tension Pressure', 'Mass Source Rate Per Unit Open Volume', 'Volume Source Rate Per Unit Open Volume', 'Macroscopic Density', 'Macroscopic Energy Of Fluid #1', 'Cooling Rate R', 'Evaporation Pressure', 'Melt Region', 'Temperature Gradient G', 'Temperature Gradient DT/dx', 'Temperature Gradient DT/dy', 'Temperature Gradient DT/dz', 'Temperature', 'X-velocity', 'Y-velocity', 'Diagnostics: Cumulative Fluid Fraction Error', 'Z-velocity']
flsgrf6pmelt400p1000130um.HistoryData = ['Diagnostics: Time-step Size', 'Diagnostics: Elapsed Clock Time', 'Diagnostics: Elapsed Clock Time Per Time Step', 'Diagnostics: % Parallel Efficiency', 'Fill Fraction', 'Solidified Volume Fraction', 'Diagnostics: Time-step Stability Limit', 'Diagnostics: X-direction Convective Time-step Limit', 'Diagnostics: Y-direction Convective Time-step Limit', 'Diagnostics: Z-direction Convective Time-step Limit', 'Diagnostics: Viscous Time-step Limit', 'Diagnostics: Free Surface Time-step Limit', 'Diagnostics: Surface Tension Time-step Limit', 'Diagnostics: Thermal Conduction Time-step Limit', 'Diagnostics: Pressure Convergence Criterion', 'Diagnostics: Pressure Relaxation Factor', 'Diagnostics: Maximum Pressure Residual', 'Diagnostics: Pressure Iteration Count', 'Diagnostics: Thermal Convergence Criterion', 'Diagnostics: Thermal Relaxation Factor', 'Diagnostics: Maximum Normalized Thermal Residual', 'Diagnostics: Maximum Thermal Residual In Degrees', 'Diagnostics: Thermal Iteration Count', 'Average Vorticity', 'Diagnostics: Convective Volume Error', 'Diagnostics: Convective Volume Error; % Lost', 'Diagnostics: Interblock Boundary Volume Error', 'Diagnostics: Interblock Boundary Volume Error; % Lost', 'Volume Of Fluid #1', 'Fluid Surface Area', 'Solidified Volume Of Fluid 1', 'Cumulative Evaporated Mass', 'Fluid Center Of Mass X-coordinate', 'Fluid Center Of Mass Y-coordinate', 'Fluid Center Of Mass Z-coordinate', 'Diagnostics: Fluid 1 Volume Net Influx', 'Mass-averaged Fluid Mean Kinetic Energy', 'Total Fluid Mass', 'Diagnostics: Accumulated Fluid Mass Source', 'Total Fluid #1 Thermal Energy', 'Minimum Fluid #1 Temperature', 'Maximum Fluid #1 Temperature', 'Average Fluid #1 Temperature', 'Cooling Rate R Mass', 'Evaporation Pressure Mass', 'Melt Region Mass', 'Temperature Gradient G Mass', 'Temperature Gradient DT/dx Mass', 'Temperature Gradient DT/dy Mass', 'Temperature Gradient DT/dz Mass', 'Total Number Of Particles', 'Hot Spots', 'Laser #  1 : X-coordinate', 'Laser #  1 : Y-coordinate', 'Laser #  1 : Z-coordinate', 'Mesh Block 2: Zmax Fluid #1 Volume Flow Rate', 'Mesh Block 2: Zmax Specified Pressure', 'Mesh Block 2: Zmax Specified Fluid Fraction', 'Mesh Block 2: Zmax Specified X-velocity', 'Mesh Block 2: Zmax Specified Y-velocity', 'Mesh Block 2: Zmax Specified Fluid #1 Temperature', 'Mesh Block 2: Zmax Specified Void Temperature', 'Mesh Block 2: Zmax Specified Melt Region']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# rename source object
RenameSource('Case 1: flsgrf.6-p-melt-400p-1000-130um', flsgrf6pmelt400p1000130um)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# destroy renderView1
Delete(renderView1)
del renderView1

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelProjection = 1
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# get layout
case1flsgrf6pmelt400p1000130um = GetLayoutByName("Case 1: flsgrf.6-p-melt-400p-1000-130um")

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView1, layout=case1flsgrf6pmelt400p1000130um, hint=0)

# create a new 'Annotate Time'
time = AnnotateTime(registrationName='Time')
time.Format = 'Time: %0.3f'

# show data in view
timeDisplay = Show(time, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
timeDisplay.WindowLocation = 'Any Location'
timeDisplay.FontSize = 30

# reset view to fit data
renderView1.ResetCamera(False)

# create a new 'Extract Block'
meshBlock1 = ExtractBlock(registrationName='Mesh Block 1', Input=flsgrf6pmelt400p1000130um)

# show data in view
meshBlock1Display = Show(meshBlock1, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
meshBlock1Display.Representation = 'Outline'
meshBlock1Display.ColorArrayName = [None, '']
meshBlock1Display.SelectTCoordArray = 'None'
meshBlock1Display.SelectNormalArray = 'None'
meshBlock1Display.SelectTangentArray = 'None'
meshBlock1Display.OSPRayScaleFunction = 'PiecewiseFunction'
meshBlock1Display.SelectOrientationVectors = 'Velocity'
meshBlock1Display.ScaleFactor = 0.014225888310465963
meshBlock1Display.SelectScaleArray = 'None'
meshBlock1Display.GlyphType = 'Arrow'
meshBlock1Display.GlyphTableIndexArray = 'None'
meshBlock1Display.GaussianRadius = 0.0007112944155232981
meshBlock1Display.SetScaleArray = [None, '']
meshBlock1Display.ScaleTransferFunction = 'PiecewiseFunction'
meshBlock1Display.OpacityArray = [None, '']
meshBlock1Display.OpacityTransferFunction = 'PiecewiseFunction'
meshBlock1Display.DataAxesGrid = 'GridAxesRepresentation'
meshBlock1Display.PolarAxes = 'PolarAxesRepresentation'
meshBlock1Display.ScalarOpacityUnitDistance = 0.002457596786255209

# create a new 'FLSGRF Extract Particles'
hotspots = FLSGRFExtractParticles(registrationName='Hot spots', Input=flsgrf6pmelt400p1000130um)
hotspots.ParticleClass = 'Hot spots'

# show data in view
hotspotsDisplay = Show(hotspots, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
hotspotsDisplay.Representation = 'Surface'
hotspotsDisplay.ColorArrayName = [None, '']
hotspotsDisplay.SelectTCoordArray = 'None'
hotspotsDisplay.SelectNormalArray = 'Normals'
hotspotsDisplay.SelectTangentArray = 'None'
hotspotsDisplay.OSPRayScaleArray = 'Magnitude'
hotspotsDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
hotspotsDisplay.SelectOrientationVectors = 'None'
hotspotsDisplay.ScaleFactor = 0.11141813099384308
hotspotsDisplay.SelectScaleArray = 'Magnitude'
hotspotsDisplay.GlyphType = 'Arrow'
hotspotsDisplay.GlyphTableIndexArray = 'Magnitude'
hotspotsDisplay.GaussianRadius = 0.005570906549692154
hotspotsDisplay.SetScaleArray = ['POINTS', 'Magnitude']
hotspotsDisplay.ScaleTransferFunction = 'PiecewiseFunction'
hotspotsDisplay.OpacityArray = ['POINTS', 'Magnitude']
hotspotsDisplay.OpacityTransferFunction = 'PiecewiseFunction'
hotspotsDisplay.DataAxesGrid = 'GridAxesRepresentation'
hotspotsDisplay.PolarAxes = 'PolarAxesRepresentation'
hotspotsDisplay.ScalarOpacityUnitDistance = 0.03343245831802152
hotspotsDisplay.OpacityArrayName = ['POINTS', 'Magnitude']

# create a new 'Logo'
fLOW3DLOGO = Logo(registrationName='FLOW-3D LOGO')

# a texture
fLOW3Dpng = CreateTexture('C:\\flow3d\\POST_2023R1\\/f3d/images/FLOW-3D.png')

# change texture
fLOW3DLOGO.Texture = fLOW3Dpng

# show data in view
fLOW3DLOGODisplay = Show(fLOW3DLOGO, renderView1, 'LogoSourceRepresentation')

# set active source
SetActiveSource(flsgrf6pmelt400p1000130um)

# get color transfer function/color map for 'Pressure'
pressureLUT = GetColorTransferFunction('Pressure')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pressureLUT.ApplyPreset('Cool to Warm', True)

# get color transfer function/color map for 'Temperature'
temperatureLUT = GetColorTransferFunction('Temperature')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
temperatureLUT.ApplyPreset('Cool to Warm', True)

# create a new 'FLSGRF IsoObject'
fluid = FLSGRFIsoObject(registrationName='Fluid', Input=flsgrf6pmelt400p1000130um)
fluid.Surface = 'Fluid'
fluid.Box = 'Box'
fluid.Colors = ['Cell Type', 'Cell Volume Fraction', 'Component Number', 'Cooling Rate R', 'Diagnostics: Cumulative Fluid Fraction Error', 'Diagnostics: Nf Values', 'Diagnostics: Pressure Iteration Residual', 'Dynamic Viscosity', 'Evaporation Pressure', 'Fraction Of Fluid', 'Liquid Region Label', 'Macroscopic Density', 'Macroscopic Energy Of Fluid #1', 'Mass Source Rate Per Unit Open Volume', 'Melt Region', 'Normalized Drag Coefficient', 'Phase Change Mass Flux', 'Pressure', 'Solid Fraction', 'Static Contact Angle', 'Surface Tension Pressure', 'Temperature', 'Temperature Gradient DT/dx', 'Temperature Gradient DT/dy', 'Temperature Gradient DT/dz', 'Temperature Gradient G', 'Velocity', 'Volume Fraction After AVRCK Adjustment', 'Volume Source Rate Per Unit Open Volume', 'X-velocity', 'Y-velocity', 'Z-velocity', 'vtkGhostType']

# init the 'Box' selected for 'Box'
fluid.Box.Position = [-0.0010720646241679788, -0.0011556369718164206, -0.007207692600786686]
fluid.Box.Length = [0.14225888310465962, 0.14221314317546785, 0.028215383179485798]

# show data in view
fluidDisplay = Show(fluid, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
fluidDisplay.Representation = 'Surface'
fluidDisplay.ColorArrayName = [None, '']
fluidDisplay.SelectTCoordArray = 'None'
fluidDisplay.SelectNormalArray = 'Normals'
fluidDisplay.SelectTangentArray = 'None'
fluidDisplay.OSPRayScaleArray = 'Normals'
fluidDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
fluidDisplay.SelectOrientationVectors = 'None'
fluidDisplay.ScaleFactor = 0.014025523991585943
fluidDisplay.SelectScaleArray = 'None'
fluidDisplay.GlyphType = 'Arrow'
fluidDisplay.GlyphTableIndexArray = 'None'
fluidDisplay.GaussianRadius = 0.0007012761995792971
fluidDisplay.SetScaleArray = ['POINTS', 'Normals']
fluidDisplay.ScaleTransferFunction = 'PiecewiseFunction'
fluidDisplay.OpacityArray = ['POINTS', 'Normals']
fluidDisplay.OpacityTransferFunction = 'PiecewiseFunction'
fluidDisplay.DataAxesGrid = 'GridAxesRepresentation'
fluidDisplay.PolarAxes = 'PolarAxesRepresentation'
fluidDisplay.ScalarOpacityUnitDistance = 0.00342998138298535
fluidDisplay.OpacityArrayName = ['POINTS', 'Normals']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
fluidDisplay.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
fluidDisplay.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# rescale color and/or opacity maps used to exactly fit the current data range
fluidDisplay.RescaleTransferFunctionToDataRange(False, True)

# create a new 'FLSGRF IsoObject'
openVolume = FLSGRFIsoObject(registrationName='Open Volume', Input=flsgrf6pmelt400p1000130um)
openVolume.Surface = 'Fluid'
openVolume.Box = 'Box'
openVolume.Colors = ['Cell Type', 'Cell Volume Fraction', 'Component Number', 'Cooling Rate R', 'Diagnostics: Cumulative Fluid Fraction Error', 'Diagnostics: Nf Values', 'Diagnostics: Pressure Iteration Residual', 'Dynamic Viscosity', 'Evaporation Pressure', 'Fraction Of Fluid', 'Liquid Region Label', 'Macroscopic Density', 'Macroscopic Energy Of Fluid #1', 'Mass Source Rate Per Unit Open Volume', 'Melt Region', 'Normalized Drag Coefficient', 'Phase Change Mass Flux', 'Pressure', 'Solid Fraction', 'Static Contact Angle', 'Surface Tension Pressure', 'Temperature', 'Temperature Gradient DT/dx', 'Temperature Gradient DT/dy', 'Temperature Gradient DT/dz', 'Temperature Gradient G', 'Velocity', 'Volume Fraction After AVRCK Adjustment', 'Volume Source Rate Per Unit Open Volume', 'X-velocity', 'Y-velocity', 'Z-velocity', 'vtkGhostType']

# init the 'Box' selected for 'Box'
openVolume.Box.Position = [-0.0010720646241679788, -0.0011556369718164206, -0.007207692600786686]
openVolume.Box.Length = [0.14225888310465962, 0.14221314317546785, 0.028215383179485798]

# create a new 'FLSGRF IsoObject'
solid = FLSGRFIsoObject(registrationName='Solid', Input=flsgrf6pmelt400p1000130um)
solid.Surface = 'Fluid'
solid.Box = 'Box'
solid.Colors = ['Cell Type', 'Cell Volume Fraction', 'Component Number', 'Cooling Rate R', 'Diagnostics: Cumulative Fluid Fraction Error', 'Diagnostics: Nf Values', 'Diagnostics: Pressure Iteration Residual', 'Dynamic Viscosity', 'Evaporation Pressure', 'Fraction Of Fluid', 'Liquid Region Label', 'Macroscopic Density', 'Macroscopic Energy Of Fluid #1', 'Mass Source Rate Per Unit Open Volume', 'Melt Region', 'Normalized Drag Coefficient', 'Phase Change Mass Flux', 'Pressure', 'Solid Fraction', 'Static Contact Angle', 'Surface Tension Pressure', 'Temperature', 'Temperature Gradient DT/dx', 'Temperature Gradient DT/dy', 'Temperature Gradient DT/dz', 'Temperature Gradient G', 'Velocity', 'Volume Fraction After AVRCK Adjustment', 'Volume Source Rate Per Unit Open Volume', 'X-velocity', 'Y-velocity', 'Z-velocity', 'vtkGhostType']

# init the 'Box' selected for 'Box'
solid.Box.Position = [-0.0010720646241679788, -0.0011556369718164206, -0.007207692600786686]
solid.Box.Length = [0.14225888310465962, 0.14221314317546785, 0.028215383179485798]

# create a new 'FLSGRF IsoObject'
voidFluid2 = FLSGRFIsoObject(registrationName='Void/Fluid 2', Input=flsgrf6pmelt400p1000130um)
voidFluid2.Surface = 'Fluid'
voidFluid2.Box = 'Box'
voidFluid2.Colors = ['Cell Type', 'Cell Volume Fraction', 'Component Number', 'Cooling Rate R', 'Diagnostics: Cumulative Fluid Fraction Error', 'Diagnostics: Nf Values', 'Diagnostics: Pressure Iteration Residual', 'Dynamic Viscosity', 'Evaporation Pressure', 'Fraction Of Fluid', 'Liquid Region Label', 'Macroscopic Density', 'Macroscopic Energy Of Fluid #1', 'Mass Source Rate Per Unit Open Volume', 'Melt Region', 'Normalized Drag Coefficient', 'Phase Change Mass Flux', 'Pressure', 'Solid Fraction', 'Static Contact Angle', 'Surface Tension Pressure', 'Temperature', 'Temperature Gradient DT/dx', 'Temperature Gradient DT/dy', 'Temperature Gradient DT/dz', 'Temperature Gradient G', 'Velocity', 'Volume Fraction After AVRCK Adjustment', 'Volume Source Rate Per Unit Open Volume', 'X-velocity', 'Y-velocity', 'Z-velocity', 'vtkGhostType']

# init the 'Box' selected for 'Box'
voidFluid2.Box.Position = [-0.0010720646241679788, -0.0011556369718164206, -0.007207692600786686]
voidFluid2.Box.Length = [0.14225888310465962, 0.14221314317546785, 0.028215383179485798]

# create a new 'FLSGRF IsoObject'
liquid = FLSGRFIsoObject(registrationName='Liquid', Input=flsgrf6pmelt400p1000130um)
liquid.Surface = 'Fluid'
liquid.Box = 'Box'
liquid.Colors = ['Cell Type', 'Cell Volume Fraction', 'Component Number', 'Cooling Rate R', 'Diagnostics: Cumulative Fluid Fraction Error', 'Diagnostics: Nf Values', 'Diagnostics: Pressure Iteration Residual', 'Dynamic Viscosity', 'Evaporation Pressure', 'Fraction Of Fluid', 'Liquid Region Label', 'Macroscopic Density', 'Macroscopic Energy Of Fluid #1', 'Mass Source Rate Per Unit Open Volume', 'Melt Region', 'Normalized Drag Coefficient', 'Phase Change Mass Flux', 'Pressure', 'Solid Fraction', 'Static Contact Angle', 'Surface Tension Pressure', 'Temperature', 'Temperature Gradient DT/dx', 'Temperature Gradient DT/dy', 'Temperature Gradient DT/dz', 'Temperature Gradient G', 'Velocity', 'Volume Fraction After AVRCK Adjustment', 'Volume Source Rate Per Unit Open Volume', 'X-velocity', 'Y-velocity', 'Z-velocity', 'vtkGhostType']

# init the 'Box' selected for 'Box'
liquid.Box.Position = [-0.0010720646241679788, -0.0011556369718164206, -0.007207692600786686]
liquid.Box.Length = [0.14225888310465962, 0.14221314317546785, 0.028215383179485798]

# create a new 'FLSGRF IsoObject'
solidifiedLiquid = FLSGRFIsoObject(registrationName='Solidified Liquid', Input=flsgrf6pmelt400p1000130um)
solidifiedLiquid.Surface = 'Fluid'
solidifiedLiquid.Box = 'Box'
solidifiedLiquid.Colors = ['Cell Type', 'Cell Volume Fraction', 'Component Number', 'Cooling Rate R', 'Diagnostics: Cumulative Fluid Fraction Error', 'Diagnostics: Nf Values', 'Diagnostics: Pressure Iteration Residual', 'Dynamic Viscosity', 'Evaporation Pressure', 'Fraction Of Fluid', 'Liquid Region Label', 'Macroscopic Density', 'Macroscopic Energy Of Fluid #1', 'Mass Source Rate Per Unit Open Volume', 'Melt Region', 'Normalized Drag Coefficient', 'Phase Change Mass Flux', 'Pressure', 'Solid Fraction', 'Static Contact Angle', 'Surface Tension Pressure', 'Temperature', 'Temperature Gradient DT/dx', 'Temperature Gradient DT/dy', 'Temperature Gradient DT/dz', 'Temperature Gradient G', 'Velocity', 'Volume Fraction After AVRCK Adjustment', 'Volume Source Rate Per Unit Open Volume', 'X-velocity', 'Y-velocity', 'Z-velocity', 'vtkGhostType']

# init the 'Box' selected for 'Box'
solidifiedLiquid.Box.Position = [-0.0010720646241679788, -0.0011556369718164206, -0.007207692600786686]
solidifiedLiquid.Box.Length = [0.14225888310465962, 0.14221314317546785, 0.028215383179485798]

# show data in view
hotspotsDisplay = Show(hotspots, renderView1, 'UnstructuredGridRepresentation')

# rescale color and/or opacity maps used to exactly fit the current data range
hotspotsDisplay.RescaleTransferFunctionToDataRange(False, True)

# get color transfer function/color map for 'SolidificationTime'
solidificationTimeLUT = GetColorTransferFunction('SolidificationTime')
solidificationTimeLUT.RGBPoints = [9.891147101370734e-07, 0.231373, 0.298039, 0.752941, 0.0034944820468467697, 0.865003, 0.865003, 0.865003, 0.006987974978983402, 0.705882, 0.0156863, 0.14902]
solidificationTimeLUT.ScalarRangeInitialized = 1.0

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(solidificationTimeLUT, renderView1)

# set active source
SetActiveSource(fluid)

# reset view to fit data
renderView1.ResetCamera(False)

# get opacity transfer function/opacity map for 'Temperature'
temperaturePWF = GetOpacityTransferFunction('Temperature')
temperaturePWF.Points = [423.025146484375, 0.0, 0.5, 0.0, 1841.5760498046875, 1.0, 0.5, 0.0]
temperaturePWF.ScalarRangeInitialized = 1

# hide data in view
Hide(time, renderView1)

# hide data in view
Hide(fLOW3DLOGO, renderView1)

# hide data in view
Hide(fluid, renderView1)

# set active source
SetActiveSource(flsgrf6pmelt400p1000130um)

# create a new 'FLSGRF Isosurfaces'
fLSGRFIsosurfaces1 = FLSGRFIsosurfaces(registrationName='FLSGRFIsosurfaces1', Input=flsgrf6pmelt400p1000130um)
fLSGRFIsosurfaces1.Surface = ['', '', '', '', '']
fLSGRFIsosurfaces1.Box = 'Box'
fLSGRFIsosurfaces1.Colors = ['Cell Type', 'Cell Volume Fraction', 'Component Number', 'Cooling Rate R', 'Diagnostics: Cumulative Fluid Fraction Error', 'Diagnostics: Nf Values', 'Diagnostics: Pressure Iteration Residual', 'Dynamic Viscosity', 'Evaporation Pressure', 'Fraction Of Fluid', 'Liquid Region Label', 'Macroscopic Density', 'Macroscopic Energy Of Fluid #1', 'Mass Source Rate Per Unit Open Volume', 'Melt Region', 'Normalized Drag Coefficient', 'Phase Change Mass Flux', 'Pressure', 'Solid Fraction', 'Static Contact Angle', 'Surface Tension Pressure', 'Temperature', 'Temperature Gradient DT/dx', 'Temperature Gradient DT/dy', 'Temperature Gradient DT/dz', 'Temperature Gradient G', 'Velocity', 'Volume Fraction After AVRCK Adjustment', 'Volume Source Rate Per Unit Open Volume', 'X-velocity', 'Y-velocity', 'Z-velocity', 'vtkGhostType']

# init the 'Box' selected for 'Box'
fLSGRFIsosurfaces1.Box.Position = [-0.0010720646241679788, -0.0011556369718164206, -0.007207692600786686]
fLSGRFIsosurfaces1.Box.Length = [0.14225888310465962, 0.14221314317546785, 0.028215383179485798]

# rename source object
RenameSource('IsoFluid', fLSGRFIsosurfaces1)

# Properties modified on fLSGRFIsosurfaces1
fLSGRFIsosurfaces1.Surface = ['', '', '', '', 'Cell Type']
fLSGRFIsosurfaces1.IsoValue = 0.02

# Properties modified on fLSGRFIsosurfaces1.Box
fLSGRFIsosurfaces1.Box.UseReferenceBounds = 1
fLSGRFIsosurfaces1.Box.Bounds = [-0.0010720646241679788, 0.14118681848049164, -0.0011556369718164206, 0.14105750620365143, -0.007207692600786686, 0.021007690578699112]
fLSGRFIsosurfaces1.Box.Position = [0.0, 0.0, 0.0]
fLSGRFIsosurfaces1.Box.Length = [1.0, 1.0, 1.0]

# show data in view
fLSGRFIsosurfaces1Display = Show(fLSGRFIsosurfaces1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
fLSGRFIsosurfaces1Display.Representation = 'Surface'
fLSGRFIsosurfaces1Display.ColorArrayName = [None, '']
fLSGRFIsosurfaces1Display.SelectTCoordArray = 'None'
fLSGRFIsosurfaces1Display.SelectNormalArray = 'None'
fLSGRFIsosurfaces1Display.SelectTangentArray = 'None'
fLSGRFIsosurfaces1Display.OSPRayScaleFunction = 'PiecewiseFunction'
fLSGRFIsosurfaces1Display.SelectOrientationVectors = 'None'
fLSGRFIsosurfaces1Display.ScaleFactor = -2.0000000000000002e+298
fLSGRFIsosurfaces1Display.SelectScaleArray = 'None'
fLSGRFIsosurfaces1Display.GlyphType = 'Arrow'
fLSGRFIsosurfaces1Display.GlyphTableIndexArray = 'None'
fLSGRFIsosurfaces1Display.GaussianRadius = -1e+297
fLSGRFIsosurfaces1Display.SetScaleArray = [None, '']
fLSGRFIsosurfaces1Display.ScaleTransferFunction = 'PiecewiseFunction'
fLSGRFIsosurfaces1Display.OpacityArray = [None, '']
fLSGRFIsosurfaces1Display.OpacityTransferFunction = 'PiecewiseFunction'
fLSGRFIsosurfaces1Display.DataAxesGrid = 'GridAxesRepresentation'
fLSGRFIsosurfaces1Display.PolarAxes = 'PolarAxesRepresentation'

# reset view to fit data
renderView1.ResetCamera(False)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on fLSGRFIsosurfaces1
fLSGRFIsosurfaces1.Surface = ['', '', '', '', 'Fraction Of Fluid']

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(fLSGRFIsosurfaces1Display, ('POINTS', 'Temperature'))

# rescale color and/or opacity maps used to include current data range
fLSGRFIsosurfaces1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fLSGRFIsosurfaces1Display.SetScalarBarVisibility(renderView1, True)

# hide color bar/color legend
fLSGRFIsosurfaces1Display.SetScalarBarVisibility(renderView1, False)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
temperatureLUT.ApplyPreset('Rainbow Desaturated', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
temperatureLUT.ApplyPreset('Rainbow Desaturated', True)

# reset view to fit data
renderView1.ResetCamera(False)

# Properties modified on animationScene1
animationScene1.AnimationTime = 1.9994085960206576e-05

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# reset view to fit data
renderView1.ResetCamera(False)

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=fLSGRFIsosurfaces1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'Cell Type']
clip1.Value = 0.5

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.07005737855433836, 0.06995093158184318, 0.006899999687448144]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [0.07005737855433836, 0.06995093158184318, 0.006899999687448144]

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# Properties modified on clip1
clip1.ClipType = 'Box'

# Properties modified on clip1.ClipType
clip1.ClipType.Position = [0.0209997, 0.0, 0.0]
clip1.ClipType.Rotation = [0.0, 0.0, 1.0]
clip1.ClipType.Length = [0.01, 0.035, 0.02]

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'Temperature']
clip1Display.LookupTable = temperatureLUT
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'Normals'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'Cell Type'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 0.0035159811919129426
clip1Display.SelectScaleArray = 'Cell Type'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'Cell Type'
clip1Display.GaussianRadius = 0.00017579905959564713
clip1Display.SetScaleArray = ['POINTS', 'Cell Type']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'Cell Type']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = temperaturePWF
clip1Display.ScalarOpacityUnitDistance = 0.0024608633477585917
clip1Display.OpacityArrayName = ['POINTS', 'Cell Type']

# hide data in view
Hide(fLSGRFIsosurfaces1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
case1flsgrf6pmelt400p1000130um.SetSize(1522, 784)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.1653202545345473, -0.22611215106880345, 0.2442275088166925]
renderView1.CameraFocalPoint = [0.022187968195084534, 0.03375778016237095, -0.0034127562734851064]
renderView1.CameraViewUp = [0.01343683928749043, 0.6936735463215555, 0.7201641913366971]
renderView1.CameraParallelScale = 0.02633867267963493
renderView1.CameraParallelProjection = 1

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).