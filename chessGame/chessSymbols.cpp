void printChessPiecesUnicode()
{
   _setmode(_fileno(stdout), _O_WTEXT);
   std::wcout << L'\u2654' << ' ' <<  L'\u2655' << ' ' << L'\u2656' << ' ' 
              << L'\u2657' << ' ' << L'\u2658' << ' ' << L'\u2659' << endl;
   std::wcout << L'\u265A' << ' ' <<  L'\u265B' << ' ' << L'\u265C' << ' ' 
              << L'\u265D' << ' ' << L'\u265E' << ' ' << L'\u265F' << endl;
}
