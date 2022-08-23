import PySimpleGUI as sg
import os
import summarization as summ
import PictureExtractorV2 as pe
import PowerPointMaker as pp
import OsHelper
import TextExtractorV2 as teV2
import pipInstalling
import spacyCliDownload

pipInstalling.installPackages(pipInstalling.listOfPackages)
spacyCliDownload.spacyCliDownload()
sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = \
    {'BACKGROUND': '#97030C',
     'TEXT': '#FFFFFF',
     'INPUT': '#FFFFFF',
     'TEXT_INPUT': '#000000',
     'SCROLL': '#FBFBFB',
     'BUTTON': ('#97030C', '#FFFFFF'),
     'PROGRESS': ('#FD7D85', '#FFFFFF'),
     'BORDER': 1, 'SLIDER_DEPTH': 0,
     'PROGRESS_DEPTH': 0, }

sg.theme('DefaultNoMoreNagging')
sg.set_options(font='Franklin 14', )
welcom_layout=[[sg.Text('Welcome to presentation generator press start to get started')],
         [sg.Button('Start')]
         ]
load_file_layout=[
    [ sg.Image('pdf.png'),sg.Text('Choose a pdf file: ')],
    [ sg.InputText(key="-FILE PATH-"),
      sg.FileBrowse(file_types=[("pdf files","*.pdf")])
      ],
    [sg.Push(),
     sg.Text('Start page: ',),
     sg.InputText(key="-START PAGE-",size=(6,0),justification='center'),
     sg.Push(),
     sg.Text('End page: ',pad=(0,30)),
     sg.InputText(key="-END PAGE-",size=(6,0),justification='center'),
     sg.Push(),
    ],
    [sg.Text("Output file name")],
    [sg.InputText(key="-OUTPUT NAME-")],
    [sg.Button('Generate presentation', key="-GENERATE-")]

]

#layout2=[
 #   [sg.Text('Welcome to the new page')]
#]
window= sg.Window('Welcome',welcom_layout,)

while True:
    event,value=window.read()

    if event == sg.WIN_CLOSED:
        break
    if event=='Start':
        window.close()
        window=sg.Window('Automated Presentation Generation',load_file_layout)
    if event == "-GENERATE-":
        print(value['-FILE PATH-'])
        if len(str(value["-START PAGE-"]))!=0 and len(str(value["-END PAGE-"]))!=0 and len(str(value['-FILE PATH-']))!=0:

            if(str(value["-START PAGE-"]).isnumeric() and str(value["-END PAGE-"]).isnumeric()):
                #make summarization
                path = str(value['-FILE PATH-'])
                startPage= int(value["-START PAGE-"])
                endPage=int( value["-END PAGE-"])

                if(startPage>0):
                    startPage -=1
                pageRange = teV2.getNumPages(path)

                if(endPage>pageRange):
                    endPage = pageRange
                #text = te.extract(path, startPage,endPage)

                resultList = teV2.loadPages(path, startPage, endPage)
                titleAndTextAndPageList = teV2.extractTextV2(resultList)


                #summarizedText = []

                extractedImage = pe.image()
                extractedImage.extractAllImages(path, startPage,endPage)


                print(titleAndTextAndPageList[2][1])
                for i in range(len(titleAndTextAndPageList)):
                    summarizedText = summ.sumarize(titleAndTextAndPageList[i][1])
                    if len(summarizedText) > 1:
                        titleAndTextAndPageList[i][1] = summarizedText
                    sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, no_titlebar=False, time_between_frames=50)
                print(titleAndTextAndPageList[2][1])

                sg.popup_animated(None)
                print('done')
                pp.makePowerPoint(titleAndTextAndPageList,startPage,"No comment",str(value["-OUTPUT NAME-"]),extractedImage)
                window.close()
                os.startfile(str(value["-OUTPUT NAME-"])+".pptx")
                OsHelper.removePngs(extractedImage.imageName)
            else:
               sg.popup("Start page or end page is not numeric",title="Error")
        else:
            sg.popup("Some input values is empty",title="Error")

        #window.close()
        #window=sg.Window('HELLO',layout2)
    #print(path)
window.close()
