if [ ! -d "bin" ]; then
    echo "Creating directory ${PWD}/bin..."
    mkdir "bin"
else
    echo "Directory ${PWD}/bin already exists!"
fi
cd "bin"
if [ ! -d "syzygy" ]; then
    echo "Downloading EGTBs..."
    python3 ../lichess-bot/engines/get_egtb.py
else
    echo "EGTBs already exist at ${PWD}/syzygy!"
fi
if [ ! -f "stockfish" ]; then
    echo "Installing Stockfish..."
    git clone https://github.com/official-stockfish/Stockfish.git
    cd Stockfish/src
    make build
    mv stockfish ../../stockfish-bin
    cd ../..
    sudo rm -rf Stockfish
    mv stockfish-bin stockfish
else
    echo "Stockfish already exists at ${PWD}/stockfish!"
fi
if [ ! -f "lc0/lc0" ]; then
    echo "Installing Leela..."
    git clone https://github.com/LeelaChessZero/lc0.git
    cd lc0
    ./build.sh
    mv build/release/lc0 ../lc0-bin
    cd ..
    sudo rm -rf lc0
    mkdir lc0
    mv lc0-bin lc0/lc0
    cd lc0
    python3 ../../lichess-bot/engines/get_network.py
else
    echo "Leela already exists at ${PWD}/lc0/lc0!"
fi