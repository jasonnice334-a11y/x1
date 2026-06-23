import x1
import os

def start_tool():
    print("-" * 30)
    print("      X1 TOOL STARTING...     ")
    print("-" * 30)
    
    funcs = dir(x1)
    
    if "main" in funcs:
        x1.main()
    elif "menu" in funcs:
        x1.menu()
    elif "start" in funcs:
        x1.start()
    else:
        print("Available functions in x1:", [f for f in funcs if not f.startswith("__")])
        print("\nPlease use one of the functions above.")

if __name__ == "__main__":
    try:
        start_tool()
    except Exception as e:
        print(f"Error: {e}")
