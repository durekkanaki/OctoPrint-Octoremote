# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin
import serial
from threading import Thread
from time import sleep

class OctoremotePlugin(octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin,
                       octoprint.plugin.TemplatePlugin,
					   octoprint.plugin.StartupPlugin):

	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(
			# put your plugin's default settings here
		)

	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/OctoRemote.js"],
			css=["css/OctoRemote.css"],
			less=["less/OctoRemote.less"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			OctoRemote=dict(
				displayName="Octoremote Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="pkElectronics",
				repo="OctoPrint-Octoremote",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/pkElectronics/OctoPrint-Octoremote/archive/{target_version}.zip"
			)
		)
	def on_after_startup(self):
		thread = SerialThread(4)
		thread.start()
		self._logger.info("Hello World!")

	def get_template_vars(self):
        return dict(port=self._settings.get(["port"]))
			
	def get_settings_defaults(self):
        return dict(port="/dev/ttyAMA0")


	
# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Octoremote Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = OctoremotePlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

class SerialThread(Thread):

	portname = ""
	cbClass = null
	baudrate = 9600
	interrupted = false

	def __init__(self,callbackClass,pname,brate):
		Thread.__init__(self)
		portname = pname
		cbClass = callbackClass
		baudrate = brate
		self.port = serial.Serial(portname, baudrate=115200, timeout=3.0)
		callbackClass._logger.exception("test")
		

	def run(self):
		while self.interrupted = false:
			pass
			
	
	def interrupt():
		interrupted = true