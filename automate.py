import os
import shutil
from paraview.simple import *


def processData(curFilePath, directory):
    print("Now Running: ", curFilePath)
    ResetSession()
    paraview.simple._DisableFirstRenderCameraReset()

    # create a new 'IOSS Reader'
    melt_pool_oute = IOSSReader(
        registrationName="melt_pool_out.e", FileName=[curFilePath]
    )
    melt_pool_oute.ElementBlocks = ["block_0"]
    melt_pool_oute.NodeBlockFields = [
        "curvature",
        "grad_ls",
        "ls",
        "p",
        "temp",
        "velocity",
    ]
    melt_pool_oute.ElementBlockFields = [
        "delta_function",
        "enthalpy",
        "heaviside_function",
        "liquid_mass_fraction",
        "liquid_volume_fraction",
        "melt_pool_mass_rate",
        "mu",
        "permeability",
        "rho",
        "solid_mass_fraction",
        "solid_volume_fraction",
        "specific_heat",
        "thermal_conductivity",
    ]
    melt_pool_oute.NodeSets = []
    melt_pool_oute.SideSets = []

    # get animation scene
    animationScene1 = GetAnimationScene()

    # get the time-keeper
    timeKeeper1 = GetTimeKeeper()

    # update animation scene based on data timesteps
    animationScene1.UpdateAnimationUsingDataTimeSteps()

    # get active view
    renderView1 = GetActiveViewOrCreate("RenderView")

    # show data in view
    melt_pool_outeDisplay = Show(
        melt_pool_oute, renderView1, "UnstructuredGridRepresentation"
    )

    # trace defaults for the display properties.
    melt_pool_outeDisplay.Representation = "Surface"
    melt_pool_outeDisplay.ColorArrayName = [None, ""]
    melt_pool_outeDisplay.SelectTCoordArray = "None"
    melt_pool_outeDisplay.SelectNormalArray = "None"
    melt_pool_outeDisplay.SelectTangentArray = "None"
    melt_pool_outeDisplay.OSPRayScaleArray = "curvature"
    melt_pool_outeDisplay.OSPRayScaleFunction = "PiecewiseFunction"
    melt_pool_outeDisplay.SelectOrientationVectors = "None"
    melt_pool_outeDisplay.ScaleFactor = 0.001
    melt_pool_outeDisplay.SelectScaleArray = "None"
    melt_pool_outeDisplay.GlyphType = "Arrow"
    melt_pool_outeDisplay.GlyphTableIndexArray = "None"
    melt_pool_outeDisplay.GaussianRadius = 5e-05
    melt_pool_outeDisplay.SetScaleArray = ["POINTS", "curvature"]
    melt_pool_outeDisplay.ScaleTransferFunction = "PiecewiseFunction"
    melt_pool_outeDisplay.OpacityArray = ["POINTS", "curvature"]
    melt_pool_outeDisplay.OpacityTransferFunction = "PiecewiseFunction"
    melt_pool_outeDisplay.DataAxesGrid = "GridAxesRepresentation"
    melt_pool_outeDisplay.PolarAxes = "PolarAxesRepresentation"
    melt_pool_outeDisplay.ScalarOpacityUnitDistance = 0.0006564197879454708
    melt_pool_outeDisplay.OpacityArrayName = ["POINTS", "curvature"]
    melt_pool_outeDisplay.SelectInputVectors = [None, ""]
    melt_pool_outeDisplay.WriteLog = ""

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    melt_pool_outeDisplay.ScaleTransferFunction.Points = [
        0.0,
        0.0,
        0.5,
        0.0,
        1.1757813367477812e-38,
        1.0,
        0.5,
        0.0,
    ]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    melt_pool_outeDisplay.OpacityTransferFunction.Points = [
        0.0,
        0.0,
        0.5,
        0.0,
        1.1757813367477812e-38,
        1.0,
        0.5,
        0.0,
    ]

    # reset view to fit data
    renderView1.ResetCamera(False)

    # changing interaction mode based on data extents
    renderView1.InteractionMode = "2D"
    renderView1.CameraPosition = [0.005, 0.005, 0.0335]
    renderView1.CameraFocalPoint = [0.005, 0.005, 0.0]

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # update the view to ensure updated data information
    renderView1.Update()

    animationScene1.Play()

    # set scalar coloring
    ColorBy(melt_pool_outeDisplay, ("POINTS", "temp"))

    # rescale color and/or opacity maps used to include current data range
    melt_pool_outeDisplay.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    melt_pool_outeDisplay.SetScalarBarVisibility(renderView1, True)

    # get color transfer function/color map for 'temp'
    tempLUT = GetColorTransferFunction("temp")

    # get opacity transfer function/opacity map for 'temp'
    tempPWF = GetOpacityTransferFunction("temp")

    # get 2D transfer function for 'temp'
    tempTF2D = GetTransferFunction2D("temp")

    animationScene1.GoToFirst()

    animationScene1.Play()

    # get layout
    layout1 = GetLayout()

    # layout/tab size in pixels
    layout1.SetSize(1400, 550)

    # current camera placement for renderView1
    renderView1.InteractionMode = "2D"
    renderView1.CameraPosition = [0.005, 0.005, 0.0335]
    renderView1.CameraFocalPoint = [0.005, 0.005, 0.0]
    renderView1.CameraParallelScale = 0.007071067811865475

    # save animation
    SaveAnimation(
        f"C:/Users/Aashman Sharma/Documents/Paraview/Sample_Data/Case_1_output/{directory}/anim.mp4",
        renderView1,
        ImageResolution=[1400, 794],
        FrameRate=20,
        FrameWindow=[0, 75],
    )

    # ================================================================
    # addendum: following script captures some of the application
    # state to faithfully reproduce the visualization during playback
    # ================================================================

    # --------------------------------
    # saving layout sizes for layouts

    # layout/tab size in pixels
    layout1.SetSize(1400, 550)

    # -----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
    renderView1.InteractionMode = "2D"
    renderView1.CameraPosition = [0.005, 0.005, 0.0335]
    renderView1.CameraFocalPoint = [0.005, 0.005, 0.0]
    renderView1.CameraParallelScale = 0.007071067811865475

    # --------------------------------------------
    # uncomment the following to render all views
    # RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).

    # save animation


def iterateFiles(folder_path, output_folder):
    for root, dirs, files in os.walk(folder_path):
        for directory in dirs:
            if directory.startswith("r"):
                dir_path = os.path.join(root, directory)
                file_path = os.path.join(dir_path, "melt_pool_out.e")
                if os.path.isfile(file_path):
                    new_folder_path = os.path.join(output_folder, directory)
                    os.makedirs(new_folder_path, exist_ok=True)
                    print("New folder created:", new_folder_path)
                    processData(file_path, directory)


folder_path = (
    r"C:\Users\Aashman Sharma\Documents\Paraview\Sample_Data\Case_1"  # data folder path
)
output_folder = r"C:\Users\Aashman Sharma\Documents\Paraview\Sample_Data\Case_1_output"  # output folder path
iterateFiles(folder_path, output_folder)
