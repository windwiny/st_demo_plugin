import os
import subprocess
import sublime, sublime_plugin

class RuncmdCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#self.view.insert(edit, 0, '')
		fn = sublime.active_window().active_view().file_name()
		di = os.path.dirname(fn)
		dr = di[0:2]
		_, ext = os.path.splitext(fn)
		if ext == '.py':
			setpath = r' && set path=e:\ux\python27;%PATH%'
		elif ext == '.rb':
			setpath = r' && setruby'
		else:
			setpath = ''
		subprocess.Popen('cmd  /k cd %s && %s %s' % (di, dr, setpath) )

class ExecfileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		fn = sublime.active_window().active_view().file_name()
		_, ext = os.path.splitext(fn)
		if ext == '.py':
			subprocess.Popen(r'cmd /k e:\ux\python27\python  "%s" && echo. && pause && exit' % fn)
		elif ext == '.rb':
			subprocess.Popen(r'cmd /k e:\ux\ruby2\bin\ruby   "%s" && echo. && pause && exit' % fn)

