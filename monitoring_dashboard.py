import curses, psutil, os, time

def draw_dashboard(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    pid = os.getpid()
    proc = psutil.Process(pid)
    proc.cpu_percent(interval=None)

    while True:
        stdscr.clear()
        stdscr.border(0)
        stdscr.addstr(1, 2, "PQES Resource Monitor", curses.A_BOLD)
        
        time.sleep(0.5)
        cpu = proc.cpu_percent(interval=None)
        ram = proc.memory_info().rss / 1024 / 1024  # MB

        stdscr.addstr(3, 4, f"PID: {pid}")
        stdscr.addstr(4, 4, f"CPU Usage: {cpu:.2f}%")
        stdscr.addstr(5, 4, f"RAM Usage: {ram:.2f} MB")
        
        sys_cpu = psutil.cpu_percent(interval=None)
        sys_ram = psutil.virtual_memory().used / 1024 / 1024

        stdscr.addstr(7, 4, f"Total CPU Usage: {sys_cpu:.2f}%")
        stdscr.addstr(8, 4, f"Total RAM Usage: {sys_ram:.2f} MB")

        stdscr.addstr(10, 2, "Press Ctrl+C to exit")
        stdscr.refresh()

try:
    curses.wrapper(draw_dashboard)
except KeyboardInterrupt:
    print("\n[Monitor] Exited.")
