"""
Teams Automation Engine Module
Handles clipboard copying, keystroke emulation, timing, and emergency fail-safes.
Cross-platform compatible (Windows, Linux, macOS).
"""

import time
import threading
import pyautogui
import pyperclip

# Windows-only sound module fallback
try:
    import winsound
except ImportError:
    winsound = None

def _beep(freq=850, duration=150):
    """Cross-platform audible beep."""
    if winsound:
        try:
            winsound.Beep(freq, duration)
            return
        except Exception:
            pass
    # Terminal bell character for Linux/macOS
    try:
        print("\a", end="", flush=True)
    except Exception:
        pass

def _message_beep():
    """Cross-platform completion sound."""
    if winsound:
        try:
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
            return
        except Exception:
            pass
    try:
        print("\a", end="", flush=True)
    except Exception:
        pass

# Enable PyAutoGUI fail-safe: Moving the mouse to any corner stops the automation
pyautogui.FAILSAFE = True

class TeamsAutomator:
    def __init__(self):
        self.is_running = False
        self.stop_requested = False
        self._thread = None

    def start(self, member_list, delay=1.5, callbacks=None):
        """
        Starts the member addition in a background thread.
        Callbacks dictionary:
            - on_countdown(sec)
            - on_progress(current, total, email)
            - on_complete(total)
            - on_stop(current, total)
            - on_failsafe()
            - on_error(err)
        """
        if self.is_running:
            return False

        self.is_running = True
        self.stop_requested = False
        callbacks = callbacks or {}

        self._thread = threading.Thread(
            target=self._run_worker,
            args=(member_list, delay, callbacks),
            daemon=True
        )
        self._thread.start()
        return True

    def stop(self):
        """Requests cancellation of the ongoing automation."""
        if self.is_running:
            self.stop_requested = True

    def _run_worker(self, member_list, delay, callbacks):
        total = len(member_list)

        # 5-second countdown with audible beeps
        for sec in range(5, 0, -1):
            if self.stop_requested:
                break
            if "on_countdown" in callbacks:
                callbacks["on_countdown"](sec)
            _beep(850, 150)
            time.sleep(1)

        if self.stop_requested:
            self.is_running = False
            if "on_stop" in callbacks:
                callbacks["on_stop"](0, total)
            return

        _beep(1200, 300)

        success_count = 0
        try:
            for idx, member in enumerate(member_list, 1):
                if self.stop_requested:
                    break

                email = member["email"]
                if "on_progress" in callbacks:
                    callbacks["on_progress"](idx, total, email)

                # Paste email via clipboard (prevents character encoding bugs)
                pyperclip.copy(email)
                time.sleep(0.05)
                pyautogui.hotkey("ctrl", "v")

                # Wait for directory lookup resolution
                time.sleep(max(0.5, delay))

                # Press Enter to select the user tag
                pyautogui.press("enter")
                time.sleep(0.4)

                success_count += 1

            if not self.stop_requested:
                _message_beep()
                if "on_complete" in callbacks:
                    callbacks["on_complete"](success_count)
            else:
                if "on_stop" in callbacks:
                    callbacks["on_stop"](success_count, total)

        except pyautogui.FailSafeException:
            if "on_failsafe" in callbacks:
                callbacks["on_failsafe"]()
        except Exception as e:
            if "on_error" in callbacks:
                callbacks["on_error"](e)
        finally:
            self.is_running = False
