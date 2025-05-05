struct Round
{
  string white_move;
  string black_move;
};

std::deque<Round> rounds;

// How many rounds are stored?
rounds.size()

// Access a round
rounds[i].white_move.c_str()

// Clear the container
rounds.clear();

// Insert or remove elements
rounds.pop_back();
rounds.push_back(round);

// Save the captured pieces
std::vector<char> white_captured;
std::vector<char> black_captured;

cout << "WHITE captured: ";
for (unsigned i = 0; i < game.white_captured.size(); i++)
{
   cout << char(game.white_captured[i]) << " ";
}

cout << "black captured: ";
for (unsigned i = 0; i < game.black_captured.size(); i++)
{
   cout << char(game.black_captured[i]) << " ";
}
