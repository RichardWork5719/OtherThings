#include <iostream>
#include <cmath>
#include <windows.h>
#include <array>
#include <vector>
#include <chrono>
#include <iomanip>
#include <algorithm>

//using namespace std;
using namespace std::chrono;

/*
class Planet{
    public:
        float mass = 0;
        float diametre = 0;

        float calculateGravity(){
            return ((6.673 * pow(10,-11)) * mass / (diametre));
        }
};
*/

/*
class Cruiser
{
    public:
    string creator;
    string model;
    string cruiserClass;
    int price;

    Cruiser(string creator, string model, string cruiserClass, int price)
    {
        this->creator = creator;
        this->model = model;
        this->cruiserClass = cruiserClass;
        this->price = price;
    }

    void printInfo()
    {
        cout << "Creator: " << creator << std::endl;
        cout << "Model: " << model << std::endl;
        cout << "Class: " << cruiserClass << std::endl;
        cout << "Price: " << price << std::endl;
    }

    void setCreator(string creator)
    {
        this->creator = creator;
    }

    void setModel(string model)
    {
        this->model = model;
    }

    void setCruiserClass(string cruiserClass)
    {
        if (cruiserClass == "Light" || cruiserClass == "Medium" || cruiserClass == "Heavy")
        {
            this->cruiserClass = cruiserClass;
        }
        else {
            cout << "Invalid cruiser class" << std::endl;
        }
    }

    void setPrice(int price)
    {
        if(price < 0)
        {
            cout << "Invalid price" << std::endl;
            return;
        }

        this->price = price;
    }

    void getCreator()
    {
        cout << "Creator: " << creator << std::endl;
    }

    void getModel()
    {
        cout << "Model: " << model << std::endl;
    }

    void getCruiserClass()
    {
        cout << "Class: " << cruiserClass << std::endl;
    }

    void getPrice()
    {
        cout << "Price: " << price << std::endl;
    }

};

void CluckMouse(int x, int y){
    INPUT input = {0};
    input.type = INPUT_MOUSE;
    input.mi.dwFlags = MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP;
    input.mi.dx = (x * 65535) / GetSystemMetrics(SM_CXSCREEN);
    input.mi.dy = (y * 65535) / GetSystemMetrics(SM_CYSCREEN);
    SendInput(1, &input, sizeof(INPUT));
}

int main()
{
    Cruiser cruiser("Navy", "Destroyer", "Light", 1000000);
    cruiser.printInfo();
    cruiser.setCreator("Mendel");
    cruiser.printInfo();



    return 0;
}
*/


/* MAIN ENTITY SHIT */
/*
class Entity{
    string NAME;
    string TYPE;

    float MAXHP;
    float HP;
    float DMG;
    int LVL;

public:
    Entity(string name, string type, float maxHp, float hp, float dmg, int lvl){
        NAME = name;
        TYPE = type;
        MAXHP = maxHp;
        HP = hp;
        DMG = dmg;
        LVL = lvl;
    }
    Entity(string name):Entity(name, "none", 1, 1, 0, 1){
        // if you only create an entity with a name it gives it some default values
    }

    void damageEntity(float damage){
        HP -= damage;
    }
    void healEntity(float amount){
        HP += amount;
        if(HP > MAXHP){
            HP = MAXHP;
        }
    }

    void attackEntity(Entity target){
        target.damageEntity(DMG);
    }
    void healOtherEntity(Entity target, float amount){
        target.healEntity(amount);
    }

    void setMaxHp(float newMax){
        MAXHP = newMax;
    }

    void lvlUpEntity(){
        LVL++;
    }

    void printEntityInfo(){
        cout << "Name: " << NAME << std::endl;
        cout << "Type: " << TYPE << std::endl;
        cout << "Max HP: " << MAXHP << std::endl;
        cout << "Current HP: " << HP << std::endl;
        cout << "Damage: " << DMG << std::endl;
        cout << "Level: " << LVL << std::endl;
    }
};
*/




/* THE GAME TUTORIAL */
/*
#include <cstdint>


typedef std::uint16_t hptype; // TODO: make this single line here a separate file called hitpointtypes.h and then include it in hp.h // this basically means we make the std::uint16_t into hptype so e can use it as a shortcut without needing to type the whole thing like a retard every time
//typedef std::cout print; // basing this off of the one above im making the whole std::cout into a shortcut called print (i hope this works)... NOPE DOESNT WORK LIKE THAT!!!

class hp{ // TODO:  make this header file called hp.h
    //hptype ShieldHP; // NEVERMIND HE JUST STRAIGHT UP FUCKING YEETED THE SHIELD
    hptype CurrentHP;
    hptype MaxHP;

public:
    bool setMaxHP(hptype new_max_hp){ // its a bool cuz it returns TRUE if successfull
        if(new_max_hp < 1){
            std::cout << "Max HP cannot be 0 or lower" << std::endl;
            return false;
        }

        MaxHP = new_max_hp;

        if(CurrentHP > MaxHP){
            CurrentHP = MaxHP;
        }

        std::cout << "New max HP has been set to: " << MaxHP << std::endl;
        return true;
    }

    hptype getCurrentHP(){
        return CurrentHP;
    }
    hptype getMaxHP(){
        return MaxHP;
    }

    void takeDamage(hptype damage){
        if (damage > CurrentHP){
            CurrentHP = 0;
            return;
        }
        */
        /*
        if (ShieldHP < damage){
            damage -= ShieldHP;
            ShieldHP = 0;
        }
        */
        /*
        CurrentHP -= damage;
    }

    void heal(hptype amount){
        if(amount + CurrentHP > MaxHP){
            CurrentHP = MaxHP;
            return;
        }

        CurrentHP += amount;
    }
};
*/

/*
#include <map.h>;
#include "map.h";
*/


/*
struct Structure{
protected:
    std::string NAME;
    char SYMBOL;

    std::string RESOURCES_REQUIRED;
    int AMOUNT_REQUIRED;

public:
    Structure(std::string name, char symbol, std::string resourcesRequired, int amountRequired){
        NAME = name;
        SYMBOL = symbol;

        RESOURCES_REQUIRED = resourcesRequired;
        AMOUNT_REQUIRED = amountRequired;
    }
};
struct FirePit: public Structure{
    std::string NAME = "fire";
    char SYMBOL = '*';

    std::string RESOURCES_REQUIRED = "wood";
    int AMOUNT_REQUIRED = 3;
};
*/




class Entity{
protected:
    int X;
    int Y;
    char SYMBOL;

public:
    Entity(int x, int y, char symbol){
        X = x;
        Y = y;
        SYMBOL = symbol;
    }

    int getX(){
        return X;
    }
    int getY(){
        return Y;
    }
    char getSymbol(){
        return SYMBOL;
    }

    void setX(int x){
        X = x;
    }
    void setY(int y){
        Y = y;
    }

    void MoveX(int x){
        X += x;
    }
    void MoveY(int y){
        Y += y;
    }

    void Interact(){
        //Do nothing for now
    } // no use right now

};


class Map{
    int X;
    int Y;

    std::vector<Entity*> MAPENTITIES;

    std::vector<std::vector<char>> MAP;//vector[50][20];

public:
    Map(int xSize, int ySize, int xPos, int yPos){
        MAP = std::vector<std::vector<char>>(ySize, std::vector<char>(xSize, ' ')); //std::array<std::array<std::string, x>, y>; //std::vector<std::vector<std::string>>(x, std::vector<std::string>(y, ' '));

        X = xPos;
        Y = yPos;

        UpdateMap();
    }
    ~Map(){
        for (int i = 0; i < MAPENTITIES.size(); ++i) {
            delete MAPENTITIES.at(i);
        }
    }

    int getX(){
        return X;
    }
    int getY(){
        return Y;
    }

    std::vector<std::vector<char>> getMap(){
        return MAP;
    }

    std::vector<Entity*> getEntityList(){
        return MAPENTITIES;
    }
    void removeEntityFromList(Entity* target){
        for (int i = 0; i < MAPENTITIES.size(); ++i) {
            if(MAPENTITIES.at(i) == target){
                MAPENTITIES.erase(MAPENTITIES.begin() + (i));
            }
        }
    }

    char getCharAt(int x, int y){
        return MAP.at(y).at(x);
    }

    void CleanMap(){
        for (int y = 0; y < MAP.size(); y++) {
            for (int x = 0; x < MAP.at(y).size(); x++) {
                MAP.at(y).at(x) = NULL;
            }
        }
    }
    void WriteOutMap(){
        for (int i = 0; i < MAPENTITIES.size(); ++i) {
            int Xloc = MAPENTITIES.at(i)->getX();
            int Yloc = MAPENTITIES.at(i)->getY();
            char symb = MAPENTITIES.at(i)->getSymbol();

            MAP.at(Yloc).at(Xloc) = symb;
        }
    }

    void printMap(){
        //system("cls"); // TODO: DELETE OR MOVE THIS LATER
        for (int y = 0; y < MAP.size(); y++) {
            for (int x = 0; x < MAP.at(y).size(); x++) {
                if(MAP.at(y).at(x) != NULL){
                    std::cout << MAP.at(y).at(x); // << setw(3) << MAP.at(row).at(column);
                }
                else{
                    std::cout << "-"; // << setw(3) << '#';
                }

            }

            std::cout << std::endl;
        }
        //system("echo press enter to proceed"); // TODO: DELETE THIS LATER
        //system("pause > nul"); // TODO: MOVE THIS LATER
    }

    void UpdateMap(){
        CleanMap();
        WriteOutMap();
    }

    void UpdateAndPrint(){
        UpdateMap();
        printMap();
    }

    void CreateWalls(){
        for(int y = 0; y < MAP.size(); y++){
            for(int x = 0; x < MAP.at(y).size(); ++x){
                if(x == 0 || x == MAP.at(y).size()-1 || y == 0 || y == MAP.size()-1){
                    CreateEntity(x, y, '#'); //MAP.at(y).at(x) = '#';
                }
            }
        }
        UpdateMap();
    }
    void DestroyWalls(){
        for (int o = 0; o < 8; ++o) { //the 'o' is how many times we want to iterate the wipe just incase it needs to be wiped more than once (last time it needed to be 8 but lets hope its not always like that)
            for (int i = 0; i < MAPENTITIES.size(); ++i) {
                auto entity = MAPENTITIES.at(i);
                if(entity->getSymbol() == '#'){
                    delete entity;
                    MAPENTITIES.erase(MAPENTITIES.begin() + (i));
                }
            }
        }
        UpdateMap();
    }

    void GenerateMapWithEntity(int amount, char entityCh){
        for (int i = 0; i < amount; i++) {
            int x, y;
            //std::srand(time(nullptr));
            x = std::rand() % (MAP.at(0).size()-1) + 1;
            y = std::rand() % (MAP.size()-1) + 1;

            if(getCharAt(x, y) == NULL){
                //std::cout << "X = " << x << std::endl;
                //std::cout << "Y = " << y << std::endl;
                CreateEntity(x, y, entityCh);
            }
            else{
                i--;
            }
        }
        UpdateMap();
    }


    void addExistingEntityToMap(Entity* target){
        MAPENTITIES.push_back(target);

        UpdateMap();
    }
    void CreateEntity(int x, int y, char symbol){
        Entity* creation = new Entity(x, y, symbol);
        addExistingEntityToMap(creation);

        UpdateMap();
    }

    void DestroyEntityAt(int x, int y){
        for (int i = 0; i < MAPENTITIES.size(); ++i) {
            int Xloc = MAPENTITIES.at(i)->getX();
            int Yloc = MAPENTITIES.at(i)->getY();
            //char symb = MAPENTITIES.at(i)->getSymbol();
            if(Xloc == x and Yloc == y){
                auto target = MAPENTITIES.at(i);
                delete target;
                MAPENTITIES.erase(MAPENTITIES.begin() + (i));
            }
        }
        UpdateMap();
    }
};


class MapManager{
    int XSIZE;
    int YSIZE;


    std::vector<Map*> MAPLIST;

    Map* CURRENTMAP;

public:
    MapManager(int xSize, int ySize){
        XSIZE = xSize;
        YSIZE = ySize;

        CURRENTMAP = CreateAndOrMoveToMap(0, 0);
    }
    ~MapManager(){
        for (int i = 0; i < MAPLIST.size(); ++i) {
            delete MAPLIST.at(i);
        }
    }

    void CreateMap(int xPos, int yPos){
        Map* map = new Map(XSIZE, YSIZE, xPos, yPos);
        MAPLIST.push_back(map);
    }

    int getX(){
        return XSIZE;
    }
    int getY(){
        return YSIZE;
    }

    std::vector<Map*> getMapList(){
        return MAPLIST;
    }

    Map* CreateAndOrMoveToMap(int xPos, int yPos){
        for (int i = 0; i < MAPLIST.size(); ++i) {
            if(MAPLIST.at(i)->getX() == xPos and MAPLIST.at(i)->getY() == yPos){
                return MAPLIST.at(i);
            }
        }
        CreateMap(xPos, yPos);
        for (int i = 0; i < MAPLIST.size(); ++i) {
            if(MAPLIST.at(i)->getX() == xPos and MAPLIST.at(i)->getY() == yPos){
                return MAPLIST.at(i);
            }
        }
    }

    void setCurrentMap(Map* target){
        CURRENTMAP = target;
    }
    Map* getCurrentMap(){
        return CURRENTMAP;
    }

};


class Player: public Entity{
    float HP = 100;
    float HUNGER = 100;

    MapManager* MAPMANAGER;

    Map* CURRENTMAP;

    std::vector<std::string> INVENTORY;

public:
    Player(int x, int y, char symbol, MapManager* mapManager): Entity(x, y, symbol){
        MAPMANAGER = mapManager;

        CURRENTMAP = MAPMANAGER->getCurrentMap();
    }

    void Move(std::string direction){
        HUNGER -= 0.5;
        if(direction == "w"){
            auto targetTile = CURRENTMAP->getCharAt(X, Y-1);
            std::cout << "You walk into a tile with: " << targetTile << std::endl;
            if(targetTile == NULL){
                MoveY(-1);
            }
            else{
                giveLoot(X, Y-1);
            }
        }
        else if(direction == "s"){
            auto targetTile = CURRENTMAP->getCharAt(X, Y+1);
            std::cout << "You walk into a tile with: " << targetTile << std::endl;
            if(targetTile == NULL){
                MoveY(1);
            }
            else{
                giveLoot(X, Y+1);
            }
        }
        else if(direction == "a"){
            auto targetTile = CURRENTMAP->getCharAt(X-1, Y);
            std::cout << "You walk into a tile with: " << targetTile << std::endl;
            if(targetTile == NULL){
                MoveX(-1);
            }
            else{
                giveLoot(X-1, Y);
            }
        }
        else if(direction == "d"){
            auto targetTile = CURRENTMAP->getCharAt(X+1, Y);
            std::cout << "You walk into a tile with: " << targetTile << std::endl;
            if(targetTile == NULL){
                MoveX(1);
            }
            else{
                giveLoot(X+1, Y);
            }
        }
        else{
            std::cout << "Unknown input: " << direction << std::endl;
        }
        CheckPlayer();
    }

    void giveLoot(int x, int y){
        if(CURRENTMAP->getCharAt(x, y) == 'T'){
            CURRENTMAP->DestroyEntityAt(x, y);
            INVENTORY.push_back("wood");
        }
        else if(CURRENTMAP->getCharAt(x, y) == 'C'){
            CURRENTMAP->DestroyEntityAt(x, y);
            INVENTORY.push_back("raw meat");
        }
        else if(CURRENTMAP->getCharAt(x, y) == '*'){
            if(count(INVENTORY.begin(), INVENTORY.end(), "raw meat") > 0){
                INVENTORY.erase(std::find(INVENTORY.begin(), INVENTORY.end(), "raw meat"));
                INVENTORY.push_back("cooked meat");
            }
        }
    }

    void printInventory(){
        std::cout << "Items in inventory: " << std::endl;
        int wood = count(INVENTORY.begin(), INVENTORY.end(), "wood");
        int rawMeat = count(INVENTORY.begin(), INVENTORY.end(), "raw meat");
        int cookedMeat = count(INVENTORY.begin(), INVENTORY.end(), "cooked meat");
        /*
        for (int i = 0; i < INVENTORY.size(); ++i) {
            if(INVENTORY.size() == i+1){
                //std::cout << INVENTORY.at(i);
            }
            else{
                //std::cout << INVENTORY.at(i) << ", ";
            }
        }
        */
        std::cout << "|Wood: " << wood;
        std::cout << "|Raw Meat: " << rawMeat;
        std::cout << "|Cooked Meat: " << cookedMeat;
        std::cout << std::endl;
    }

    void Build(std::string structure, std::string direction){
        if(structure == "fire"){
            if(count(INVENTORY.begin(), INVENTORY.end(), "wood") >= 3){
                INVENTORY.erase(std::find(INVENTORY.begin(), INVENTORY.end(), "wood"));
                INVENTORY.erase(std::find(INVENTORY.begin(), INVENTORY.end(), "wood"));
                INVENTORY.erase(std::find(INVENTORY.begin(), INVENTORY.end(), "wood"));
                int x = X;
                int y = Y;
                Move(direction);
                CURRENTMAP->CreateEntity(x, y, '*');
            }
            else{
                std::cout << "You dont have enough wood" << std::endl;
            }
        }
        else{
            std::cout << "Invalid order" << structure << " " << direction << std::endl;
        }
    }

    void Eat(){
        if(count(INVENTORY.begin(), INVENTORY.end(), "cooked meat") > 0){
            INVENTORY.erase(std::find(INVENTORY.begin(), INVENTORY.end(), "cooked meat"));
            HUNGER += 20;
            if(HUNGER > 100){
                HUNGER = 100;
            }
        }
        else{
            std::cout << "You dont have any cooked food" << std::endl;
        }
    }

    void CheckHungerAndHP(){
        if(HUNGER <= 0){
            HUNGER = 0;
            HP -= 1;
        }
        if(HP <= 0){
            HP = 0;
            //TODO: make the player fucking die
        }
        if(HUNGER > 80){
            HP += 0.2;
        }
        if(HP > 100){
            HP = 100;
        }
    }


    void CheckLocation(){
        int maxX = MAPMANAGER->getX()-1;
        int maxY = MAPMANAGER->getY()-1;
        // TODO: add a map switch
        if(X >= maxX || X <= 0 || Y >= maxY || Y <= 0){
            CURRENTMAP->removeEntityFromList(this);
            int newX = MAPMANAGER->getCurrentMap()->getX()+1;
            int newY = MAPMANAGER->getCurrentMap()->getY();
            //CURRENTMAP = MAPMANAGER->CreateAndOrMoveToMap(newX, newY);
            MAPMANAGER->setCurrentMap(MAPMANAGER->CreateAndOrMoveToMap(newX, newY));
            CURRENTMAP->addExistingEntityToMap(this);
            X = 0;
        }
    }


    void CheckPlayer(){
        CheckHungerAndHP();
        CheckLocation();
    }

    void printStats(){
        std::cout << "HP = " << HP << std::endl;
        std::cout << "Hunger = " << HUNGER << std::endl;
        printInventory();
    }
};


class Game{
    bool RUNNING = false;

public:
    void StartGame(int x, int y){
        RUNNING = true;
        std::srand(time(nullptr));

        MapManager* mapManager = new MapManager(x, y);


        //Map* map = new Map(x, y, 0, 0);
        mapManager->getCurrentMap()->CreateWalls();
        mapManager->getCurrentMap()->GenerateMapWithEntity(10, 'T');
        mapManager->getCurrentMap()->GenerateMapWithEntity(10, 'C');
        mapManager->getCurrentMap()->GenerateMapWithEntity(10, 'E');

        Player* THEPLAYER = new Player(int(x/2), int(y/2), 'P', mapManager);
        mapManager->getCurrentMap()->addExistingEntityToMap(THEPLAYER);

        bool firstMapFinished = false;

        while(RUNNING){
            //system("cls");
            THEPLAYER->printStats();
            mapManager->getCurrentMap()->UpdateAndPrint();
            std::string input;
            std::cout << "Command: ";
            std::cin >> input;
            system("cls");
            if(input == "w" || input == "s" || input == "a" || input == "d"){
                THEPLAYER->Move(input);
            }
            else if(input == "i" || input == "inv" || input == "inventory"){
                THEPLAYER->printInventory();
            }
            else if(input == "fire"){
                THEPLAYER->Build("fire", "w");
            }
            else if(input == "eat"){
                THEPLAYER->Eat();
            }
            else if(input == "exit" || input == "quit"){
                RUNNING = false;
                std::cout << "Exiting..." << std::endl;
            }

            if(firstMapFinished == false){
                bool foundChicken = false;
                auto entityList = mapManager->getCurrentMap()->getEntityList();
                for (int i = 0; i < entityList.size(); ++i) {
                    if(entityList.at(i)->getSymbol() == 'C'){
                        foundChicken = true;
                    }
                }
                if(foundChicken == false){
                    firstMapFinished = true;
                    mapManager->getCurrentMap()->DestroyWalls();
                }
            }

            //system("pause > nul");
            //system("cls");
        }
        ExitGame(mapManager->getCurrentMap());
    }

    void ExitGame(Map* map){
        delete map;
    }
};














int main(){
    auto start = high_resolution_clock::now();

    /*
    for(int i = 0; i < 1000; i++){
        cout << i << std::endl;
    }
    */
    //Entity *Sheep = new Entity("Sheep");

    //Sheep->printEntityInfo();



    Game* game = new Game();

    game->StartGame(50, 20);



    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Time taken by function: " << duration.count()/1000 << " seconds or: " << duration.count() << " milliseconds";
    system("pause > nul");
    return 0;
}
