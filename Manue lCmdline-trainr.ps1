Write-host('PosFilter')


$var = 'H:\Projects\opencv_tutorials\008_cascade_classifier\positive'

$goods = 'H:\Projects\opencv_tutorials\008_cascade_classifier\pos.txt'

$casc = 'H:\Projects\opencv_tutorials\008_cascade_classifier\cascade'

$bads = 'H:\Projects\opencv_tutorials\008_cascade_classifier\neg.txt'

H:\CVShenanigans\opencv\build\x64\vc15\bin\opencv_annotation.exe --annotations=pos.txt --images=$var

#H:\CVShenanigans\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info pos.txt -w 20 -h 20 -num 100 -vec pos.vec


#H:\CVShenanigans\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data $casc -vec pos.vec -bg $bads -w 20 -h 20 -numPos 30 -numNeg 80numNeg 80