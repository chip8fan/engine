if [ ! -d "lichess-bot" ]; then
    git clone https://github.com/chip8fan/lichess-bot.git
else
    echo "Directory ${PWD}/lichess-bot exists!"
fi
if [ ! -d "bin" ]; then
    echo "Creating directory ${PWD}/bin..."
    mkdir "bin"
else
    echo "Directory ${PWD}/bin already exists!"
fi
cd "bin"
if [ ! -f "book.bin" ]; then

fi
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
    if [ -d "lc0" ]; then
        sudo rm -rf lc0
    fi
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
    cd ..
else
    echo "Leela already exists at ${PWD}/lc0/lc0!"
fi
if [ ! -f "patricia" ]; then
    git clone https://github.com/Adam-Kulju/Patricia.git
    cd Patricia/engine
    make
    mv patricia ../../patricia-bin
    cd ../..
    sudo rm -rf Patricia
    mv patricia-bin patricia
else
    echo "Patricia already exists at ${PWD}/patricia!"
fi
if [ ! -f "arasan" ]; then
    git clone --recursive https://github.com/jdart1/arasan-chess.git
    cd arasan-chess/src
    make
    mv ../bin/arasanx-64 ../../arasan
    cd ../..
    sudo rm -rf arasan-chess
else
    echo "Arasan already exists at ${PWD}/arasan!"
fi
if [ ! -d "maia-chess" ]; then
    git clone https://github.com/CSSLab/maia-chess.git
fi
for rating in $(seq 1100 100 1900); do
    if [ ! -d "maia${rating}" ]; then
        mkdir "maia${rating}"
        mv "maia-chess/maia_weights/maia-${rating}.pb.gz" "maia${rating}/maia-${rating}.pb.gz"
        cp lc0/lc0 "maia${rating}/lc0"
    else
        echo "Maia${rating} already exists at ${PWD}/maia${rating}!"
    fi
done
if [ ! -d "LeelaNets" ]; then
    git clone https://github.com/CallOn84/LeelaNets.git
fi
if [ ! -d "maia2200" ]; then
    mkdir "maia2200"
    mv "LeelaNets/Nets/Maia 2200/maia-2200.pb.gz" "maia2200/maia-2200.pb.gz"
    cp lc0/lc0 "maia2200/lc0"
else
    echo "Maia2200 already exists at ${PWD}/maia2200!"
fi
if [ ! -d "eliteleela-v1" ]; then
    mkdir "eliteleela-v1"
    mv "LeelaNets/Nets/Elite Leela/Elite-Leela-v1-128x10b-200000.pb.gz" "eliteleela-v1/eliteleela-v1.pb.gz"
    cp lc0/lc0 "eliteleela-v1/lc0"
else
    echo "EliteLeela-v1 already exists at ${PWD}/eliteleela-v1!"
fi
if [ ! -d "eliteleela-v2" ]; then
    mkdir "eliteleela-v2"
    mv "LeelaNets/Nets/Elite Leela/Elite-Leela-v2-128x10x8h-1704000.pb.gz" "eliteleela-v2/eliteleela-v2.pb.gz"
    cp lc0/lc0 "eliteleela-v2/lc0"
else
    echo "EliteLeela-v2 already exists at ${PWD}/eliteleela-v2!"
fi