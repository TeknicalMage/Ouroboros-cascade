$pos_img_folder = 'positive'

$posdottext = 'pos.txt'

$cascade_nfo = 'cascade'

$negdottext = 'neg.txt'

Write-host('Manual Deployment of cascade Classifer')
Write-Host('  ')

Start-Sleep -Seconds 1

Write-Host('Type Annotate for Manual Postive Image Isolatin')
Write-Host('Type Vector for pos.txt formating')
Write-Host('Type Train for Cascade Training')
Write-Host('')




function main{

    $selection = Read-Host

    if($selection -match 'Annotate'){
    
        H:\CVShenanigans\opencv\build\x64\vc15\bin\opencv_annotation.exe --annotations=pos.txt --images=$pos_img_folder
    }
    elseif($selection -match 'Vector'){
        H:\CVShenanigans\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info $posdottext -w 20 -h 20 -num 100 -vec pos.vec
    }
    elseif($selection -match 'Train'){
        H:\CVShenanigans\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data $cascade_nfo -vec pos.vec -bg $negdottext -w 20 -h 20 -numPos 30 -numNeg 80numNeg 80
    }  

}

main



