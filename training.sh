git clone https://github.com/DanielUranga/trainingdata-tool.git
cd trainingdata-tool
git clone https://github.com/DanielUranga/lc0.git
cd lc0
git checkout 015583a28bebf961e5032232224c80f12c49f827
cd ..
git clone https://github.com/DanielUranga/polyglot.git
cd polyglot
git checkout 830fa946748cb23b19d8017fdcf0937520121dc6
cd ..
git clone https://github.com/madler/zlib.git
read
cmake .
cmake --build .
mv trainingdata-tool tool
mv tool ..
cd ..
sudo rm -rf trainingdata-tool
mv tool trainingdata-tool