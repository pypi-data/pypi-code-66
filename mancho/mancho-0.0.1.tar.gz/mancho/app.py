# SPDX-License-Identifier: GPL-3.0-only

import os

import soundfile as sf

from .audio import AudioPlayer
from .wave_display import AnimatedWaveDisplay

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk  # noqa


class App:

    def __init__(self):
        self.builder = Gtk.Builder()
        print(__file__)
        gladefile_path = os.path.join(os.path.dirname(__file__), "static",
                                      "main.glade")
        self.builder.add_from_file(gladefile_path)
        self.builder.connect_signals(self)
        main_window = self.builder.get_object("main_window")
        main_box = self.builder.get_object("main_box")
        self.wave_display = AnimatedWaveDisplay()
        self.wave_display.connect("selection-updated",
                                  self.on_selection_updated)
        main_box.pack_start(self.wave_display, True, True, 0)
        main_window.show_all()

        self.file_dialog = self.builder.get_object("open_dialog")
        self.file_dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                     Gtk.STOCK_OPEN, Gtk.ResponseType.OK)

        self.audio_player = AudioPlayer()
        self.marked_time = None

    def on_quit(self, *args):
        self.audio_player.stop()
        Gtk.main_quit()

    def on_selection_updated(self, wave_display, selection0, selection1):
        self.time_selection = (selection0, selection1)
        self.audio_player.stop()
        return True

    def on_open_clicked(self, *args):
        response = self.file_dialog.run()
        if response == Gtk.ResponseType.OK:
            path = self.file_dialog.get_filename()
            self.load_wav(path)
        self.file_dialog.hide()

    def on_main_window_key_press_event(self, window, event):
        def scroll_seconds(delta):
            self.wave_display.set_display_range(
                [i+delta for i in
                 self.wave_display.display_range])

        def zoom(zoom_factor):
            zoom_diff = (self.wave_display.display_range[1] -
                         self.wave_display.display_range[0])*zoom_factor

            self.wave_display.set_display_range(
                [self.wave_display.display_range[0] + zoom_diff,
                 self.wave_display.display_range[1] - zoom_diff]
            )

        if event.keyval == 65363:  # Right arrow
            scroll_seconds(1)
        elif event.keyval == 65361:  # Left arrow
            scroll_seconds(-1)
        elif event.keyval == 65362:  # Up arrow
            zoom(0.1)
        elif event.keyval == 65364:  # Down arrow
            zoom(-0.1)
        elif event.keyval == 97:  # a
            offset = (0 if self.time_selection is None
                      else self.time_selection[0])
            playback_time = offset + self.audio_player.playback_time
            if self.marked_time is None:
                self.marked_time = playback_time
            else:
                self.time_selection = sorted([self.marked_time, playback_time])
                self.wave_display.set_selection(self.time_selection)
                self.marked_time = None
                self.audio_player.stop()
        elif event.keyval == 32:  # Spacebar
            self.on_play_pause_clicked()
        else:
            return False
        return True

    def on_play_pause_clicked(self, *args):
        if self.audio_player.is_playing:
            self.audio_player.stop()
        else:
            speed = self.builder.get_object("speed_scale").get_value() / 100
            if self.time_selection:
                start_sample = int(self.time_selection[0]*self.sampling_rate)
                end_sample = int(self.time_selection[1]*self.sampling_rate)
            else:
                start_sample = 0
                end_sample = len(self.data)
            self.audio_player.play(self.data[start_sample:end_sample],
                                   self.sampling_rate, playback_speed=speed)

    def load_wav(self, path):
        self.data, self.sampling_rate = sf.read(path)
        self.wave_display.update_data(self.data, self.sampling_rate)
        # TODO remove magic numbers [0-10]
        self.time_selection = None
        self.wave_display.set_display_range([0, 10])
        self.wave_display.set_selection(None)
        self.audio_player.stop()

    def run(self):
        Gtk.main()
